import requests

def test_invalid_auth():
    """
    Simulates an invalid authentication request to an API
    that always returns 401 Unauthorized.
    """

    url = "https://httpstat.us/401"   # Always returns 401

    headers = {
        "Authorization": "Bearer INVALID_TOKEN"
    }

    print("Sending request to forced-401 endpoint...")
    response = requests.get(url, headers=headers)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 401:
        print("Authentication failed: This endpoint always returns 401.")
        print("Useful for testing onboarding error handling and logging.")
    else:
        print("Unexpected response:")
        print(response.text)


if __name__ == "__main__":
    test_invalid_auth()
