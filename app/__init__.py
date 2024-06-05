from flask import Flask

app = Flask(__name__)

from .views import main as main_blueprint

app.register_blueprint(main_blueprint)

def create_app():

    return app