from flask import current_app

@current_app.route("/hi", methods=["GET"])
def hello_world():
    return "hello world", 200
