from collections import UserString
from .db import db
from .stock import Stock
from .user import User


class Purchase_History(db.Model):
    __tablename__ = 'purchase_histories'

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('users.id'))
    stockId = db.Column(db.Integer, db.ForeignKey('stocks.id'))
    priceBought = db.Column(db.Float, nullable=False)
    sharesbought = db.Column(db.Float, nullable=False)
    dateBought = db.Column(db.Date, nullable=False)
    priceSold = db.Column(db.Float)
    sharesSold= db.Column(db.Float)
    dateSold = db.Column(db.Date)

    users = db.relationship("User", back_populates="purchaseHistory")
    stocks = db.relationship("Stock", back_populates="purchaseHistory")


    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "stockId": self.stockId,
            "priceBought": self.priceBought,
            "sharesBought": self.sharesBought,
            "dateBought": self.dateBought,
            "priceSold": self.priceSold,
            "sharesSold": self.sharesSold,
            "dateSold": self.dateSold
        }
