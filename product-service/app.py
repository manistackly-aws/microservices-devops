from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        service="Product Service",
        status="running"
    )

@app.route("/products")
def products():
    return jsonify(
        products=[
            {"id": 101, "name": "Keyboard"},
            {"id": 102, "name": "Mouse"}
        ]
    )

if __name__ == "__main__":
    app.run(port=5002)
