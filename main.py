from flask import Flask
from src import init_app

app: Flask = init_app()
app.run("127.0.0.1", 5000, debug=True)
