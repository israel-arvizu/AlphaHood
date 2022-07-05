from app.models import db, Portfolio
from datetime import datetime

def seed_portfolio():
    second = Portfolio(
        userId= 1, stockId=1, shares=1, priceBought=145.32, dateBought=datetime.strptime("22/06/25 07:30", "%d/%m/%y %H:%M"))
    third = Portfolio(
        userId= 1, stockId=5, shares=1, priceBought=78.50, dateBought=datetime.strptime("22/06/24 10:30", "%d/%m/%y %H:%M"))


    db.session.add(second)
    db.session.add(third)

    db.session.commit()

def undo_portfolio():
    db.session.execute('TRUNCATE portfolios RESTART IDENTITY CASCADE;')
    db.session.commit()
