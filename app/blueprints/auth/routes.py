from app import db
from app.blueprints.main.models import User
from app.blueprints.auth.forms import RegistrationForm
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from . import bp as app


@app.route('/login', methods=['get', 'post'])
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
