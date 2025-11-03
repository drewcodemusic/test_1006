import requests
import pytest
from src.config import BASE_URL


class TestAPIBenchmarks:
    """Benchmark tests for API performance."""

    def test_benchmark_get_booking(self, benchmark, created_booking):
        """Benchmark GET request for a single booking."""
        booking_id = created_booking["booking_id"]

        # benchmark will run this function multiple times to get accurate measurements
        result = benchmark(requests.get, f"{BASE_URL}/booking/{booking_id}")

        assert result.status_code == 200

    def test_benchmark_get_all_bookings(self, benchmark):
        """Benchmark GET request for all booking IDs."""

        result = benchmark(requests.get, f"{BASE_URL}/booking")

        assert result.status_code == 200

    def test_benchmark_post_booking(self, benchmark, sample_booking_data):
        """Benchmark POST request to create a booking."""
        headers = {"Content-Type": "application/json"}

        # For operations with multiple parameters, use lambda or a wrapper function
        result = benchmark(
            lambda: requests.post(
                f"{BASE_URL}/booking",
                json=sample_booking_data,
                headers=headers
            )
        )

        assert result.status_code == 200

    def test_benchmark_patch_booking(self, benchmark, created_booking):
        """Benchmark PATCH request to update a booking."""
        booking_id = created_booking["booking_id"]

        patch_data = {
            "firstname": "BenchmarkTest",
            "totalprice": 999
        }

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
        }

        result = benchmark(
            lambda: requests.patch(
                f"{BASE_URL}/booking/{booking_id}",
                json=patch_data,
                headers=headers
            )
        )

        assert result.status_code == 200

    def test_benchmark_full_workflow(self, benchmark, sample_booking_data):
        """Benchmark a complete workflow: create, get, update, get again."""

        def full_workflow():
            # Create booking
            headers = {"Content-Type": "application/json"}
            create_response = requests.post(
                f"{BASE_URL}/booking",
                json=sample_booking_data,
                headers=headers
            )
            booking_id = create_response.json()["bookingid"]

            # Get booking
            get_response = requests.get(f"{BASE_URL}/booking/{booking_id}")

            # Update booking
            patch_data = {"firstname": "Updated"}
            auth_headers = {
                "Content-Type": "application/json",
                "Accept": "application/json",
                "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
            }
            patch_response = requests.patch(
                f"{BASE_URL}/booking/{booking_id}",
                json=patch_data,
                headers=auth_headers
            )

            # Get booking again to verify
            final_response = requests.get(f"{BASE_URL}/booking/{booking_id}")

            return final_response

        result = benchmark(full_workflow)
        assert result.status_code == 200
