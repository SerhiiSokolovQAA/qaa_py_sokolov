import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger("cars_test_logger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_search.log", mode="w")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


@pytest.fixture(scope="class")
def authenticated_session():
    session = requests.Session()
    auth_url = f"{BASE_URL}/auth"

    response = session.post(auth_url, auth=HTTPBasicAuth("test_user", "test_pass"))
    assert response.status_code == 200, "Auth failed"

    access_token = response.json().get("access_token")
    assert access_token, "No access token received"

    session.headers.update({"Authorization": f"Bearer {access_token}"})
    logger.info("Authentication successful. Token acquired.")

    return session

@pytest.mark.parametrize(
    "sort_by, limit",
    [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 7),
        ("brand", 10),
        ("price", 2),
        ("year", None),
        (None, 4),
    ]
)
class TestCarSearch:
    def test_search_cars(self, authenticated_session, sort_by, limit):
        params = {}
        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        response = authenticated_session.get(f"{BASE_URL}/cars", params=params)
        logger.info(f"Request with params={params}, status={response.status_code}")

        assert response.status_code == 200

        cars = response.json()
        assert isinstance(cars, list), "Response must be a list"
        if limit:
            assert len(cars) <= limit, f"Expected at most {limit} cars"

        logger.info(f"Received {len(cars)} cars. First item: {cars[0] if cars else 'EMPTY'}")
