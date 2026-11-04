from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        service="User Service",
        status="running"
    )

@app.route("/users")
def users():
    return jsonify(
        users=[
            {"id": 1, "name": "Asha"},
            {"id": 2, "name": "Rahul"}
        ]
    )

if __name__ == "__main__":
    app.run(port=5001)
