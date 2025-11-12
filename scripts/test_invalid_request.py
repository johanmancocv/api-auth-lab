import requests

def test_invalid_auth():
    """
    Always returns 401 Unauthorized for testing.
    """

    url = "https://run.mocky.io/v3/3ec54759-3d40-4dbc-bd4b-9f39dbe55123"

    print("Sending request to forced 401 endpoint...")
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 401:
        print("Authentication failed (expected).")
        print("Working 401 test endpoint confirmed.")
    else:
        print("Unexpected response:")
        print(response.text)


if __name__ == "__main__":
    test_invalid_auth()

