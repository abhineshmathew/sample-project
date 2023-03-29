import os

from config import Config
from flask import Flask, redirect, url_for
from app.routes import bp


def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(bp)
    
    @app.route('/api/status')
    def status():
        return {'status': 1},200
    
    return app