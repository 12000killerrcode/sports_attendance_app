from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login, app
from flask_login import UserMixin
from datetime import datetime
from hashlib import md5
import jwt
from time import time


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
    last_seen = db.Column(db.DateTime, default=datetime.now)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time() + expires_in},
            app.config['SECRET_KEY'],
            algorithm='HS256')

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id= jwt.decode(
                token,
                app.config['SECRET_KEY'],
                algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    
        


    def __repr__ (self):
        return f'User: {self.email}'

    # Password hashing
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(120), index=True)
    season = db.Column(db.String(120), index=True)
    wins = db.Column(db.String(120), index=True)
    losses = db.Column(db.String(120), index=True)
    draws = db.Column(db.String(120), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__ (self):
        return f'Performance: {self.season} {self.year}'    

class Target(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(120), index=True)
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__ (self):
        return f'Target: {self.body}'
    

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), index=True)
    lastname = db.Column(db.String(50), index=True)
    date_of_birth = db.Column(db.DateTime, index=True, default=datetime.now)
    attendance = db.Column(db. String(200), index=True)
    fitness = db.Column(db. Integer, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__ (self):
        return f'Player: {self.lastname}' 

class Coaching(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tactics = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
     
    def __repr__ (self):
        return f'Coaching: {self.tactics}'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__ (self):
        return f'Post: {self.body}'

    


