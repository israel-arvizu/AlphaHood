from .db import db



class PurchaseHistory(db.Model):
    __tablename__ = 'purchaseHistories'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    stockid = db.Column(db.Integer, db.ForeignKey("stocks.id"), nullable=False)
    sharesBought = db.Column(db.Integer)
    priceBought = db.Column(db.Float)
    dateBought = db.Column(db.Date)
    priceSold = db.Column(db.Float)
    sharesSold = db.Column(db.Float)
    dateSold = db.Column(db.Date)

    users = db.relationship("User", back_populates="purchaseHistory")
    stocks = db.relationship("Stock", back_populates="purchaseHistory")


    def to_dict(self):
        return {
            "id": self.id,
            "userid": self.userid,
            "stockid": self.stockid,
            "sharesBought": self.sharesBought,
            "priceBought": self.priceBought,
            "dateBought": self.dateBought,
            "priceSold": self.priceSold,
            "sharesSold": self.sharesSold,
            "dateSold": self.dateSold,

        }
