from flask import Flask
from config import config
from extensions import (
    ma, fbcrypt, db
)

# app factory
def create_app(config_name):
    app = Flask(__name__)

    # app config
    app.config.from_object(config[config_name])

    db.init_app(app)
    ma.init_app(app)
    fbcrypt.init_app(app)

    # register blueprints
    from .doctor import doc

    app.register_blueprint(doc, url_prefix="/doctor")

    return app
