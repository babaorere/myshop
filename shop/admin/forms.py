from wtforms import Form, BooleanField, StringField, PasswordField, validators
import email_validator

class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=128)])
    username = StringField('Username', [validators.Length(min=4, max=32)])
    email = StringField('Email Address', [validators.Length(min=6, max=128), validators.Email()])
    password = PasswordField('New Password', [
        validators.Length(min=4, max=32),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
#    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

class LoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=128), validators.Email()])
    password = PasswordField('New Password', [validators.Length(min=4, max=32)])
