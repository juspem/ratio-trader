# Nasdaq–Gold Trading Bot

An educational Python project for learning APIs and data processing. The goal is to fetch Nasdaq and gold price data, calculate their ratio, and simulate a simple rotation strategy.

**Status:** fetches a quote for one symbol from Alpha Vantage. The strategy will be added later.

## Structure

- `src/trade_bot/` – application code
- `tests/` – automated tests
- `docs/` – design decisions
- `pyproject.toml` – package metadata and dependencies

## Getting started

Requires Python 3.12 or newer. Run in PowerShell from the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
```

Copy `.env.example` to `.env` and add your API key:

```dotenv
MARKET_DATA_API_KEY=your_api_key
```

Fetch a quote:

```powershell
.\.venv\Scripts\python.exe src/trade_bot/market_data.py
```

`.env` is a local text file ignored by Git. Keep real API keys out of source code and `.env.example`.
