from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
	username = StringField('username',validators=[DataRequired(message='please input username')])
	password = PasswordField('password',validators=[DataRequired(message='please input username')])
	remember_me = BooleanField('remember me!')
	submit = SubmitField('log in')
