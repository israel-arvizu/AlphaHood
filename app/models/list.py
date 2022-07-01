from .db import db



class List(db.Model):
    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True)
    stockId = db.Column(db.Integer, db.ForeignKey("stocks.id"))
    watchlistId = db.Column(db.Integer, db.ForeignKey("watchlists.id"))

    watchlists = db.relationship("Watchlist",  back_populates="lists")

    def to_dict(self):
        return {
            'id': self.id,
            'stockId': self.stockId,
            'watchlistId': self.watchlistId,

        }
