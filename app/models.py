from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login
from flask_login import UserMixin
from datetime import datetime


@login.user_loader
def login_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    performances = db.relationship('Performance', backref='author', lazy='dynamic')
    targets = db.relationship('Target', backref='author', lazy='dynamic')
    players = db.relationship('Player', backref='author', lazy='dynamic')
    coaching = db.relationship('Coaching', backref='author', lazy='dynamic')



    def __repr__ (self):
        return f'User: {self.email}'

    # Password hashing
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(120), index=True)
    season = db.Column(db.String(120), index=True)
    wins = db.Column(db.String(120), index=True)
    losses = db.Column(db.String(120), index=True)
    draws = db.Column(db.String(120), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Target(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(120), index=True)
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), index=True)
    lastname = db.Column(db.String(50), index=True)
    date_of_birth = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    attendance = db.Column(db. String(200), index=True)
    fitness = db.Column(db. Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Coaching(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tactics = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    


