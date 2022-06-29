from flask import Blueprint
from app.models import Stock



search_routes = Blueprint('search', __name__)

@search_routes.route('/', methods=["GET"])
def get_search_stocks():
    stock_lst = []
    stocks = Stock.query.all()


    for idx in range(0, len(stocks)):
        stock_lst.append(
            {"ticker": stocks[idx]["ticker"], "name": stocks[idx].name}
        )
    return {"searched_stocks": stock_lst}
