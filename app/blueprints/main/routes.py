import requests
from app import db
from app.blueprints.main.forms import SearchForm
from app.blueprints.main.models import Pokemon
from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from . import bp as app


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/collection')
def collection():
    return render_template('collection.html')


@login_required
@app.route('/search', methods=['get', 'post'])
def search():
    base_api_url = "https://pokeapi.co/api/v2/pokemon/"
    form = SearchForm()
    if form.validate_on_submit():
        pokemon_name = form.name.data
        api_url = base_api_url + pokemon_name
        data = requests.get(api_url).json()
        form.name.data = ''
        return render_template('search.html', form=form, api_response=data)

    return render_template('search.html', form=form)
