from ast import For
from datetime import datetime
from enum import unique

from sqlalchemy import ForeignKey

from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(250))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    pokemon = db.relationship('Pokemon', backref='owner', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_id = db.Column(db.Integer, unique=True)
    name = db.Column(db.String(50))
    type = db.Column(db.String(50))
    description = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
