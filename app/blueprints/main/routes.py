from flask import redirect, render_template, url_for
from flask_login import current_user

from . import bp as app


@app.route('/')
def home():
    return render_template('index.html')

