from flask import render_template, request, session, url_for, redirect, flash
from functools import wraps

from app import app


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


@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']

        # TODO: create username and password validation checking

        session['admin_logged_in'] = True
        flash('Admin is successfully logged in', 'success')

        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')


@app.route('/dashboard')
@admin_logged_in
def admin_dashboard():
    return render_template('admin_dashboard.html')


@app.route('/logout')
@admin_logged_in
def logout():
    session.clear()
    flash('You have successfully logged out', 'success')
    return redirect(url_for('home'))
