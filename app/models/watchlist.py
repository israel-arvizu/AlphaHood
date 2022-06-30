from .db import db




<<<<<<< HEAD
watchlist = db.Table(
    'watchlists',
    db.Model.metadata,
    db.Column('name',db.String(100), nullable=False),
    db.Column("stockId", db.ForeignKey("stocks.id"), primary_key=True),
    db.Column("userId", db.ForeignKey("users.id"), primary_key=True)


=======
Watchlist =  db.Table(
    "watchlists",

    db.Model.metadata,
    db.Column('name',db.String(100), nullable=False, unique=True),
    db.Column('stockId',db.ForeignKey("stocks.id")),
    db.Column('userId', db.ForeignKey("users.id")),
>>>>>>> origin/main
)
