import os
from flask import Flask
import py_eureka_client.eureka_client as eureka_client

from config import Config
from app.extensions import db

port = int(os.environ.get('PORT', 8056))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    eureka_client.init(eureka_server="http://localhost:8761/eureka",
    app_name="scoring-service-py",
    instance_port=port)

    # Register blueprints here
    from app.api import bp
    app.register_blueprint(bp)
    # Register error handlers here

    return app