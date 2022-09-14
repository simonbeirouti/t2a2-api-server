from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

db = SQLAlchemy() # Database object
ma = Marshmallow() # Marshmallow object
bc = Bcrypt() # Bcrypt object

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.app_config')

    db.init_app(app)
    ma.init_app(app)
    bc.init_app(app)

    from commands import db_cmd
    app.register_blueprint(db_cmd)

    return app