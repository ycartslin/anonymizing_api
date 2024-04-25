from flask import Flask, request, jsonify
from api_client import LLMClient

app = Flask(__name__)
client = LLMClient(api_key="your-api-key")

@app.route("/query", methods=["POST"])
def query():
    data = request.json
    response = client.query(model="text-davinci-003", prompt=data["prompt"])
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)