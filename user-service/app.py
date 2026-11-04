from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        service="User Service",
        status="running"
    )

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

@app.route("/users")
def users():
    return jsonify(
        users=[
            {"id": 1, "name": "Asha"},
            {"id": 2, "name": "Rahul"}
        ]
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
