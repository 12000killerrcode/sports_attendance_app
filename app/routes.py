from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/coaching')
def coaching():
    """Coaching"""
    return render_template('coaching.html' , title='Coaching')
@app.route('/performance')
def performance():
    """performance"""
    return render_template('performance.html' , title='Performance')
@app.route('/player')
def player():
    """player"""
    return render_template('player.html' , title='player')
@app.route('/target')
def target():
    """target"""
    return render_template('target.html' , title='target')
@app.route('/login')
def login():
    """login"""
    return render_template('login.html' , title='login')
@app.route('/register')
def register():
    """register"""
    return render_template('register.html' , title='register')

