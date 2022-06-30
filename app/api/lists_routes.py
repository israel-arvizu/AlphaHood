from flask import Blueprint, json, jsonify, request
from app.models import User, db, Stock, Watchlist
from flask_login import login_required



lists_routes = Blueprint('lists', __name__)

@lists_routes.route('/new', methods=['post'])
@login_required
def add_list():
    print("----------------addlist----------------")
    req = request.get_json()
    newlist= Watchlist(
        name=req['name'],
        userId= req['userId']
    )

    db.session.add(newlist)
    db.session.commit()



    return "success"


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
