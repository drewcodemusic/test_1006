import requests
import pytest
from src.config import BASE_URL


class TestPostBooking:
    def test_create_booking_valid_data(self):
        """Test POST booking with valid data."""
        booking_data = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{BASE_URL}/booking", json=booking_data, headers=headers)

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert "bookingid" in data, "Missing bookingid"
        assert "booking" in data, "Missing booking data"
        assert data["booking"]["firstname"] == "Jim", "Firstname mismatch"
        assert data["booking"]["lastname"] == "Brown", "Lastname mismatch"

    def test_create_booking_missing_firstname(self):
        """Test POST booking with missing firstname."""
        booking_data = {
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            }
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{BASE_URL}/booking", json=booking_data, headers=headers)

        assert response.status_code == 500, f"Expected 500, got {response.status_code}"

    def test_create_booking_missing_lastname(self):
        """Test POST booking with missing lastname."""
        booking_data = {
            "firstname": "John",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            }
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{BASE_URL}/booking", json=booking_data, headers=headers)

        assert response.status_code == 500, f"Expected 500, got {response.status_code}"

    def test_create_booking_invalid_price(self):
        """Test POST booking with invalid price."""
        booking_data = {
            "firstname": "Jane",
            "lastname": "Doe",
            "totalprice": "invalid",
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            }
        }

        headers = {"Content-Type": "application/json"}
        response = requests.post(f"{BASE_URL}/booking", json=booking_data, headers=headers)

        # The API appears to accept invalid price and convert it
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert "bookingid" in data, "Missing bookingid"