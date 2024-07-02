#!/usr/bin/python3
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    endpoint = {}
    endpoint["client_ip"] = request.remote_addr
    visitor_name = request.args.get('visitor_name', 'Guest')
    endpoint["greeting"] = (f"Hello, {visitor_name}!, the temperature is 11" +
                           " degrees Celcius in New York")
    try:
        response = requests.get(f'https://ipinfo.io/{endpoint["client_ip"]}/city?token=$TOKEN')
        response.raise_for_status()
       # data = response.json()
        #endpoint["city"] = data.get("city", "Unknown")
        endpoint["city"] = response
    except requests.RequestException:
        endpoint["city"] = "Unknown"
    return jsonify(endpoint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

