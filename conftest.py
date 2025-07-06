import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("API_URL", "https://yavshok.ru/api/v1")

@pytest.fixture
def api_client(base_url):
    from utils.api_client import ApiClient
    return ApiClient(base_url)