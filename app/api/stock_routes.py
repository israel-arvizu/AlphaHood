from flask import Blueprint, jsonify, session, request
from app.models import User, db, Stock, Portfolio

from flask_login import current_user, login_user, logout_user, login_required

stock_routes = Blueprint('stock', __name__)

# load / get
@stock_routes.route('/<int:id>', methods=["GET"])
@login_required
def get_stock(id):
    stocks = Stock.query.get(id)
    return stocks.to_dict()


# buy /create


@stock_routes.route('', methods=["POST"])
@login_required
def buy_shares():
    req = request.get_json()
    user_id = req['user_id']
    stock_id = req['stock_id']
    portfolio = Portfolio.query.filter_by(user=userid)

# Change user balance
# add stock to portfolio
# put buy order on purchase history
#

# sell / delete

# @stock_routes.route('', methods=["DELETE"])
# @login_required
# def random():
#     pass
# # price/update / put

# @stock_routes.route('', methods=["PUT"])
# @login_required
# def random():
#     pass
