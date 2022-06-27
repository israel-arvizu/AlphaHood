from .db import db




watchlist = db.Table(
    'watchlists',
    db.Model.metadata,
    db.Column('name',db.String(100), nullable=False),
    db.Column("stockId", db.ForeignKey("stocks.id"), primary_key=True),
    db.Column("userId", db.ForeignKey("users.id"), primary_key=True)


)
