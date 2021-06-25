from flask import Flask

def create_app():
    app = Flask(__name__)

    import fluffy_http_app.controllers as control

    app.register_blueprint(control.module)

    return app