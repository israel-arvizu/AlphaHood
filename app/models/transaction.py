from collections import UserString
from .db import db
from .stock import Stock



class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    stockId = db.Column(db.Integer, db.ForeignKey('stocks.id'))
    price = db.Column(db.Float, nullable=False)
    shares = db.Column(db.Float, nullable=False)
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String(15), nullable=False)

    users = db.relationship("User", back_populates="transactions")
    stocks = db.relationship("Stock", back_populates="transactions")


    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "stockId": self.stockId,
            "price": self.price,
            "shares": self.shares,
            "date": self.date,
            "type": self.type
        }
