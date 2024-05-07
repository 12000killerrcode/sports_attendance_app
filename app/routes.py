from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegisterForm, PlayerForm, PerformanceForm, TargetForm, EditProfileForm, PostForm, \
    ResetPasswordRequestForm, ResetPasswordForm
from app.models import User, Performance, Target , Player, Post
from flask_login import current_user, login_user, logout_user, login_required, current_user 
from app.email import send_password_reset_email
from datetime import datetime

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.now()
        db.session.commit()


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    """Reset password URL"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template(
        'reset_password.html',
        title='Reset Password',
        form=form)

@app.route('/request_password_reset', methods=['GET', 'POST'])
def request_password_reset():
    """Request password reset URL"""
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('check your email  for the instruction to reset your password. ASANTE!,THANKYOU!')
        return redirect(url_for('login'))
    return render_template(
        'request_password_reset.html',
        title='Request Password Reset',
        form=form)    



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


@app.route('/performance', methods=['GET', 'POST'])
@login_required
def performance():
    """performance"""
    form = PerformanceForm()
    if form.validate_on_submit():
        performance = Performance(
            year = form.year.data,
            season = form.season.data,
            wins = form.wins.data,
            losses = form.losses.data,
            draws = form.draws.data,
            author=current_user 
            )
        db.session.add(performance)
        db.session.commit()
        flash('Added performance record')
        return redirect(url_for('performance'))
    performances = Performance.query.all()        
    return render_template('performance.html' , title='Performance', form = form, performances = performances)


@app.route('/delete-performance/<int:id>')
@login_required
def delete_performance(id):
    performance = Performance.query.filter_by(id = id).first()
    db.session.delete(performance)
    db.session.commit()
    flash('Performance has been deleted succesfully')
    return redirect(url_for('performance'))




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


@app.route('/target', methods=['GET', 'POST'])
@login_required
def target():
    """target"""
    form = TargetForm()
    if form.validate_on_submit():
        target = Target(
            year = form.year.data,
            body = form.body.data,
            author=current_user 
            )
        db.session.add(target)
        db.session.commit()
        flash('Added Target')
        return redirect(url_for('target'))
    targets = Target.query.all()        
    return render_template('target.html' , title='target', form = form, targets = targets)


@app.route('/delete-target/<int:id>')
@login_required
def delete_target(id):
    target = Target.query.filter_by(id = id).first()
    db.session.delete(target)
    db.session.commit()
    flash('Target has been deleted succesfully')
    return redirect(url_for('target'))



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


@app.route('/<email>/profile')
@login_required
def profile(email):
    """Profile page"""
    user = User.query.filter_by(email=email).first_or_404()
    return render_template(
        'profile.html',
        title='Profile',
        user=user)


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.email)
    if form.validate_on_submit():
        current_user.email = form.email.data
        db.session.commit()
        flash('Your changes have been saved')
        return redirect (url_for('profile', email=current_user.email))
    elif request.method == 'GET':
        form.email.data = current_user.email
    return render_template(
        'edit_profile.html',
        title='Edit Profile',
        form=form
    )    


@app.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    """post"""
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            body = form.body.data,
            author=current_user 
            )
        db.session.add(post)
        db.session.commit()
        flash('Posted')
        return redirect(url_for('chat'))
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page=page,
        per_page=app.config['POSTS_PER_PAGE'],
        error_out=False)
    next_url = url_for('chat', email=current_user.email, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('chat', email= current_user.email, page=posts.prev_num) \
        if posts.has_prev else None
    return render_template(
        'chat.html' , 
        title='Chat', 
        form = form, 
        posts = posts.items,
        next_url=next_url,
        prev_url=prev_url)

@app.route('/delete-post/<int:id>')
@login_required
def delete_post(id):
    post = Post.query.filter_by(id = id).first()
    db.session.delete(post)
    db.session.commit()
    flash('Post has been deleted')
    return redirect(url_for('chat'))


@app.route("/about_us")
def about_us():
    """About_Us  URL"""
    return render_template('about_us.html', title='SIFA group')



@app.route("/patners")
def patners():
    """Patners URL"""
    return render_template('patners.html', title='SIFA partners')