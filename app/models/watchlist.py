from .db import db




class Watchlist(db.Model):
    __tablename__= 'watchlists'

    db.Model.metadata
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    stockId= db.Column(db.ForeignKey("stocks.id"))
    userId=db.Column(db.ForeignKey("users.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "stockId": self.stockId,
            "userId": self.userId

        }
