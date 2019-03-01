from flask import render_template, session, url_for, redirect, flash, request, abort, jsonify
from passlib.hash import sha256_crypt
import pandas as pd
from functools import wraps
from datetime import date
from bson.objectid import ObjectId
from bson import json_util

from app import app, mongo
from app.forms import LoginForm, TeamForm, SelectTeamForm, BlogPostForm


# Decorator to check if admin is logged in
def admin_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'admin_logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Access denied', 'danger')
            return redirect(url_for('home'))
    return wrap


def get_standings():
    teams = list(mongo.db.teams.find())
    return pd.DataFrame(teams).sort_values(by=['points'], ascending=False)


# Routes

# @app.route('/', methods=['GET'])
# def home():
#     return jsonify('pong!')


@app.route('/api/standings', methods=['GET'])
def standings():
    teams_df = get_standings()
    #return render_template('standings.html', teams=teams_df.to_dict(orient='records'))
    return json_util.dumps(teams_df.to_dict(orient='records'))


@app.route('/api/players', methods=['GET'])
def players():
    teams = list(mongo.db.teams.find())
    return json_util.dumps(teams)


@app.route('/api/stats/<string:captain>')
def stats(captain):
    captain = ' '.join(captain.split('-'))
    team = mongo.db.teams.find_one({'captain': captain})
    #return render_template('stats.html', team=team)
    return json_util.dumps(team)

##################################################



# @app.route('/stats/<string:captain>')
# def stats(captain):
#     team = mongo.db.teams.find_one({'captain': captain})
#     return render_template('stats.html', team=team)


@app.route('/dashboard')
@admin_logged_in
def admin_dashboard():
    return render_template('admin_dashboard.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        admin = mongo.db.users.find_one({'username': username})

        # Verify username and password
        if admin is None or not sha256_crypt.verify(password, admin['password']):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('admin_login'))

        session['admin_logged_in'] = True
        flash('Admin is successfully logged in', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin_login.html', form=login_form)


@app.route('/logout')
@admin_logged_in
def logout():
    session.clear()
    flash('You have successfully logged out', 'success')
    return redirect(url_for('home'))


@app.route('/add_team', methods=['GET', 'POST'])
@admin_logged_in
def add_team():
    team_form = TeamForm()

    if team_form.validate_on_submit():
        team = {
            'name': team_form.team_name.data,
            'captain': team_form.team_captain.data,
            'points': team_form.points.data
        }

        mongo.db.teams.insert_one(team)

        flash('{} successfully added.'.format(team['name']), 'success')
        return redirect(url_for('add_team'))

    return render_template('admin_add_team.html', form=team_form)


@app.route('/update_team', methods=['GET', 'POST'])
@admin_logged_in
def update_team():
    teams_df = get_standings()
    teams = teams_df.to_dict(orient='records')

    select_team_form = SelectTeamForm()
    select_team_form.selected_team.choices = [(0, 'please select a team')] + [(team['name'], team['name']) for team in teams]

    if select_team_form.validate_on_submit():
        updated_team = request.form.get('selected_team')
        return redirect(url_for('update_team_info', team=updated_team))

    return render_template('admin_update_team.html', form=select_team_form)


@app.route('/update_team_info/<string:team>', methods=['GET', 'POST'])
@admin_logged_in
def update_team_info(team):
    team_form = TeamForm()

    team_to_update = mongo.db.teams.find_one({'name': team})

    team_form.team_name.data = team_to_update['name']
    team_form.team_captain.data = team_to_update['captain']
    team_form.points.data = team_to_update['points']

    if team_form.validate_on_submit():
        updated_team = {
            'name': request.form['team_name'],
            'captain': request.form['team_captain'],
            'points': request.form['points']
        }

        mongo.db.teams.find_one_and_update({'name': team}, {"$set": updated_team})

        flash('{} successfully updated.'.format(updated_team['name']), 'success')
        return redirect(url_for('update_team'))

    return render_template('admin_update_team_info.html', form=team_form)


@app.route('/delete_team', methods=['GET', 'POST'])
@admin_logged_in
def delete_team():
    teams_df = get_standings()
    teams = teams_df.to_dict(orient='records')

    select_team_form = SelectTeamForm()
    select_team_form.selected_team.choices = [(0, 'please select a team')] + [(team['name'], team['name']) for team in teams]

    if select_team_form.validate_on_submit():
        deleted_team = request.form.get('selected_team')

        mongo.db.teams.delete_one({'name': deleted_team})

        flash('{} successfully deleted.'.format(deleted_team), 'success')
        return redirect(url_for('delete_team'))

    return render_template('admin_delete_team.html', form=select_team_form)




