from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import User, db

user_routes = Blueprint('users', __name__)


@user_routes.route('/')
@login_required
def users():
    users = User.query.all()
    return {'users': [user.to_dict() for user in users]}



@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()


@user_routes.route('/<int:id>/balance', methods=['POST'])
@login_required
def user_add_balance(id):
    req = request.get_json()
    user = User.query.get(id)
    user.balance = user.balance + int(req)
    db.session.commit()

    return user.to_dict()
