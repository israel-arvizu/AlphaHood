from .db import db




Watchlist =  db.Table(
    "watchlists",

    db.Model.metadata,
    db.Column('name',db.String(100), nullable=False, unique=True),
    db.Column('stockId',db.ForeignKey("stocks.id")),
    db.Column('userId', db.ForeignKey("users.id")),
)
