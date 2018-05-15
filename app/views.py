from flask import render_template, session, url_for, redirect, flash
from passlib.hash import sha256_crypt
import pandas as pd
from functools import wraps
import logging

from app import app, mongo
from app.forms import LoginForm, TeamForm


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


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/standings')
def standings():
    teams = list(mongo.db.teams.find())
    teams_df = pd.DataFrame(teams).sort_values(by=['points'], ascending=False)

    return render_template('standings.html', teams=teams_df.to_dict(orient='records'))


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



