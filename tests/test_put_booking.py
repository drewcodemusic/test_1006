import requests
import pytest
from src.config import BASE_URL


class TestPutBooking:
    def test_put_booking_with_token(self, created_booking, auth_token):
        """Test PUT booking using token cookie authentication."""
        booking_id = created_booking["booking_id"]

        # Get the booking to verify initial data
        get_response = requests.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_response.status_code == 200, f"Failed to get booking: {get_response.status_code}"
        initial_data = get_response.json()
        assert initial_data["firstname"] == "Test"
        assert initial_data["totalprice"] == 150

        # PUT request with complete updated booking data
        put_data = {
            "firstname": "James",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Cookie": f"token={auth_token}"
        }

        put_response = requests.put(
            f"{BASE_URL}/booking/{booking_id}",
            json=put_data,
            headers=headers
        )

        assert put_response.status_code == 200, f"Expected 200, got {put_response.status_code}"
        updated_data = put_response.json()

        # Verify all fields were updated
        assert updated_data["firstname"] == "James", "Firstname was not updated"
        assert updated_data["lastname"] == "Brown", "Lastname was not updated"
        assert updated_data["totalprice"] == 111, "Total price was not updated"
        assert updated_data["depositpaid"] == True, "Depositpaid was not updated"
        assert updated_data["bookingdates"]["checkin"] == "2018-01-01", "Checkin date was not updated"
        assert updated_data["bookingdates"]["checkout"] == "2019-01-01", "Checkout date was not updated"
        assert updated_data["additionalneeds"] == "Breakfast", "Additional needs was not updated"
