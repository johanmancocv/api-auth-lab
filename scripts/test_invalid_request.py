import requests

def test_invalid_auth():
    """
    Sends a request to the local 401 test endpoint and validates
    that authentication fails as expected.
    """

    url = "http://127.0.0.1:5000/unauthorized"  # Local endpoint

    print("Sending request to local 401 endpoint...")
    try:
        response = requests.get(url)
    except Exception as e:
        print(f"Request failed due to connection error: {e}")
        return

    print(f"Status Code: {response.status_code}")

    if response.status_code == 401:
        print("Authentication failed: Invalid or missing API credentials.")
    else:
        print("Unexpected response:")
        print(response.text)

if __name__ == "__main__":
    test_invalid_auth()


