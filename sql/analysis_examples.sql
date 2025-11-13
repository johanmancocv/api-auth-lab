##1. Detect missing settlements
-- Events that have already started but have no settlement record

SELECT f.event_id, f.start_time
FROM fixtures f
LEFT JOIN settlements s ON f.event_id = s.event_id
WHERE f.start_time < NOW() - INTERVAL '2 hours'
  AND s.event_id IS NULL;


-- 2. Reconcile bets vs settlements for a given event
-- Useful for auditing payouts or detecting discrepancies

SELECT b.event_id,
       COUNT(*) AS total_bets,
       SUM(b.stake) AS total_stake,
       SUM(s.payout) AS total_payout
FROM bets b
JOIN settlements s ON b.event_id = s.event_id
WHERE b.event_id = 'EVT1001'
GROUP BY b.event_id;


-- 3. Check for duplicated odds entries
-- (A common issue in streaming or polling integrations)

SELECT event_id, market, COUNT(*) AS duplicates
FROM odds
GROUP BY event_id, market
HAVING COUNT(*) > 1;


-- 4. Log of failed API calls (authentication or connectivity issues)

SELECT timestamp, endpoint, status_code, error_message
FROM api_error_log
WHERE status_code IN (401, 403, 500)
ORDER BY timestamp DESC;


-- 5. Validate odds timing vs fixtures timing
-- Detect odds delivered before fixture created (inconsistent data)

SELECT o.event_id, o.timestamp AS odds_time, f.created_at AS fixture_time
FROM odds o
JOIN fixtures f ON o.event_id = f.event_id
WHERE o.timestamp < f.created_at;
