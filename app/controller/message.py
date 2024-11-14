from flask import Blueprint, jsonify, request
from pyexpat.errors import messages

from app.service.producer.producer import produce_message

message_blueprint = Blueprint('mission', __name__)


from flask import request

@message_blueprint.route('/', methods=['POST'])
def publish_message():
    # Get the JSON data from the request
    message = request.get_json()
    content = message.get('content')
    produce_message(message)

    return jsonify({"message": content}, 200)
