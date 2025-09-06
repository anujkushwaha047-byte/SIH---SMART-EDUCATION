from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Welcome to Smart Education API 🚀"})

if __name__ == "__main__":
    app.run(debug=True)
