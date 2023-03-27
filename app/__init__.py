from flask import Flask

def create_app():
    app=Flask(__name__)
    @app.route('/api/status')
    def status():
        return {'status':'online'},200
    return app