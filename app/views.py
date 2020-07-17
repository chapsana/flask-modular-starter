# -*- encoding: utf-8 -*-
# Python modules
import os

# Flask modules
from flask import render_template, request, url_for, redirect, send_from_directory,flash
from flask_login import login_user, logout_user, current_user

# App modules
from app import app, lm
from app.forms.auth import LoginForm, RegisterForm
from app.models.user import User

from werkzeug.security import generate_password_hash, check_password_hash


# Provide login manager with load_user callback
@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# Logout user
@app.route('/logout.html')
def logout():
    """ Logout user """
    logout_user()
    return redirect(url_for('index'))


# Reset Password - Not
@app.route('/reset.html')
def reset():
    """ Not implemented """
    return render_template('layouts/auth-default.html',
                           content=render_template('pages/reset.html'))


# Register a new user
@app.route('/register.html', methods=['GET', 'POST'])
def register():
    """ Create a new user """
    # declare the Registration Form
    form = RegisterForm(request.form)
    msg = None
    if request.method == 'GET':
        return render_template('layouts/auth-default.html',
                               content=render_template('pages/register.html', form=form, msg=msg))
    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():
        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)
        email = request.form.get('email', '', type=str)

        # filter User out of database through username
        user = User.query.filter_by(user=username).first()
        # filter User out of database through username
        user_by_email = User.query.filter_by(email=email).first()
        if user or user_by_email:
            msg = 'Error: User exists!'
            flash('Email address already exists')
        else:

            user = User(username, email, password=generate_password_hash(password, method='sha256'))
            user.save()
            msg = 'User created, please <a href="' + url_for('login') + '">login</a>'
    else:
        msg = 'Input error'

    return render_template('layouts/auth-default.html',
                           content=render_template('pages/register.html', form=form, msg=msg))


# Authenticate user
@app.route('/login.html', methods=['GET', 'POST'])
def login():
    # Declare the login form
    form = LoginForm(request.form)
    # Flask message injected into the page, in case of any errors
    msg = None
    # check if both http method is POST and form is valid on submit
    if form.validate_on_submit():
        # assign form data to variables
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)
        # filter User out of database through username
        user = User.query.filter_by(user=username).first()
        if user:
            # if bc.check_password_hash(user.password, password):
            if user.password == password:
                login_user(user)
                return redirect(url_for('index'))
            else:
                msg = "Wrong password. Please try again."
        else:
            msg = "Unknown user - Please register."
    return render_template('layouts/auth-default.html',
                           content=render_template('pages/login.html', form=form, msg=msg))


# App main route + generic routing
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path>')
def index(path):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    content = None
    try:
        # try to match the pages defined in -> pages/<input file>
        return render_template('layouts/default.html',
                               content=render_template('pages/' + path))
    except:
        return render_template('layouts/auth-default.html',
                               content=render_template('pages/error-404.html'))


# Return sitemap
@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.xml')
