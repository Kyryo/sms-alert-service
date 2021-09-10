from werkzeug.datastructures import Headers
from . import app
from flask import request
from app.utils import sms as SMS, lang
import json
import logging
logging.basicConfig(filename='error.log', level=logging.DEBUG)


@app.route('/', methods=['POST'])
def receive_sms():

    params = {
        "api_key": "6ec4fbee-3dc3-4fa1-9b75-e44d3d78fe06",
        "message": "data received from some_app: some_body ",
        "recipient": "+265998006237"
    }

    url = "https://sms.angledimension.com/api/Messages/SendMessageRapid"

    params = {
        "message": "Hello there!",
        "recipients": ["+265998006237"],
        "source": "2479",
        "sender": "2479",
        "transactionReference": "123456"
    }

    headers = {'Content-type': 'application/json; charset=utf-8'}

    SMS.Send(url=url, params=params, headers=headers)

    return json.dumps({"status": "success"}), 200


@app.route('/v1/sms/send', methods=['POST'])
def send_sms():
    """sends an SMS as defined by specific payload

    Returns:
        json: request status, status can be error if SMS was not sent or success if SMS is sent successfully
    """

    # * DATA FROM REQUEST
    # * DECODE DATA COMING IN

    # * define empty dict to hold data from request
    data = {}

    # * attempt to get data, raise an exception if data has errors/ format issues
    try:
        data = json.loads(request.data)

    #! [TODO] handle the exception better
    except:
        return json.dumps({"status": "error", "error": lang.error['json_decode_error']}), 400

    # * VALIDATIONS
    # * CHECK API KEY, REQUIRED JSON KEYS, PHONE NUMBER VALIDITY
    #! [TODO] move validations to utils

    # * validate data coming from request/json to have required keys
    if not SMS.Validate.check_keys(data):
        return json.dumps({"status": "error", "error": lang.error['data_format']}), 400

    if not SMS.Validate.validate_api_key(data):
        return json.dumps({"status": "error", "error": lang.error['authorization_error']}), 400

    # * validate if phone number is valid
    if not SMS.Validate.is_valid_phone_number(data):
        return json.dumps({"status": "error", "error": lang.error['invalid_phone']}), 400

    # * SEND SMS
    # * SETUP PARAMS, SEND SMS, SEND RESPONSE

    url = "https://sms.angledimension.com/api/Messages/SendMessageRapid"

    params = {
        "message": data["message"],
        "recipients": ["" + data['recipient'] + ""],
        "source": "2479",
        "sender": "2479",
        "transactionReference": "123456"
    }

    headers = {'Content-type': 'application/json; charset=utf-8'}

    send_obj = SMS.Send(url=url, params=params, headers=headers)

    # * check if SMS was successfully sent
    if send_obj.message() is True:

        return json.dumps({"status": "success", "message": "your message was sent successfully"}), 200

    # * respond accordingly once SMS is not sent
    else:

        return json.dumps({"status": "error", "error": lang.error['general']}), 500
