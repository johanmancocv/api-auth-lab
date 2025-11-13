# Sportsbook Onboarding – API Integration & Authentication Diagnostic Lab

## Overview

This lab simulates a **common API integration issue** during a sportsbook onboarding process:  
- Authentication failures caused by **missing or invalid credentials**.

It demonstrates how **Johan**:
- Diagnoses and reproduces authentication errors (401/403).
- Coordinates with technical teams to configure proper credentials.
- Validates API connectivity after remediation.
- Documents the issue professionally (incident, RCA (Root Cause Analysis), resolution plan).

This lab simulates a sportsbook onboarding scenario similar to those managed in real life, but it uses generic mock APIs and authentication flows to remain vendor-neutral and compliant.

---

## Scenario

During the onboarding of a new sportsbook client (`BetNova`), all test calls to the API returned: **401 Unauthorized**

## Diagnosis (Reproducing the Issue)

**To confirm the authentication failure, Johan executed a diagnostic script to simulate an API request without credentials:**

python scripts/test_invalid_request.py

**Expected output:**
```
/fixtures -> 401 Unauthorized
/odds -> 401 Unauthorized
/settlements -> 401 Unauthorized
```
This reproduces the exact blocker the client would experience in a real sportsbook onboarding:
**No valid credentials → no access to event, odds, or settlement data.**

## Root Cause

After reviewing the integration environment, Johan identified that:

**The client did not have authentication credentials configured correctly
(missing token, missing client_id/client_secret, or misconfigured headers).**

Without proper credentials, the API gateway rejects any request with a 401 error.

This directly blocks:

- Data ingestion

- Odds updates

- Settlement processing

- UAT (User Acceptance Testing) test execution

**Remediation (Simulating the Fix)**

To simulate what would happen when credentials are finally configured, Johan generated mock credentials using:

python scripts/simulate_credentials_setup.py


This script creates a **credentials.json** file containing:

- client_id

- client_secret

- access_token

These represent a **correctly configured** sportsbook integration.

## Re-Test (Expected Response: 200 OK)

**With credentials in place, Johan re-tested the API calls:**

python scripts/test_valid_request.py


**Expected output:**

Status: 200 OK
Response snippet: [{"event_id": "EVT1001", "league": "Premier League", ...}]


This confirms that the onboarding blocker was resolved and the API now functions as expected.

## Results Summary
```
**Endpoint------Before Fix------After Fix**
/fixtures----------401------------200
/odds--------------401------------200
/settlements-------401------------200
```
A full summary is available in:
1. reports/test_results.md
2. reports/screenshots/

## Jira Documentation

As part of the PM workflow, Johan logged the issue and its lifecycle in Jira-style documentation.

Files included:
```
**File	---> Description**
jira_docs/incident_report.md	--->       What happened, context, impact
jira_docs/root_cause.md	        --->       Detailed RCA
jira_docs/resolution_plan.md	--->       Fix applied + preventive actions
```
**This mirrors a real onboarding incident process.**

## Learnings & PM Takeaways

This lab demonstrates Johan’s:

- Ability to diagnose API-level issues quickly

- Understanding of authentication flows

- Use of reproducible tests to confirm hypotheses

- Clear communication with engineering and clients

- Structured documentation for preventable issues

- Familiarity with common sportsbook onboarding blockers

These skills are essential for **Technical Project Management roles** in sports data integrations.

## Repository Structure

```bash
api-auth-lab/
│
├── README.md
│
├── scripts/
│   ├── mock_api_server.py
│   ├── mock_api_server_ReadMe.md
│   ├── simulate_credentials_setup.py
│   ├── simulate_credentials_setup_ReadMe.md
│   ├── test_invalid_request.py
│   ├── test_invalid_request_ReadMe.md
│   ├── test_valid_request.py
│   └── test_valid_request_ReadMe.md
│
├── jira_docs/
│   ├── Issue: ONB-102 incident_report.md
│   ├── Issue: ONB-103 root_cause.md
│   └── Issue: ONB-104 resolution_plan.md
│
├── sql/
│   ├── analysis_examples.sql
│   ├── FotoSQLmensaje.PNG
│   └── FotoSQLresultado.PNG
│
└── reports/
    ├── test_results.md
    └── screenshots/
```

## Tags

- sportsbook
- API 
- authentication 
- integration
- project-management
- jira
- SQL
- onboarding
- diagnostics

## How to Run This Lab

**1. Follow the steps below to reproduce the full onboarding simulation, from authentication failure (401) to successful API access (200).**

Install Dependencies
This lab requires Python 3, plus: 

```
pip install flask requests 
``` 
**2. Start the Mock API Server**

This server simulates a sportsbook API provider.

Run: 
``` 
python mock_api_server.py 
```

Expected: 
``` 
Running on http://127.0.0.1:5000 
```

Leave this terminal window open and running throughout the entire lab.

Endpoints provided: 
``` 
/unauthorized → returns 401

/fixtures → returns sample event data

/odds → returns sample odds

/settlements → returns sample settlement data 
``` 
**3. Reproduce the Authentication Failure (401)**

Open a new terminal window (do NOT stop the Flask server) and run: 
```
python scripts/test_invalid_request.py 
```

Expected output: 
``` 
Sending request to local 401 endpoint... Status Code: 401 Authentication failed: Invalid or missing API credentials. 
```

This represents the initial failing state of the onboarding.

Simulate Credential Setup
Next, simulate the step where the provider configures valid credentials: 
``` 
python scripts/simulate_credentials_setup.py
```

This generates:

- credentials.json
  
containing:

- client_id

- client_secret

- access_token

This represents the “fix” applied by the onboarding team.

**Validate Successful API Access (200 OK)
With credentials in place, test the real integration endpoints:** 
``` 
python scripts/test_valid_request.py 
```

Expected: 
``` 
/fixtures -> 200 /odds -> 200 /settlements -> 200 Authentication successful. API connectivity verified. 
```

This confirms that the onboarding blocker has been resolved.

**Execution Flow Summary Step Script Expected Result 1 mock_api_server.py Server running on localhost 2 test_invalid_request.py 401 Unauthorized 3 simulate_credentials_setup.py credentials.json created 4 test_valid_request.py 200 OK for all endpoints**


## Author

Johan Manco Cardona

**Technical Project Management | Sports Data | API Integrations**
