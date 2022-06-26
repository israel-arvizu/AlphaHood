from .db import db

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


Base=db.declarative_base()

watchlists = db.Table(
    'watchlists',
    Base.metadata,
    db.Column("stock_id", db.ForeignKey("stocks.id"), primary_key=True),
    db.Column("user_id", db.ForeignKey("users.id"), primary_key=True)
)


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    birthday=db.Column(db.Date, nullable=False)
    balance=db.Column(db.Integer, nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    stocks = db.relationship("Stock", secondary=watchlists, back_populates="users")
    portfolios = db.relationship("Portfolio", back_populates="users")



class Portfolio(Base):
    __tablename__ = 'portfolios'

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.Integer, db.ForeignKey("users.id"))
    stockid = db.Column(db.Integer, db.ForeignKey("stocks.id"))
    shares = db.Column(db.Integer)
    priceBought = db.Column(db.Float)
    dateBought = db.Column(db.Date)

    user = db.relationship("User", back_populates="portfolios")
    stocks = db.relationship("Stock", back_populates="portfolios")

class Stock(Base):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(60))
    Ticker = db.Column(db.String(5))
    MarketCap = db.Column(db.Float)
    HighToday = db.Column(db.Float)
    LowToday= db.Column(db.Float)

    users = db.relationship("User", secondary=watchlists, back_populates="stocks")
    portfolio = db.relationship("Portfolio", back_populates="stocks")
