from app.routes import bp
from app.controller.home import *


bp.add_url_rule('/', 'index', index, methods=['GET'])
