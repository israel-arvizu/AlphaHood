from datetime import date
from flask import Blueprint, jsonify, session, request
from app.models import User, db, Stock, Portfolio, Transaction
import datetime
import yfinance as yf
import pandas as pd
from datetime import datetime
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

@stock_routes.route('/<ticker>/buy', methods=['GET','POST'])
@login_required
def buy_stock(ticker):
    req = request.get_json()
    currentUserId = req['userId']
    userBalance = float(req['userBalance'])
    shareCount = int(req['shareCount'])
    stockPrice = float(req['stockPrice'])
    stockId = int(req['stockId'])
    transactionPrice = stockPrice * shareCount
    user = User.query.get(currentUserId)
    user.balance = user.balance - transactionPrice
    db.session.commit()
    ownedBool = False

    #check if user already owns stock
    allOwned = Portfolio.query.filter_by(userId=(f"{currentUserId}"))
    for row in allOwned:
        if(row.stockId == stockId):
            ownedBool = True
            row.shares = row.shares + shareCount
            db.session.commit()
            return jsonify('Stock Purchased')
    if(not ownedBool):
        portfolio = Portfolio(
            userId=currentUserId,
            stockId=stockId,
            shares=shareCount,
            priceBought=stockPrice,
            dateBought=datetime.now()
        )
        db.session.add(portfolio)
        db.session.commit()
        return jsonify('Stock Purchased')

    return jsonify('something went wrong')

@stock_routes.route('/<ticker>/sell', methods=['GET','POST'])
@login_required
def sell_stock(ticker):
    req = request.get_json()
    currentUserId = req['userId']
    userBalance = float(req['userBalance'])
    shareCount = int(req['shareCount'])
    stockPrice = float(req['stockPrice'])
    stockId = int(req['stockId'])
    transactionPrice = stockPrice * shareCount
    user = User.query.get(currentUserId)
    user.balance = user.balance + transactionPrice
    db.session.commit()
    ownedBool = False

    allOwned = Portfolio.query.filter_by(userId=(f"{currentUserId}"))
    for row in allOwned:
        if(row.stockId == stockId):
            row.shares = row.shares - shareCount
            db.session.commit()
            return jsonify('Stock sold')

@stock_routes.route('/loadOwnedStocks/<int:id>', methods=['GET'])
@login_required
def load_owned_stocks(id):
    userId = id
    stocks = Portfolio.query.filter(Portfolio.userId == userId)
    stockList = []
    for stock in stocks:
        newDict = {"id": stock.id, "userId": stock.userId,
        "stockId": stock.stockId,
        "shares": stock.shares,
        }
        stockList.append(newDict)
    return jsonify(stockList)

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
    userId = id
    stocks = Portfolio.query.filter(Portfolio.userId == userId)
    stockList = []
    portfolioValue = 0
    for stock in stocks:
        newDict = {"id": stock.id, "userId": stock.userId,
        "stockId": stock.stockId,
        "shares": stock.shares,
        }
        stockList.append(newDict)

    for stock in stockList:
        stockTicker = Stock.query.filter(Stock.id == stock["stockId"])
        numOfShares = stock["shares"]
        for stock in stockTicker:
            tick = yf.Ticker(stock.ticker)
            currentStock = tick.info
            portfolioValue += currentStock["currentPrice"] * numOfShares; # <--- CURR PRICE X NUMBER OF SHARES

    return jsonify(portfolioValue)

@stock_routes.route('/loadportfolio/<int:id>')
def portfolioList(id):
    userId = id
    stocks = Portfolio.query.filter(Portfolio.userId == userId)
    listPort = []
    listStock = []
    listTickers = []
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
        numOfShares = stock["shares"]
        for stock in stockTicker:
            tick = yf.Ticker(stock.ticker)
            data = yf.download(stock.ticker, group_by="Ticker", period="1d", interval="5m")
            data = data[['Open']]
            data.columns =  [data.columns[0]]
            separated = [data.iloc[:,i] for i in range(len(data.columns))]
            row = list(filter(lambda x: x[0:4] == "2022", str(separated).split("\n")))
            for timeFrames in row:
                splitList = timeFrames.split("    ")
                splitList[1] = float(splitList[1]) * numOfShares
                listStock.append(splitList[0]+"    "+ str(splitList[1]))
            listTickers.append(listStock)

    portDict = {}
    for stockFrames in listStock:
        splitList = stockFrames.split("    ")
        if splitList[0] in portDict:
            portDict[splitList[0]] += float(splitList[1])
        else:
            portDict[splitList[0]] = float(splitList[1])

    return jsonify(portDict)
