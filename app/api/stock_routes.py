from datetime import date
from flask import Blueprint, jsonify, session, request
from app.models import User, db, Stock, Portfolio, Transaction
import datetime
import yfinance as yf
import pandas as pd

from flask_login import current_user, login_user, logout_user, login_required

stock_routes = Blueprint('stocks', __name__)

# load / get
@stock_routes.route('/<ticker>', methods=["GET"])
@login_required
def get_stock(ticker):
    tickerUpper = ticker.upper()
    selectedStock = Stock.query.filter(Stock.ticker == tickerUpper).first()
    # newStock = yf.Ticker(selectedStock.ticker).info
    # print(newStock)
    return jsonify(selectedStock.to_dict())

@stock_routes.route('/update/<ticker>', methods=["POST"])
@login_required
def update_stock(ticker):
    print('=======================RUNNING UPDATE=======================')
    tickerUpper = ticker.upper()
    selectedStock = Stock.query.filter(Stock.ticker == tickerUpper).first()
    newStock = yf.Ticker(selectedStock.ticker).info

    selectedStock.marketCap = newStock['marketCap']
    selectedStock.dayHigh = newStock['dayHigh']
    selectedStock.dayLow = newStock['dayLow']
    selectedStock.currentPrice = newStock['currentPrice']
    selectedStock.fullTimeEmployees = newStock['fullTimeEmployees']
    selectedStock.trailingPE = newStock['trailingPE']
    selectedStock.dividendYield = newStock['dividendYield']
    selectedStock.averageVolume = newStock['averageVolume']
    selectedStock.regularMarketOpen = newStock['regularMarketOpen']
    selectedStock.volume = newStock['volume']
    selectedStock.fiftyTwoWeekHigh = newStock['fiftyTwoWeekHigh']
    selectedStock.fiftyTwoWeekLow = newStock['fiftyTwoWeekLow']
    selectedStock.recommendationKey = newStock['recommendationKey']

    db.session.commit()
    # print(selectedStock.currentPrice)
    # print(newStock['currentPrice'])
    return jsonify(selectedStock.to_dict())

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


# sell / delete WORK IN PROGRESSSSSSSSSS
# @stock_routes.route('/sell', methods=['POST'])
# def sell_shares():
#     req = request.get_json()
#     userId = req['userId']
#     stockId = req['stockId']
#     soldShares = req['shareCount']

#     user = User.query.get(userId)
#     stock = Stock.query.get(stockId)

# Change user balance
    user.balance = User.balance + (Stock.price * soldShares)

# add stock to portfolio
    def ownedStock(userId, stockId):
        portfolioCheck = Portfolio.query.filter(Portfolio.userId == userId).filter(Portfolio.stockId == stockId)
        if (portfolioCheck):
            if (portfolioCheck.shares - soldShares > 0):
                Portfolio.query.filter(Portfolio.id == portfolioCheck.id).update({
                    'soldShares': portfolioCheck.shares - soldShares
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


@stock_routes.route('/loadfeaturelists', methods=["POST"])
def featurelists():
    tickerList = []
    i = 0
    req = request.get_json()
    for stock in req:
        try:
            currentStock = yf.Ticker(stock)
            currentStockInfo=currentStock.info
            # increase / original * 100
            performancePercentage = ((currentStockInfo['currentPrice'] - currentStockInfo['regularMarketOpen']) / currentStockInfo['regularMarketOpen']) * 100
            performancePercentage = round(performancePercentage, 2)
            currentStockobj = {"name": currentStockInfo['shortName'], "ticker": stock, "price": currentStockInfo['currentPrice'],"todayPerformance": performancePercentage, "marketCap": currentStockInfo['marketCap']}
            tickerList.append(currentStockobj)
            i += 1
        except:
            tickerList.error = "Something went wrong!"

    return jsonify(tickerList)

@stock_routes.route('/getportfolio/<int:id>')
def portfolio(id):
    userId = id;
    stocks = Portfolio.query.filter(Portfolio.userId == userId);
    stockList = []
    portfolioValue = 0;
    for stock in stocks:
        newDict = {"id": stock.id, "userId": stock.userId,
        "stockId": stock.stockId,
        "shares": stock.shares,
        }
        stockList.append(newDict)

    for stock in stockList:
        stockTicker = Stock.query.filter(Stock.id == stock["stockId"])
        for stock in stockTicker:
            tick = yf.Ticker(stock.ticker)
            currentStock = tick.info
            portfolioValue += currentStock["currentPrice"];

    return jsonify(portfolioValue);

@stock_routes.route('/loadportfolio/<int:id>')
def portfolioList(id):
    userId = id;
    stocks = Portfolio.query.filter(Portfolio.userId == userId)
    listPort = []
    listTickers = [];
    for stock in stocks:
        newDict = {"id": stock.id, "userId": stock.userId,
        "stockId": stock.stockId,
        "shares": stock.shares,
        "priceBought": stock.priceBought,
        "dateBought": stock.dateBought
        }
        listPort.append(newDict)

    for stock in listPort:
        stockTicker = Stock.query.filter(Stock.id == stock["stockId"])
        for stock in stockTicker:
            tick = yf.Ticker(stock.ticker)
            data = yf.download(stock.ticker, group_by="Ticker", period="1d", interval="5m")
            data = data[['Open']]
            data.columns =  [data.columns[0]]
            separated = [data.iloc[:,i] for i in range(len(data.columns))]
            listTickers.append(list(filter(lambda x: x[0:4] == "2022", str(separated).split("\n"))))

    portDict = {}
    for stockFrames in listTickers:
        for timeFrames in stockFrames:
            splitList = timeFrames.split("    ")
            if splitList[0] in portDict:
                portDict[splitList[0]] += float(splitList[1])
            else:
                portDict[splitList[0]] = float(splitList[1])

    return jsonify(portDict)
