# Beginner course for RC.

## Structure
- `tests/api/`: Tests for ReqRes API (Requests)
- `tests/ui/`: Tests for HerokuApp (Playwright)
- `conftest.py`: Global fixtures and settings

## Install
1. `pip install -r requirements.txt`
2. `playwright install chromium`

## Launch
- **All tests:** `pytest -v -s --log-cli-level=INFO`
- **Only API:** `pytest tests/api`
- **Only UI:** `pytest tests/ui`
