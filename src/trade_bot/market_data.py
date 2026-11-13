import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

from dotenv import dotenv_values


def read_api_key(env_path: Path) -> str:
    settings = dotenv_values(env_path, encoding="utf-8-sig", interpolate=False)
    api_key = (settings.get("MARKET_DATA_API_KEY") or "").strip()

    if not api_key:
        raise ValueError("Add MARKET_DATA_API_KEY to the .env file in the project root.")

    return api_key


def main() -> None:
    env_path = Path(__file__).resolve().parents[2] / ".env"
    try:
        api_key = read_api_key(env_path)
    except ValueError as error:
        raise SystemExit(str(error)) from None

    parameters = {
        "function": "GLOBAL_QUOTE",
        "symbol": "IBM",
        "apikey": api_key,
    }

    url = "https://www.alphavantage.co/query?" + urlencode(parameters)

    with urlopen(url, timeout=10) as response:
        print("HTTP status:", response.status)
        data = json.load(response)

    print(json.dumps(data, indent=2))

    quote = data["Global Quote"]

    symbol = quote["01. symbol"]
    price = quote["05. price"]
    trading_day = quote["07. latest trading day"]

    print("Symbol:", symbol)
    print("Price:", price)
    print("Trading day:", trading_day)


if __name__ == "__main__":
    main()
