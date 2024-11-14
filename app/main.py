
from controller.message import message_blueprint
from flask import Flask

app = Flask(__name__)

app.register_blueprint(message_blueprint, url_prefix="/api/email")

if __name__ == "__main__":

    app.run(debug=True)
