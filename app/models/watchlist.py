from .db import db




watchlists = db.Table(
    'watchlists',
    db.Model.metadata,
    db.Column('name',db.String(100), nullable=False),
    db.Column("stock_id", db.ForeignKey("stocks.id"), primary_key=True),
    db.Column("user_id", db.ForeignKey("users.id"), primary_key=True)


)
