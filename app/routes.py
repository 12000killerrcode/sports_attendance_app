from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegisterForm, PlayerForm
from app.models import User, Performance, Target , Player
from flask_login import current_user, login_user, logout_user, login_required


@app.route("/")
@app.route("/index")
def index():
    """Index URL"""
    if current_user.is_authenticated:
        return redirect(url_for('coaching'))
    return render_template('index.html', title='Sports Management App')

@app.route('/coaching')
@login_required
def coaching():
    """Coaching"""
    return render_template('coaching.html' , title='Coaching')


@app.route('/performance')
@login_required
def performance():
    """performance"""
    return render_template('performance.html' , title='Performance')


@app.route('/player', methods=['GET', 'POST'])
@login_required
def player():
    """player"""
    form = PlayerForm()
    if form.validate_on_submit():
        player = Player(
            firstname = form.firstname.data,
            lastname = form.lastname.data,
            date_of_birth= form.date_of_birth.data,
            attendance = form.attendance.data,
            fitness = form.fitness.data,
            author=current_user 
            )
        db.session.add(player)
        db.session.commit()
        flash('Added Player')
        return redirect(url_for('player'))
    players = Player.query.all()        
    return render_template('player.html' , title='Player', form = form, players = players)


@app.route('/delete-player/<int:id>')
@login_required
def delete_player(id):
    player = Player.query.filter_by(id = id).first()
    db.session.delete(player)
    db.session.commit()
    flash('Player has been deleted succesfully')
    return redirect(url_for('player'))


@app.route('/target')
@login_required
def target():
    """target"""
    return render_template('target.html' , title='Target')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """login"""
    if current_user.is_authenticated:
        return redirect(url_for('coaching'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect (url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Welcome {form.email.data}')
        return redirect(url_for('index'))
    return render_template('login.html' , title='Login', form=form)


@app.route('/logout')
@login_required
def logout():
    """Logout a user"""
    logout_user()
    return redirect(url_for('login'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register"""
    if current_user.is_authenticated:
        return redirect(url_for('coaching'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have been registered successfuly. Login to continue')
        return redirect(url_for('login'))
    return render_template('register.html' , title='Register', form=form)
