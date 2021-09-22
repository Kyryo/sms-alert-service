from .utils import validate, send, lang
from werkzeug.datastructures import Headers
from . import app
from flask import request
import json


@app.route('/v1/sms/send', methods=['POST'])
def send_sms():
    #! [TODO] would be nice to check that the data coming in is really a JSON
    data = json.loads(request.data)

    validator = validate.Validate(data)

    if not validator.is_valid_phone_number():
        return json.dumps({"status": "error", "error": lang.error['invalid_phone']}), 400

    # * try to send the SMS
    params = {}
    send_obj = send.Send(params)

    # * check if the SMS was sent successfully
    if(send_obj.message()):

        # * return appropriate response
        #! [TODO] when sending through twilio API, the API returns sid for each successful call - you can change in utils/send.py for the method to return the sid instead of bool
        return json.dumps({"status": "success", "message": "your message was sent successfully"}), 200

    else:
        return json.dumps({"status": "error", "message": "your message failed to send"}), 400
