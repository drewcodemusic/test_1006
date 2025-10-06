import requests
import pytest
from src.config import BASE_URL


class TestGetBooking:
    def test_get_booking_valid_id(self):
        """Test GET booking with valid ID."""
        response = requests.get(f"{BASE_URL}/booking/3458")

        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        data = response.json()
        assert "firstname" in data, "Missing firstname"
        assert "lastname" in data, "Missing lastname"
        assert "depositpaid" in data, "Missing depositpaid"
        assert "totalprice" in data, "Missing totalprice"
        assert "bookingdates" in data, "Missing bookingdates"

    def test_get_booking_invalid_id(self):
        """Test GET booking with invalid ID."""
        response = requests.get(f"{BASE_URL}/booking/999999")

        assert response.status_code == 404, f"Expected 404, got {response.status_code}"

    def test_get_booking_non_numeric_id(self):
        """Test GET booking with non-numeric ID."""
        response = requests.get(f"{BASE_URL}/booking/invalid")

        assert response.status_code == 404, f"Expected 404, got {response.status_code}"