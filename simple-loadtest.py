from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Random wait between requests (1 to 5 seconds)

    @task
    def load_homepage(self):
        self.client.get("/")

    @task(2)
    def load_search_page(self):
        self.client.get("/results?search_query=locust")
