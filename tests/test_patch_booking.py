import requests
import pytest
from src.config import BASE_URL


class TestPatchBooking:
    def test_patch_booking(self, created_booking):
        """Test PATCH booking using fixture to create booking first."""
        booking_id = created_booking["booking_id"]

        # Get the booking to verify initial data
        get_response = requests.get(f"{BASE_URL}/booking/{booking_id}")
        assert get_response.status_code == 200, f"Failed to get booking: {get_response.status_code}"
        initial_data = get_response.json()
        assert initial_data["firstname"] == "Test"
        assert initial_data["totalprice"] == 150

        # Patch the booking with updated data
        patch_data = {
            "firstname": "Newman",
            "totalprice": 200
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
        }

        patch_response = requests.patch(
            f"{BASE_URL}/booking/{booking_id}",
            json=patch_data,
            headers=headers
        )

        assert patch_response.status_code == 200, f"Expected 200, got {patch_response.status_code}"
        patched_data = patch_response.json()

        # Verify the patched fields were updated
        assert patched_data["firstname"] == "Newman", "Firstname was not updated"
        assert patched_data["totalprice"] == 200, "Total price was not updated"

        # Verify other fields remained unchanged
        assert patched_data["lastname"] == "User", "Lastname should remain unchanged"
        assert patched_data["depositpaid"] == True, "Depositpaid should remain unchanged"
