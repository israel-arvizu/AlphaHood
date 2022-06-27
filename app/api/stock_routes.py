from datetime import date
from flask import Blueprint, jsonify, session, request
from AlphaHood.app.models.purchase_history import Purchase_History
from app.models import User, db, Stock, Portfolio
import datetime

from flask_login import current_user, login_user, logout_user, login_required

stock_routes = Blueprint('stock', __name__)

# load / get
@stock_routes.route('/<int:id>', methods=["GET"])
@login_required
def get_stock(id):
    stocks = Stock.query.get(id)
    return stocks.to_dict()


# buy /create


@stock_routes.route('/<int:id>', methods=["POST"])
@login_required
def buy_shares():
    req = request.get_json()
    userId = req['userId']
    stockId = req['stockId']
    shares = req['shareCount']

    user = User.query.get(userId)
    stock = Stock.query.get(stockId)

# Change user balance
    user.balance = User.balance - (Stock.price * shares)

# add stock to portfolio
    def stockCheck(userId, stockId):
        rowCheck = Portfolio.query.filter(Portfolio.userId == userId).filter(Portfolio.stockId == stockId)
        if (rowCheck):
            Portfolio.query.filter(Portfolio.id == rowCheck.id).update({
                'shares': rowCheck.shares + shares
            })
        else:
            newPortfolio = Portfolio(
                userId = userId,
                stockId = stockId,
                shares = shares,
                priceBought = stock.price,
                dateBought = datetime.datetime.now()
            )
            db.session.add(newPortfolio)
            db.session.commit()
    stockCheck(userId,stockId)
# put buy order on purchase history
    newPurchase = Purchase_History(
        userId = userId,
        stockId = stockId,
        priceBought = stock.price,
        sharesBought = shares,
        dateBought = datetime.datetime.now()
    )
    db.session.add(newPurchase)
    db.session.commit()
#

# sell / delete WORK IN PROGRESSSSSSSSSS
@stock_routes.route('/sell', methods=['POST'])
def sell_shares():
    req = request.get_json()
    userId = req['userId']
    stockId = req['stockId']
    soldShares = req['shareCount']

    user = User.query.get(userId)
    stock = Stock.query.get(stockId)

# Change user balance
    user.balance = User.balance + (Stock.price * soldShares)

# add stock to portfolio
    def ownedStock(userId, stockId):
        rowCheck = Portfolio.query.filter(Portfolio.userId == userId).filter(Portfolio.stockId == stockId)
        if (rowCheck):
            if (rowCheck.shares - soldShares > 0):
                Portfolio.query.filter(Portfolio.id == rowCheck.id).update({
                    'soldShares': rowCheck.shares - soldShares
            })
        else:
            return ("error")

    ownedStock(userId, stockId)
# put buy order on purchase history
    soldHistory = Purchase_History(
        userId = userId,
        stockId = stockId,
        priceBought = stock.price,
        sharesBought = soldShares,
        dateBought = datetime.datetime.now()
    )
    Purchase_History.query.filter(Purchase_History.userId == userId).update({
                    'soldShares': rowCheck.shares - soldShares
            })

# @stock_routes.route('', methods=["DELETE"])
# @login_required
# def random():
#     pass
# # price/update / put

# @stock_routes.route('', methods=["PUT"])
# @login_required
# def random():
#     pass
