from flask import Blueprint, jsonify
from app.models import Stock

search_routes = Blueprint('search', __name__)

@search_routes.route('/', methods=["GET"])
def get_stocks():
    searchedStocks = Stock.query.all()
    return jsonify(searchedStocks)
