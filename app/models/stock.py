from .db import db
from .watchlist import watchlist




class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    ticker = db.Column(db.String(5))
    marketCap = db.Column(db.Float)
    highToday = db.Column(db.Float)
    lowToday= db.Column(db.Float)

    users = db.relationship("User", secondary=watchlist, back_populates="stocks")
    portfolios = db.relationship("Portfolio", back_populates="stocks")
    purchaseHistories = db.relationship("PurchaseHistory", back_populates='stocks')


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ticker": self.ticker,
            "marketCap": self.marketCap,
            "highToday": self.highToday,
            "lowToday": self.lowToday
        }
