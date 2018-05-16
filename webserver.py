import json, requests, datetime
from flask import Flask, request

app = Flask(__name__)

# Networking
ROOT = 'http://raspberrypi.local';
BUZZER_ROOT = '192.XXX';

# Sensors
DOOR = 'door'

buzzer = {}

# Sends a POST request, returns JSON object
def post (url, body):
    response = requests.post(url, json=body);

    if response.status_code > 200:
        raise ValueError('Can\'t make request to ' + url);

    return json.loads(response.text);

# Routes

# Handles buzz request
@app.route('/buzz', methods=['POST'])
def buzz():
    sensor = request.args.get('sensor')
    state = request.args.get('state')

    if sensor is not None and state is not None:
        return 'Yo!';
    else:
        return 'Missing parameters!', 400


@app.errorhandler(404)
def page_not_found(error):
    return 'Not found!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
