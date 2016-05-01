from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(Form):
    email = StringField("E-mail address", validators=[DataRequired('Please insert your e-mail'), Email()])
    password = PasswordField("Password", validators=[DataRequired('Please insert your password'),
                                                     EqualTo('confirm', message='Password must match')])
    confirm = PasswordField("Confirm password", validators=[DataRequired('Please insert your confirm password')])
    submit = SubmitField("Register")
