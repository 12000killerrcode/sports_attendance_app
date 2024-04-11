from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, email

class EditProfileForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    submit =  SubmitField('Edit Profile')

class LoginForm(FlaskForm):
    '''Login Form'''
    email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    '''Register Form'''
    email = StringField('Email', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    register = SubmitField('Register')


class PlayerForm(FlaskForm):
    '''Player Form'''
    firstname = StringField('First Name', validators=[DataRequired(), Length(1, 50)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(1, 50)])
    date_of_birth= DateField('Date of birth', validators=[DataRequired()])
    attendance = StringField('Attendance', validators=[DataRequired(), Length(1, 200)])
    fitness = IntegerField('Fitness', validators=[DataRequired()])
    submit = SubmitField('Submit')    


class PerformanceForm(FlaskForm):
    '''Performance Form'''
    year = StringField('Year', validators=[DataRequired(), Length(0, 5000)])
    season = StringField('Season', validators=[DataRequired(), Length(1, 1000)])
    wins= StringField('Wins', validators=[DataRequired(), Length(0, 1000)])
    losses = StringField('Losses', validators=[DataRequired(), Length(0, 1000)])
    draws = StringField('Draws', validators=[DataRequired(), Length(0, 1000)])
    submit = SubmitField('Submit')    

class TargetForm(FlaskForm):
    '''Target Form'''
    year = StringField('Year', validators=[DataRequired(), Length(0, 5000)])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Submit')