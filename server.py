from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print("Received TradingView alert:", data)
        # Handle alert logic here
        return jsonify({"status": "received"}), 200

    # Handle UptimeRobot ping
    return "Webhook is alive", 200

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render sets PORT environment variable
    app.run(host='0.0.0.0', port=port)