from flask import Flask, request, jsonify
from datetime import datetime
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

@app.before_request
def log_request_path():
    logging.info(f"Request path: {request.path}")

# Route 1: GET - Returns the current date
@app.route('/date', methods=['GET'])
def get_date():
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return jsonify({"date": current_date})

# Route 2: POST - Responds with "stored"
@app.route('/store', methods=['POST'])
def store_data():
    data = request.json  # Assuming JSON data is sent in the request body
    # print(f"Data received: {data}")  # Optional: Log the data to the console
    return jsonify({"message": f"Data received and stored: {data}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)