# Incident Report — Authentication Failure (401)

Issue: ONB-102  
Summary: Initial API calls returned 401 Unauthorized during sportsbook onboarding.  
Impact: Client unable to retrieve fixtures, odds, settlements.  
Reproduction Steps:
1. Run mock_api_server.py
2. Execute test_invalid_request.py
3. Observe 401 response
Expected: 200 after authentication
Actual: 401 Unauthorized


