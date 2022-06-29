import yfinance as yf
from flask import Blueprint, jsonify
import random

news_routes = Blueprint('news', __name__)

@news_routes.route('/load')
def loadNews():
    """
    Loads news in dashboard
    """
    newsList = ['APPL', 'TSLA', 'MSFT', 'NVDA', 'GOOGL', 'AMD', 'TWTR'];

    currentNews = yf.Ticker(newsList[random.randrange(0, 6)]);

    return jsonify(currentNews.news);
