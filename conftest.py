"""Pytest configuration and fixtures."""

import pytest
import requests
from src.config import BASE_URL


@pytest.fixture(scope="session")
def api_base_url():
    """Provide the base URL for API tests."""
    return BASE_URL


@pytest.fixture(scope="session")
def verify_api_health():
    """Verify API is accessible before running tests."""
    try:
        response = requests.get(f"{BASE_URL}/ping", timeout=10)
        if response.status_code != 201:
            pytest.skip("API is not healthy or accessible")
    except requests.exceptions.RequestException:
        pytest.skip("API is not accessible")


@pytest.fixture
def sample_booking_data():
    """Provide sample booking data for tests."""
    return {
        "firstname": "Test",
        "lastname": "User",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "WiFi"
    }