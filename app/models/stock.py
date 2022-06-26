from .db import db
from .watchlist import watchlists

Base=db.declarative_base()


class Stock(Base):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(60))
    Ticker = db.Column(db.String(5))
    MarketCap = db.Column(db.Float)
    HighToday = db.Column(db.Float)
    LowToday= db.Column(db.Float)

    users = db.relationship("User", secondary=watchlists, back_populates="stocks")
    portfolio = db.relationship("Portfolio", back_populates="stocks")
