import requests
from app import db
from app.blueprints.main.forms import SearchForm
from app.blueprints.main.models import Pokemon, User
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from . import bp as app


@app.route('/')
def home():
    return render_template('index.html')


@login_required
@app.route('/collection')
def collection():
    user = User.query.get(current_user.id)
    pokemon = Pokemon.query.filter_by(owner=user)
    return render_template('collection.html', pokemon=pokemon)


@login_required
@app.route('/search', methods=['get', 'post'])
def search():
    base_api_url = "https://pokeapi.co/api/v2/pokemon/"
    form = SearchForm()
    try:
        if form.validate_on_submit():
            pokemon_name = form.name.data
            api_url = base_api_url + pokemon_name
            data = requests.get(api_url).json()
            api_id = data['id']
            name = data['name']
            type = data['types'][0]['type']['name']
            description = f"Id: {api_id}, name: {name}, type: {type}, height; {data['height']}, weight: {data['weight']}, base experience: {data['base_experience']}, order: {data['order']}"
            user = User.query.get(current_user.id)
            new_poke = Pokemon(api_id=api_id, name=name,
                               type=type, description=description, owner=user)
            db.session.add(new_poke)
            db.session.commit()
            flash(f"{name} successfully added")
            # form.name.data = ''
            return render_template('search.html', form=form)
    except Exception:
        flash("Invalid Pokemon name.")
        form.name.data = ''
        return render_template('search.html', form=form)
    return render_template('search.html', form=form)
