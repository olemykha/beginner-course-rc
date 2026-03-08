import pytest
import requests
import logging
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Automation")


# --- URLs ---

@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"


@pytest.fixture(scope="session")
def ui_base_url():
    return "https://the-internet.herokuapp.com"


# --- API CLIENT ---

@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    api_key = "reqres_509acbecebc8471387c6a57Se754e637"

    session.headers.update({
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0",
        "x-api-key": api_key
    })

    logger.info(" [API SETUP] Session started.")
    yield session
    logger.info(" [API TEARDOWN] Closing session.")
    session.close()


# --- UI PAGE ---

@pytest.fixture(scope="function")
def page():
    logger.info(" [UI SETUP] Launching browser...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page_obj = context.new_page()
        yield page_obj
        logger.info(" [UI TEARDOWN] Closing browser.")
        context.close()
        browser.close()
