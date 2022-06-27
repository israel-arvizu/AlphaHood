from .db import db



class Portfolio(db.Model):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("users.id"))
    stockid = db.Column(db.Integer, db.ForeignKey("stocks.id"))
    shares = db.Column(db.Integer)
    priceBought = db.Column(db.Float)
    dateBought = db.Column(db.Date)

    users = db.relationship("User", back_populates="portfolios")
    stocks = db.relationship("Stock", back_populates="portfolios")
