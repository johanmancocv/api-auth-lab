**API Authentication Lab – Test Results**

This document summarizes the results of running the full sportsbook onboarding authentication simulation, including API failures, credential setup, and successful authentication validation.

**1. Environment Setup**

Local Mock API Server:
```
http://127.0.0.1:5000
```
Python Version:
```
3.x
```
Libraries Used:

- Flask

- Requests

Scripts Executed:
```
mock_api_server.py

test_invalid_request.py

simulate_credentials_setup.py

test_valid_request.py
```
**2. Test 1 — Invalid Authentication (Expected 401)**

Command:
```
python scripts/test_invalid_request.py
```

Endpoint tested:
```
/unauthorized
```

Result:
```
Sending request to local 401 endpoint...
Status Code: 401
Authentication failed: Invalid or missing API credentials.
```

Status:
Authentication failed as expected (correct behavior)

**This confirms that the client was unable to access the API due to missing or invalid credentials.**

**3. Test 2 — Credential Setup Simulation**

Command:
```
python scripts/simulate_credentials_setup.py
```

Result:
```
Simulating credential setup for sportsbook client...
Client credentials created successfully!
File generated: credentials.json
```

Generated File:
```
credentials.json
```

Contents Created:

- client_id

- client_secret

- access_token

- issued_at timestamp

Status:
```
Credentials generated successfully
```

This simulates the provider enabling valid API access for the client.

**4. Test 3 — Valid Authentication (Expected 200)**

Command:
```
python scripts/test_valid_request.py
```

Endpoints tested:
```
/fixtures

/odds

/settlements
```
Results:
```
/fixtures -> 200
Response snippet: [{"event_id": "EVT1001", "league": "Premier League", ...}]

/odds -> 200
Response snippet: [{"event_id": "EVT1001", "market": "1X2", "odds": 1.85, ...}]

/settlements -> 200
Response snippet: [{"event_id": "EVT1001", "result": "home", ...}]
```

Status:

- Authentication successful
- All endpoints returned 200 OK
- Data retrieval validated

This confirms that the onboarding issue was resolved and the API is functioning correctly with valid credentials.

**5. Summary of Test Outcomes**

Step	Script	Expected	Result
```
Initial failure	test_invalid_request.py	401	401 ✔
Credential setup	simulate_credentials_setup.py	credentials.json	Created ✔
Valid data access	test_valid_request.py	200	200 ✔
```
**6. Conclusion**

All test scenarios behaved exactly as expected:
```
The API initially rejected unauthorized calls (401)

Credential setup was completed successfully

The client then accessed all main endpoints with valid authentication (200)
```
**This confirms the full onboarding flow:**

**Failure → Fix → Validation**

The lab accurately simulates a real-world sportsbook API integration issue and its resolution.
