# Root Cause Analysis — Missing Credentials

Issue: ONB-103  
Root Cause: Client had no valid credentials configured.
Contributing Factors:
- No access token
- No authentication header
Evidence: test_invalid_request.py output (401)
