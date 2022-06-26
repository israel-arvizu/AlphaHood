from .db import db

Base=db.declarative_base()


watchlists = db.Table(
    'watchlists',
    Base.metadata,
    name=db.Column(db.String(100), nullable=False)
    db.Column("stock_id", db.ForeignKey("stocks.id"), primary_key=True),
    db.Column("user_id", db.ForeignKey("users.id"), primary_key=True)
)
