from flask import Blueprint, json, jsonify, request
from app.models import User, db, Stock, Watchlist
from flask_login import login_required
import os


dashboard_routes = Blueprint('dashboard', __name__)



# api keys ???


# @dashboard_routes.route('/')
# @login_required
# def random2():
#     pass


# # graph routes


# @dashboard_routes.route('')
# @login_required
# def random2():
#     pass
# #watchlist route

# @dashboard_routes.route('')
# @login_required
# def random2():
#     pass

# # news
# @dashboard_routes.route('')
# @login_required
# def random2():
#     pass
# # TRENding
