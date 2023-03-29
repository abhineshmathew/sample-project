from flask import blueprints

bp = blueprints.Blueprint(name='main',import_name=__name__, url_prefix='/')

from app.routes import auth, home

