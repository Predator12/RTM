from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.mongo_folder import UserMongoModel
from app import logger

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    logger.info("request data {}".format(request.form))
    try:
        user = UserMongoModel.objects.get({"name": username})
        logger.info('Successful get user {} from db'.format(user.name))
    except BaseException:
        user = None

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    # if not user or not check_password_hash(user.password, password):
    if not user or user.password != password:
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    session["last_name"] = user.lastname
    session["email"] = user.email
    logger.info("Successful login")
    return redirect(url_for('main.profile'))


@auth.route('/logout')
def logout():
    logout_user()
    logger.info("Successful logout")
    return render_template('login.html')
