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
    watchListId = Watchlist.query.all()





    return "hello"



@lists_routes.route('/addstock', methods=['post'])
@login_required
def add_stock():

    req = request.get_json()
    addToList= List(
        name=req['stockId'],
        userId= req['watchlistId']
    )


    db.session.add(List)
    db.session.commit()



    return "hello"


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
