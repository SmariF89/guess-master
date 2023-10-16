from flask import Flask

def init_app() -> Flask:
    app = Flask(__name__)

    with app.app_context():
        import src.app
        return app
