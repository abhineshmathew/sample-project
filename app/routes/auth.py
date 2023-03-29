from app.routes import bp
from app.controller.auth import *


bp.add_url_rule('/oauth', 'login', login, methods=['GET'])
bp.add_url_rule('/oauth/callback', 'callback', callback, methods=['GET'])
bp.add_url_rule('/logout', 'logout', logout, methods=['GET'])

