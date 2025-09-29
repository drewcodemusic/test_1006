import requests

BASE_URL = "https://restful-booker.herokuapp.com"


def test_get_booking_valid_id():
    print("Testing GET booking with valid ID...")
    response = requests.get(f"{BASE_URL}/booking/3458")

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "firstname" in data, "Missing firstname"
    assert "lastname" in data, "Missing lastname"
    assert "depositpaid" in data, "Missing depositpaid"
    assert "totalprice" in data, "Missing totalprice"
    assert "bookingdates" in data, "Missing bookingdates"
    print("✓ Test passed!")

if __name__ == "__main__":
    print("Running GET booking tests...\n")

    test_get_booking_valid_id()
    print()

    print("All GET booking tests completed!")