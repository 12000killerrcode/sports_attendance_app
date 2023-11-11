from app import app
from flask import render_template
from app.forms import LoginForm, RegisterForm


@app.route("/")
@app.route("/index")
def index():
    """Index URL"""
    return render_template('index.html', title='Sports Management App')

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
    return render_template('player.html' , title='Player')


@app.route('/target')
def target():
    """target"""
    return render_template('target.html' , title='Target')


@app.route('/login')
def login():
    """login"""
    form = LoginForm()
    return render_template('login.html' , title='Login', form=form)


@app.route('/register')
def register():
    """register"""
    form = RegisterForm()
    return render_template('register.html' , title='Register', form=form)
