from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from .models import User


class RegisterForm(Form):
    email = StringField("E-mail address", validators=[DataRequired('Please insert your e-mail'), Email()])
    password = PasswordField("Password", validators=[DataRequired('Please insert your password'),
                                                     EqualTo('confirm', message='Password must match')])
    confirm = PasswordField("Confirm password", validators=[DataRequired('Please insert your confirm password')])
    submit = SubmitField("Register")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False

        user = User.query.filter_by(email=self.email.data.lower()).first()
        if user:
            self.email.errors.append("That email is already taken")
            return False
        else:
            return True
