from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/anonymize', methods=['POST'])
def anonymize():
    data = request.json['data']
    anonymized_data = data[::-1]  # Simple anonymization by reversing the string
    return jsonify({'anonymized_data': anonymized_data})

if __name__ == '__main__':
    app.run(debug=True)