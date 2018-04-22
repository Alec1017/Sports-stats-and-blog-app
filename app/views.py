from flask import render_template, request, session, url_for, redirect, flash

from app import app


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

        return redirect(url_for('home'))
    return render_template('admin_login.html')

