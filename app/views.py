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

    #! [TODO] try to send the SMS
    #! [TODO] check if the SMS was sent successfully
    #! [TODO] return appropriate response
    return json.dumps({"status": "success", "message": "your message was sent successfully"}), 200
