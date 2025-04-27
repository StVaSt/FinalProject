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
        self.data_strings = ["login", "word", "description", "image_num", "empty_element"]
        for i in self.data_strings:
            setattr(self, i, session.get(i, ''))
        self.data_ints = ["count_letter","count_win", "count_loss","try_win", "try_loss"]
        for j in self.data_ints:
            setattr(self, j, session.get(j, 0))
        self.data_lists = ["used_letters"]
        for k in self.data_lists:
            setattr(self, k, session.get(k, []))

    def save(self):
        for i in self.data_strings + self.data_ints + self.data_lists:
            session[i] = getattr(self, i)

    def reset(self):
        for i in self.data_strings:
            setattr(self, i, '')
        for j in self.data_ints:
            setattr(self, j, 0)
        for k in self.data_lists:
            setattr(self, k, [])
        self.save()