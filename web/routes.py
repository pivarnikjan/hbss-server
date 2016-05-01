from flask import render_template, request, session, redirect, url_for

from web import app
from .forms import RegisterForm
from .models import db, User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home page')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        if not form.validate():
            return render_template('signup.html', form=form)
        else:
            new_user = User(form.email.data, form.password.data)
            db.session.add(new_user)
            db.session.commit()

            session['email'] = new_user.email
            return redirect(url_for('success'))

    elif request.method == 'GET':
        return render_template('signup.html', form=form)


@app.route('/success')
def success():
    if 'email' not in session:
        return redirect(url_for('register'))

    user = User.query.filter_by(email=session['email']).first()

    if user is None:
        return redirect(url_for('register'))
    else:
        return render_template('success.html',
                               title='Successful registration')
