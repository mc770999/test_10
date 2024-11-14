from flask import Blueprint, jsonify, request
from pyexpat.errors import messages

from app.psql.repository.explosive_repository import get_all_message_explodes
from app.psql.repository.hostage_repository import get_all_message_hostages
from app.psql.repository.person_repository import get_person_by_email
from app.service.producer.producer import produce_message
from app.utils.most_common_word import most_common_word

message_blueprint = Blueprint('mission', __name__)


from flask import request

@message_blueprint.route('/', methods=['POST'])
def publish_message():
    # Get the JSON data from the request
    message = request.get_json()
    content = message.get('content')
    produce_message(message)

    return jsonify({"message": content}, 200)

@message_blueprint.route('/', methods=['GET'])
def get_person():
    # Get the JSON data from the request
    message = request.get_json()
    print(message["email"])
    content = get_person_by_email(message["email"])

    return jsonify(content, 200)
@message_blueprint.route('/most_common_word', methods=['GET'])
def get_most_common_word():
    list1 = get_all_message_explodes()
    list2 =  get_all_message_hostages()
    word = most_common_word(list1, list2)

    return jsonify({"word" : word}, 200)
