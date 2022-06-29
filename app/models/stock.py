from .db import db
from .watchlist import Watchlist




class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    ticker = db.Column(db.String(5))
    marketCap = db.Column(db.BigInteger)
    dayHigh = db.Column(db.Float)
    dayLow = db.Column(db.Float)
    currentPrice = db.Column(db.Float)
    longBusinessSummary = db.Column(db.String)
    fullTimeEmployees = db.Column(db.BigInteger)
    city = db.Column(db.String)
    state = db.Column(db.String)
    trailingPE = db.Column(db.Float)
    dividendYield = db.Column(db.Float) #MAKE SURE IT CAN BE EMPTY
    averageVolume = db.Column(db.BigInteger)
    regularMarketOpen = db.Column(db.Float)
    volume = db.Column(db.BigInteger)
    fiftyTwoWeekHigh = db.Column(db.Float)
    fiftyTwoWeekLow = db.Column(db.Float)
    recommendationKey = db.Column(db.String)
    industry = db.Column(db.String)



    users = db.relationship("User", secondary=Watchlist, back_populates="stocks")
    portfolios = db.relationship("Portfolio", back_populates="stocks")
    transactions = db.relationship("Transaction", back_populates="stocks")


    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "ticker": self.ticker,
            "marketCap": self.marketCap,
            "dayHigh": self.dayHigh,
            "dayLow": self.dayLow,
            "currentPrice": self.currentPrice,
            "longBusinessSummary": self.longBusinessSummary,
            "fullTimeEmployees": self.fullTimeEmployees,
            "city": self.city,
            "state": self.state,
            "trailingPE": self.trailingPE,
            "dividendYield": self.dividendYield,
            "averageVolume": self.averageVolume,
            "regularMarketOpen": self.regularMarketOpen,
            "volume": self.volume,
            "fiftyTwoWeekHigh": self.fiftyTwoWeekHigh,
            "fiftyTwoWeekLow": self.fiftyTwoWeekLow,
            "recommendationKey": self.recommendationKey,
            "industry": self.industry
        }
