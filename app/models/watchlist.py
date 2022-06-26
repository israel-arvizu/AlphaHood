from .db import db

Base=db.declarative_base()


watchlists = db.Table(
    'watchlists',
    Base.metadata,
    db.Column("stock_id", db.ForeignKey("stocks.id"), primary_key=True),
    db.Column("user_id", db.ForeignKey("users.id"), primary_key=True)
)
