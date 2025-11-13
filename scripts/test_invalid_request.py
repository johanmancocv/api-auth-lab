import requests

API_BASE = "http://127.0.0.1:5000"   # Local Flask mock API
ENDPOINT = "/unauthorized"           # 401 endpoint

def test_invalid_auth():
    """
    Sends a request to the local unauthorized endpoint and validates
    that authentication fails as expected.
    """

    url = API_BASE + ENDPOINT

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



