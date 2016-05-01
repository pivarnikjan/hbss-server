from flask import render_template, request, flash

from web import app
from .forms import RegisterForm


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
            flash('All fields are required.')
            return render_template('signup.html', form=form)
        else:
            return 'Form posted.'

    elif request.method == 'GET':
        return render_template('signup.html', form=form)

