from app.models import db, Portfolio
from datetime import datetime

def seed_portfolio():
    first = Portfolio(
        userId= 2, stockId=2, shares=1, priceBought=105.50, dateBought=datetime.strptime("22/06/15 08:30", "%d/%m/%y %H:%M"))
    second = Portfolio(
        userId= 1, stockId=3, shares=1, priceBought=145.32, dateBought=datetime.strptime("22/06/25 07:30", "%d/%m/%y %H:%M"))
    third = Portfolio(
        userId= 1, stockId=6, shares=1, priceBought=105.50, dateBought=datetime.strptime("22/06/24 10:30", "%d/%m/%y %H:%M"))
    fourth = Portfolio(
        userId= 1, stockId=10, shares=1, priceBought=105.50, dateBought=datetime.strptime("22/06/15 08:30", "%d/%m/%y %H:%M"))

    db.session.add(first)
    db.session.add(second)
    db.session.add(third)
    db.session.add(fourth)

    db.session.commit()

def undo_portfolio():
    db.session.execute('TRUNCATE portfolios RESTART IDENTITY CASCADE;')
    db.session.commit()
