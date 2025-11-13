from flask import Flask, jsonify

app = Flask(__name__)

# Simulates the API returning 401 (invalid credentials)
@app.route("/unauthorized")
def unauthorized():
    return jsonify({"error": "Unauthorized access"}), 401

# Simulates the API returning 200 (valid credentials)
@app.route("/fixtures")
def fixtures():
    data = [
        {"event_id": "EVT1001", "league": "Premier League", "home": "Liverpool", "away": "Chelsea"}
    ]
    return jsonify(data), 200

@app.route("/odds")
def odds():
    data = [
        {"event_id": "EVT1001", "market": "1X2", "selection": "Liverpool", "odds": 1.85}
    ]
    return jsonify(data), 200

@app.route("/settlements")
def settlements():
    data = [
        {"event_id": "EVT1001", "result": "home", "payout": 1.85}
    ]
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(port=5000)
