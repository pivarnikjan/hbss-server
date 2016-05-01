from werkzeug.security import generate_password_hash, check_password_hash

from web import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    pwdhash = db.Column(db.String(54))
    tree = db.Column(db.String(120))

    def __init__(self, email, password):
        self.email = email.lower()
        self.set_password(password)

    def __repr__(self):
        return '<User %r>' % self.email

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)
