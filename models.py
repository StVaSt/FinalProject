from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from flask import session


# Cоздание экземпляра объекта SQLAlchemy
db = SQLAlchemy()

# Создание модели для таблицы users_hangman
class UsersHangman(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    count_win = db.Column(db.Integer, default=0)
    count_loss = db.Column(db.Integer, default=0)

# Создание модели для таблицы words_hangman
class WordsHangman(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(15), nullable=False)
    count_letter = db.Column(db.Integer, nullable=False)
    count_win = db.Column(db.Integer, default=0)
    count_loss = db.Column(db.Integer, default=0)
    description = db.Column(db.String(255), nullable=False)

# Создание модели для таблицы cookies_hangman
class CookiesHangman(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(15), ForeignKey('users_hangman.login'), nullable=False)
    cookie_value = db.Column(db.String(255), nullable=False)
    validity_period = db.Column(db.DateTime, nullable=False)

    user = relationship('UsersHangman', backref=db.backref('cookies', lazy=True))

class GameSessionData:
    def __init__(self):
        self.login = session.get('login', '')
        self.word = session.get('word', '')
        self.count_letter = session.get('count_letter', 0)
        self.description = session.get('description', '')
        self.count_win = session.get('count_win', 0)
        self.count_loss = session.get('count_loss', 0)
        self.image_num = session.get('image_num', '')
        self.try_win = session.get('try_win', 0)
        self.try_loss = session.get('try_loss', 0)
        self.empty_element = session.get('empty_element', '')
        self.used_letters = session.get('used_letters', [])

    def save(self):
        session['login'] = self.login
        session['word'] = self.word
        session['count_letter'] = self.count_letter
        session['description'] = self.description
        session['count_win'] = self.count_win
        session['count_loss'] = self.count_loss
        session['image_num'] = self.image_num
        session['try_win'] = self.try_win
        session['try_loss'] = self.try_loss
        session['empty_element'] = self.empty_element
        session['used_letters'] = self.used_letters

    def reset(self):
        self.word = ''
        self.count_letter = 0
        self.description = ''
        self.count_win = 0
        self.count_loss = 0
        self.image_num = ''
        self.try_win = 0
        self.try_loss = 0
        self.empty_element = ''
        self.used_letters = []
        self.save()