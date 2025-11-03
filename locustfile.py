from locust import HttpUser, task

'''
class TestRestfulBooker(HttpUser):
    @task
    def get_all_bookings(self):
        self.client.get("/booking")
'''

class TestMockServer(HttpUser):
    @task
    def list_users(self):
        self.client.get("/api/users")