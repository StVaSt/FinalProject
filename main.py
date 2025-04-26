from flask import Flask, render_template
import functions
from models import db
import function_game
import json


app = Flask(__name__)

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Настройка подключения к базе данных
app.config['SQLALCHEMY_DATABASE_URI'] = config['database']['uri']

app.secret_key = config['secret']['key']

# Инициализация объекта db
db.init_app(app)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/new_users", methods=["POST"])
def new_users():
    return functions.new_users()

@app.route("/authorization")
def authorization():
    return render_template("authorization.html")

@app.route("/login_users", methods=["POST"])
def login_users():
    return functions.login_users()

@app.route("/rules")
def rules():
    return render_template("rules.html")


@app.route("/main_game")
def main_game():
    return functions.check_cookie("main_game")

@app.route("/add_word")
def add_word():
    return functions.check_cookie("add_word")

@app.route("/new_word", methods=["POST"])
def new_word():
    return functions.new_word()

@app.route("/statistics")
def statistics():
    return functions.check_cookie("statistics")

@app.route("/play")
def play():
    return functions.check_cookie("play")

@app.route("/guess", methods=["POST"])
def guess():
    return function_game.guess()


if __name__ == '__main__':
    app.run(debug=True)
