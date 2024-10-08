from flask import Flask
from twilio.rest import Client

app = Flask(__name__)

@app.route('/trigger-call', methods=['GET', 'POST'])
def trigger_call():
    account_sid = 'AC2b8b1e42b650668cefb704c114dc10f8'
    auth_token = '5faf35997c18b6fe8803f00a31367fc8'
    client = Client(AC2b8b1e42b650668cefb704c114dc10f8,5faf35997c18b6fe8803f00a31367fc8)

    # List of numbers to call
    numbers_to_call = ['+918179685957']
    call_sids = []  # To store Call SIDs

    for number in numbers_to_call:
        call = client.calls.create(
                            twim='<Response><Say>"change Alert message here"</Say></Response>',
                            to=number,
                            from_='<twilio-number>'
                        )
        call_sids.append(call.sid)

    # Joining all the Call SIDs to return in response
    call_sids_str = ', 'join(call_sids)
    return f"Call initiated with SIDs: {call_sids_str}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
