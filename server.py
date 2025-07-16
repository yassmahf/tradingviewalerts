from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received alert:", data)

    # Process the RSI alert and trigger trading logic here

    return jsonify({"status": "success"}), 200

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render sets PORT environment variable
    app.run(host='0.0.0.0', port=port)