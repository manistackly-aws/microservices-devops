from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        service="Order Service",
        status="running"
    )

@app.route("/orders")
def orders():
    return jsonify(
        orders=[
            {"id": 1001, "user_id": 1},
            {"id": 1002, "user_id": 2}
        ]
    )

if __name__ == "__main__":
    app.run(port=5003)
