import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1

    print("\nUser Name:", data["name"])
    print("Email:", data["email"])
