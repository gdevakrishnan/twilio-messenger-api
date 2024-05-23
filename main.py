from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

app = Flask(__name__)


@app.route('/')
def home():
    return "Twilio Messenger API using Flask"

@app.route('/send_sms', methods=['POST'])
def send_sms():
    from_number = '[twilio mobile number]'
    data = request.json
    to_number = data.get('to')
    body = data.get('body')

    if not from_number or not to_number or not body:
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        account_sid = '##################################'
        auth_token = '[auth_token]'

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_=from_number,
            body=body,
            to=to_number
        )
        return jsonify({'message_sid': message.sid}), 200
    except TwilioRestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
