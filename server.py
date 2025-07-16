from flask import Flask, request, jsonify

app = Flask(__name__)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Render Webhook is up", 200

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print("Received TradingView alert:", data)
        return jsonify({"status": "received"}), 200
    return "Webhook is alive", 200

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render sets PORT environment variable
    app.run(host='0.0.0.0', port=port)