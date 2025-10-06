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


@pytest.fixture
def auth_token():
    """Get authentication token from the API."""
    auth_data = {
        "username": "admin",
        "password": "password123"
    }
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/auth", json=auth_data, headers=headers)

    assert response.status_code == 200, f"Failed to get auth token: {response.status_code}"
    token = response.json()["token"]

    yield token

    # Teardown: No cleanup needed for token


@pytest.fixture
def created_booking(sample_booking_data):
    """Create a booking and return the booking ID and data."""
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/booking", json=sample_booking_data, headers=headers)

    assert response.status_code == 200, f"Failed to create booking: {response.status_code}"
    data = response.json()

    return {
        "booking_id": data["bookingid"],
        "booking_data": data["booking"]
    }