import requests

def test_invalid_auth():
    url = "http://127.0.0.1:5000/unauthorized"   # Local API, guaranteed to work

    print("Sending request to local 401 endpoint...")
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 401:
        print("Local 401 endpoint working perfectly.")
    else:
        print("Unexpected response:")
        print(response.text)

if __name__ == "__main__":
    test_invalid_auth()


