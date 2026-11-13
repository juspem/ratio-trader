import io
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from trade_bot.market_data import main, read_api_key


class ApiKeyTests(unittest.TestCase):
    def test_reads_saved_key_with_windows_encoding(self):
        with TemporaryDirectory() as directory:
            env_path = Path(directory) / ".env"
            env_path.write_text("MARKET_DATA_API_KEY=test-key\n", encoding="utf-8-sig")

            self.assertEqual(read_api_key(env_path), "test-key")

    def test_missing_or_empty_key_is_rejected(self):
        with TemporaryDirectory() as directory:
            env_path = Path(directory) / ".env"
            for content in (None, "", "MARKET_DATA_API_KEY=\n"):
                with self.subTest(content=content):
                    if content is not None:
                        env_path.write_text(content, encoding="utf-8")
                    with self.assertRaisesRegex(ValueError, "MARKET_DATA_API_KEY"):
                        read_api_key(env_path)

    def test_missing_key_stops_before_network_request(self):
        with patch("trade_bot.market_data.read_api_key", side_effect=ValueError("Missing API key")):
            with patch("trade_bot.market_data.urlopen") as request:
                with self.assertRaisesRegex(SystemExit, "Missing API key"):
                    main()
                request.assert_not_called()

    def test_saved_key_is_used_without_prompting_or_printing_it(self):
        payload = b'{"Global Quote": {"01. symbol": "IBM", "05. price": "100.00", "07. latest trading day": "2026-11-12"}}'
        with patch("trade_bot.market_data.read_api_key", return_value="test-key"):
            with patch("trade_bot.market_data.urlopen") as request:
                response = io.BytesIO(payload)
                response.status = 200
                request.return_value.__enter__.return_value = response
                with patch("getpass.getpass", side_effect=AssertionError("Unexpected prompt")):
                    with patch("sys.stdout", new_callable=io.StringIO) as output:
                        main()
                self.assertIn("apikey=test-key", request.call_args.args[0])
                self.assertIn("HTTP status: 200", output.getvalue())
                self.assertIn("Symbol: IBM", output.getvalue())
                self.assertIn("Price: 100.00", output.getvalue())
                self.assertIn("Trading day: 2026-11-12", output.getvalue())
                self.assertNotIn("test-key", output.getvalue())
