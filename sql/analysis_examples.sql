/* ==========================================================
   00 — Drop tables if they already exist
   ========================================================== */

DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS settlements;
DROP TABLE IF EXISTS odds;
DROP TABLE IF EXISTS bets;
DROP TABLE IF EXISTS api_error_log;
GO

/* ==========================================================
   01 — Create mock sportsbook tables
   ========================================================== */

CREATE TABLE fixtures (
    event_id VARCHAR(20),
    league VARCHAR(100),
    start_time DATETIME,
    created_at DATETIME
);

CREATE TABLE settlements (
    event_id VARCHAR(20),
    result VARCHAR(50),
    payout DECIMAL(10,2)
);

CREATE TABLE odds (
    event_id VARCHAR(20),
    market VARCHAR(50),
    selection VARCHAR(100),
    odds DECIMAL(5,2),
    timestamp DATETIME
);

CREATE TABLE bets (
    event_id VARCHAR(20),
    stake DECIMAL(10,2),
    payout DECIMAL(10,2)
);

CREATE TABLE api_error_log (
    timestamp DATETIME,
    endpoint VARCHAR(200),
    status_code INT,
    error_message VARCHAR(500)
);


/* ==========================================================
   02 — Insert sample data
   ========================================================== */

-- Fixtures (one with a settlement, one missing)
INSERT INTO fixtures VALUES
('EVT1001', 'Premier League', DATEADD(HOUR, -3, GETDATE()), DATEADD(HOUR, -4, GETDATE())),
('EVT1002', 'La Liga', DATEADD(HOUR, -5, GETDATE()), DATEADD(HOUR, -6, GETDATE()));

-- Settlement for only one event
INSERT INTO settlements VALUES
('EVT1001', 'home', 185.00);

-- Odds (including a duplicate entry)
INSERT INTO odds VALUES
('EVT1001', '1X2', 'Liverpool', 1.85, DATEADD(HOUR, -2, GETDATE())),
('EVT1001', '1X2', 'Liverpool', 1.85, DATEADD(HOUR, -2, GETDATE()));  -- duplicate record

-- Bets
INSERT INTO bets VALUES
('EVT1001', 100, 185);

-- Mock API error log entries
INSERT INTO api_error_log VALUES
(GETDATE(), '/unauthorized', 401, 'Invalid token'),
(GETDATE(), '/fixtures', 500, 'Internal server error');


/* ==========================================================
   03 — Detect missing settlements
   ========================================================== */

PRINT '--- Missing Settlements (Events that started >2h ago with no settlement) ---';

SELECT f.event_id, f.start_time
FROM fixtures f
LEFT JOIN settlements s ON f.event_id = s.event_id
WHERE f.start_time < DATEADD(HOUR, -2, GETDATE())
  AND s.event_id IS NULL;



/* ==========================================================
   04 — Reconcile bets vs settlements
   ========================================================== */

PRINT '--- Reconciliation Results (bets vs settlements) ---';

SELECT 
    b.event_id,
    COUNT(*) AS total_bets,
    SUM(b.stake) AS total_stake,
    SUM(s.payout) AS total_payout
FROM bets b
JOIN settlements s ON b.event_id = s.event_id
WHERE b.event_id = 'EVT1001'
GROUP BY b.event_id;



/* ==========================================================
   05 — Detect duplicate odds entries
   ========================================================== */

PRINT '--- Duplicate Odds Detected (events with duplicates) ---';

SELECT event_id, market, COUNT(*) AS duplicates
FROM odds
GROUP BY event_id, market
HAVING COUNT(*) > 1;



/* ==========================================================
   06 — Show failed API calls
   ========================================================== */

PRINT '--- API Error Log (401/403/500 errors) ---';

SELECT timestamp, endpoint, status_code, error_message
FROM api_error_log
WHERE status_code IN (401, 403, 500)
ORDER BY timestamp DESC;



/* ==========================================================
   07 — Validate timing consistency (odds vs fixtures)
   ========================================================== */

PRINT '--- Timing Check (odds received before fixture created) ---';

SELECT 
    o.event_id, 
    o.timestamp AS odds_time, 
    f.created_at AS fixture_time
FROM odds o
JOIN fixtures f ON o.event_id = f.event_id
WHERE o.timestamp < f.created_at;


