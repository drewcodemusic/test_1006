import requests

BASE_URL = "https://restful-booker.herokuapp.com"


def test_create_booking_valid_data():
    print("Testing POST booking with valid data...")

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

    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert "bookingid" in data, "Missing bookingid"
    assert "booking" in data, "Missing booking data"
    assert data["booking"]["firstname"] == "Jim", "Firstname mismatch"
    assert data["booking"]["lastname"] == "Brown", "Lastname mismatch"
    print("✓ Test passed!")

def test_create_booking_missing_firstname():
    print("Testing POST booking with missing firstname...")

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

    print(f"Status Code: {response.status_code}")

    assert response.status_code == 500, f"Expected 500, got {response.status_code}"
    print("✓ Test passed!")

if __name__ == "__main__":
    print("Running POST booking tests...\n")

    test_create_booking_valid_data()
    print()

    test_create_booking_missing_firstname()
    print()

    print("All POST booking tests completed!")