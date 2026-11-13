# Tests

Tests cover loading a saved API key, handling a missing key, and fetching a quote using a simulated API response.

API tests use predefined responses. Running them must not require a real API key or consume the service's request quota.

Install the project following the main README, then run tests from the project root:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```
