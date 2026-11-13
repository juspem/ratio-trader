# Project structure and scope

## Goal

Build a small Python command-line application whose author can explain the entire flow from API requests to price processing and rule-based signals. The initial goal is a historical simulation using virtual funds.

## Chosen approach

Use Python and a market data API. A broker API is deferred because account configuration and order placement are not needed for the initial learning goal. A user interface can be added once the command-line application works.

## Current components

- `src/trade_bot/` contains the installable Python package.
- `tests/` contains tests that verify application behavior.
- `pyproject.toml` defines the package, Python version, and dependencies. `python-dotenv` reads the local `.env` configuration file.
- `market_data.py` reads the API key from the project root and fetches a quote for one symbol. A missing key stops the application before any network request.

## Components to add as needed

The API client handles HTTP requests and response validation. Calculations operate on validated price data so the strategy can be tested without network access. The command-line entry point connects these components and displays the result.

Storage and charts will be added after the initial data fetching and calculations work. Empty modules for future features are not created in advance.

## Open decisions

The first API integration uses Alpha Vantage, IBM as the example symbol, and Python's `urllib` library. Instruments representing Nasdaq and gold, along with the working currency, will be selected later.
