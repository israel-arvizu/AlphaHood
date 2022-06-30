from .db import db




class Watchlist (db.Model):
    __tablename__="watchlists"


    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False, unique=True)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"))
    listId = db.Column(db.Integer, db.ForeignKey("lists.id"))

    lists = db.relationship("List", back_populates="watchlists")
    users = db.relationship("User", back_populates="watchlists")
