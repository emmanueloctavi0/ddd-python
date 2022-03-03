from flask import Flask
from apps.http.blueprints import users

app = Flask(__name__)

app.register_blueprint(users.bp)


@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"
