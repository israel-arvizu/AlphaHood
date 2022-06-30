from .db import db



class List(db.Model):
    __tablename__ = 'lists'

    id = db.Column(db.Integer, primary_key=True)
    stockId = db.Column(db.Integer, db.ForeignKey("stocks.id"))
    listIdentifier=db.Column(db.Integer)

    watchlists = db.relationship("Watchlist", back_populates="lists")
