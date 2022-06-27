from flask import Blueprint, jsonify, session, request
from app.models import User, db

from flask_login import current_user, login_user, logout_user, login_required

portfolio_routes = Blueprint('portfolio', __name__)
