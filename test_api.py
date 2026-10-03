import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_user():

    response = requests.get(
        f"{BASE_URL}/users/1"
    )

    # 1. Validate status code
    assert response.status_code == 200

    # 2. Validate response type
    assert "application/json" in response.headers["Content-Type"]

    # Convert JSON response into Python dictionary
    data = response.json()

    # 3. Validate JSON structure
    assert isinstance(data, dict)

    # 4. Validate required keys
    assert "id" in data
    assert "name" in data
    assert "email" in data

    # 5. Validate expected value
    assert data["id"] == 1

    # 6. Validate data types
    assert isinstance(data["id"], int)
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)

    # 7. Basic email validation
    assert "@" in data["email"]

    print("\nGET USER")
    print("User ID:", data["id"])
    print("User Name:", data["name"])
    print("Email:", data["email"])


def test_create_post():

    payload = {
        "title": "Python Automation",
        "body": "Learning REST API testing using Pytest",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == "Python Automation"
    assert data["userId"] == 1

    print("\nPOST RESPONSE")
    print(data)


def test_update_post():

    payload = {
        "id": 1,
        "title": "Updated Python Automation",
        "body": "Updated using PUT request",
        "userId": 1
    }

    response = requests.put(
        f"{BASE_URL}/posts/1",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Updated Python Automation"

    print("\nPUT RESPONSE")
    print(data)


def test_delete_post():

    response = requests.delete(
        f"{BASE_URL}/posts/1"
    )

    assert response.status_code == 200

    print("\nDELETE RESPONSE")
    print("Status Code:", response.status_code)

def test_get_invalid_user():

    response = requests.get(
        f"{BASE_URL}/users/9999"
    )

    assert response.status_code == 404

    print("\nNEGATIVE TEST")
    print("Invalid User Status Code:", response.status_code)
