import logging
import os
from flask import Flask

app = Flask(__name__)

# Ensure logs directory exists
log_directory = "logs/flask"
os.makedirs(log_directory, exist_ok=True)

# Configure logging
logging.basicConfig(filename=os.path.join(log_directory, "app.log"), level=logging.INFO)

@app.route('/')
def home():
    app.logger.info("Home route accessed")
    return "Hello, DevOps with Flask!"

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
