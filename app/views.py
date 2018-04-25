from flask import render_template, request, session, url_for, redirect, flash
from passlib.hash import sha256_crypt
from functools import wraps

from app import app, mongo


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
    # TODO: populate standings with database data
    return render_template('standings.html')


@app.route('/dashboard')
@admin_logged_in
def admin_dashboard():
    return render_template('admin_dashboard.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        admin = mongo.db.users.find_one({'username': username})

        # Verify username and password
        if admin is None or not sha256_crypt.verify(password, admin['password']):
            flash('Invalid username or password', 'danger')
            return redirect(url_for('admin_login'))

        session['admin_logged_in'] = True
        flash('Admin is successfully logged in', 'success')

        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')


@app.route('/logout')
@admin_logged_in
def logout():
    session.clear()
    flash('You have successfully logged out', 'success')
    return redirect(url_for('home'))
