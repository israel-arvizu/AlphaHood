import yfinance as yf
from flask import Blueprint, jsonify
from flask_login import current_user, login_user, logout_user, login_required
import random

news_routes = Blueprint('news', __name__)

@news_routes.route('/load')
@login_required
def loadNews():
    """
    Loads news in dashboard
    """
    newsList = ['APPL', 'TSLA', 'MSFT', 'NVDA', 'GOOGL', 'AMD', 'TWTR'];
    currentNews = {}

    try:
        currentNews = yf.Ticker(newsList[random.randrange(0, 6)])
    except:
        raise NewsError("Couldn't Fetch News")
    print(currentNews.news)
    return jsonify(currentNews.news)


@news_routes.route('/<ticker>')
@login_required
def loadTickerNews(ticker):
    tickerUpper = ticker.upper()
    stockNews = yf.Ticker(tickerUpper).news

    randomNews = stockNews[random.randrange(0, len(stockNews))]
    # print(randomNews)
    return jsonify(randomNews)
