import json
import time

print("Simulating credential setup for sportsbook client...")

# Mock client credentials (simulating what would happen once the API provider configures them)
credentials = {
    "client_id": "client_abc123",
    "client_secret": "secret_xyz456",
    "access_token": "mock_valid_token_789",
    "issued_at": time.strftime("%Y-%m-%d %H:%M:%S")
}

# Save mock credentials to file
with open("credentials.json", "w") as f:
    json.dump(credentials, f, indent=2)

print("Client credentials created successfully!")
print("File generated: credentials.json")

