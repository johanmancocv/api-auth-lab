import requests
import urllib3

# Disable warnings for unverified HTTPS
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def test_invalid_auth():
    url = "https://run.mocky.io/v3/3ec54759-3d40-4dbc-bd4b-9f39dbe55123"

    print("Sending request to forced 401 endpoint...")
    response = requests.get(url, verify=False)  # FIX

    print(f"Status Code: {response.status_code}")

    if response.status_code == 401:
        print("Authentication failed (expected).")
    else:
        print("Unexpected response:")
        print(response.text)

if __name__ == "__main__":
    test_invalid_auth()

