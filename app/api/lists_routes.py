from flask import Blueprint, json, jsonify, request

from app.models import User, db, Stock, Watchlist, List
from flask_login import login_required



lists_routes = Blueprint('lists', __name__)

@lists_routes.route('/new', methods=['post'])
@login_required
def add_list():

    req = request.get_json()
    newWatchList= Watchlist(
        name=req['name'],
        userId= req['userId']
    )

    db.session.add(newWatchList)
    db.session.commit()
    return newWatchList.to_dict()


@lists_routes.route('/', methods=['post'])
@login_required
def load_watchlist():
    req = request.get_json()
    watchlists = Watchlist.query.filter_by(userId=int(req)).all()
    return {'watchlists': [watchlist.to_dict() for watchlist in watchlists]}

@lists_routes.route('/<int:id>/edit', methods=['post'])
@login_required
def update_list(id):
    req = request.get_json()

    watchlist = Watchlist.query.get(id)
    watchlist.name = req
    db.session.commit()

    return watchlist.to_dict()


@lists_routes.route('/stocks', methods=['post'])
@login_required
def load_list():
    watchListsArr = request.get_json()
    stockObj = {}
    for watchList in watchListsArr:
        indvList = List.query.filter(List.watchlistId == watchList).all()
        listArry = []
        for listS in indvList:
            singleList = listS.to_dict()
            stock = Stock.query.filter(Stock.id == singleList["stockId"]).one()
            stockTicker = {"ticker": stock.ticker, "currentPrice": stock.currentPrice}
            listArry.append(stockTicker)
        stockObj[watchList] = listArry

    return jsonify(stockObj)



@lists_routes.route('/addstock', methods=['post'])
@login_required
def add_stock():

    req = request.get_json()
    print("23423423423423424323442", req)
    for lists in req['arrays']:
        print(lists)

        newlist = List(
            stockId=req['stockId'],
            watchlistId=lists
        )
        db.session.add(newlist)
        db.session.commit()


   ## addToList= List(
   ##     name=req['lists'],
   ##     watchlist= req['watchlistId']
   ## )
#
    #db.session.add(List)
    #db.session.commit()


    return "hello"

@lists_routes.route('/deletestock', methods=['post'])
@login_required
def delete_stock():
    req=request.get_json()
    stockid = req['stockId']
    print(req)
    for listid in req['arrays']:
        oldlist = List.query.filter_by(watchlistId=int(listid), stockId=stockid)

        oldlist.delete()
        db.session.commit()

    return jsonify(req['arrays'])



@lists_routes.route('/<int:id>/', methods=['post'])
@login_required
def delete_list(id):

    req = request.get_json()
    watchlist = Watchlist.query.filter_by(id=id)
    watchlist.delete()
    db.session.commit()

    return jsonify(id)

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
