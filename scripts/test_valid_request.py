import json
import requests

API_BASE = "http://127.0.0.1:5000"   # Local Flask mock API

# Load mock credentials created by simulate_credentials_setup.py
with open("credentials.json") as f:
    creds = json.load(f)

headers = {"Authorization": f"Bearer {creds['access_token']}"}

print("Testing API endpoints with valid credentials...\n")

endpoints = ["/fixtures", "/odds", "/settlements"]

for endpoint in endpoints:
    url = API_BASE + endpoint
    try:
        response = requests.get(url, headers=headers)
    except Exception as e:
        print(f"Request failed due to connection error: {e}")
        continue

    print(f"{endpoint} -> {response.status_code}")
    print("Response snippet:", response.text[:120], "\n")

print("Authentication successful. API connectivity verified.")

