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
def load_list():
    req = request.get_json()
    print(req)
    watchlists = Watchlist.query.filter_by(userId=int(req)).all()
    print(watchlists)

    return {'watchlists': [watchlist.to_dict() for watchlist in watchlists]}

@lists_routes.route('/<int:id>/edit', methods=['post'])
@login_required
def update_list(id):
    req = request.get_json()

    watchlist = Watchlist.query.get(id)
    watchlist.name = req
    db.session.commit()

    return watchlist.to_dict()




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
