from .db import db
from .watchlist import watchlists




class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(60))
    Ticker = db.Column(db.String(5))
    MarketCap = db.Column(db.Float)
    HighToday = db.Column(db.Float)
    LowToday= db.Column(db.Float)

    users = db.relationship("User", secondary=watchlists, back_populates="stocks")
    portfolios = db.relationship("Portfolio", back_populates="stocks")
    purchaseHistories = db.relationship("PurchaseHistory", back_populates='stocks')


    def to_dict(self):
        return {
            "id": self.id,
            "Name": self.Name,
            "Ticker": self.Ticker,
            "MarketCap": self.MarketCap,
            "HighToday": self.HighToday,
            "LowToday": self.LowToday
        }
