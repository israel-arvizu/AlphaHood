from flask import Blueprint, jsonify, session, request
from app.models import User, db, Watchlist, List
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash

auth_routes = Blueprint('auth', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        password = generate_password_hash(form.data['password'])
        user = User(
            username=form.data['username'],
            email=form.data['email'],
            birthday=form.data['birthday'],
            hashed_password=password,
            balance=0
            )
        db.session.add(user)
        db.session.commit()
        watchlistPort = Watchlist(
            name="Portfolio",
            userId=user.id
        )
        db.session.add(watchlistPort)
        db.session.commit()

        watchlist = Watchlist(
            name="My First List",
            userId=user.id
        )
        db.session.add(watchlist)
        db.session.commit()




        liststock = List(
            stockId=22,
            watchlistId=watchlist.id
        )
        db.session.add(liststock)
        db.session.commit()
        liststock1 = List(
            stockId=23,
            watchlistId=watchlist.id
        )
        db.session.add(liststock1)
        db.session.commit()
        liststock2 = List(
            stockId=19,
            watchlistId=watchlist.id
        )
        db.session.add(liststock2)
        db.session.commit()
        liststock3 = List(
            stockId=223,
            watchlistId=watchlist.id
        )
        db.session.add(liststock3)
        db.session.commit()
        liststock4 = List(
            stockId=101,
            watchlistId=watchlist.id
        )
        db.session.add(liststock4)
        db.session.commit()
        liststock5 = List(
            stockId=322,
            watchlistId=watchlist.id
        )
        db.session.add(liststock5)
        db.session.commit()

        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
