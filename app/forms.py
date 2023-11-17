from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateField, IntegerField
from wtforms.validators import DataRequired, Length


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
    