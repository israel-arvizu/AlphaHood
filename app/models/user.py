from .transaction import Transaction
from .db import db

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
<<<<<<< HEAD
from .watchlist import watchlist
=======
from .watchlist import Watchlist
>>>>>>> origin/main



class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
<<<<<<< HEAD
    birthday=db.Column(db.Date, nullable=False)
    balance=db.Column(db.Float, nullable=False)
=======
    birthday = db.Column(db.Date, nullable=False)
    balance = db.Column(db.Float, nullable=False)
>>>>>>> origin/main

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        print(check_password_hash(self.password, password), '--------------------')
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'birthday': self.birthday,
            'balance': self.balance

        }

<<<<<<< HEAD
    stocks = db.relationship("Stock", secondary=watchlist, back_populates="users")
    portfolios = db.relationship("Portfolio", back_populates="users", cascade="all,delete-orphan")
    purchaseHistories = db.relationship("PurchaseHistory", back_populates='users')
=======
    stocks = db.relationship("Stock", secondary=Watchlist, back_populates="users", cascade="all")
    portfolios = db.relationship("Portfolio", back_populates="users")
    transactions = db.relationship("Transaction", back_populates="users", cascade="all,delete-orphan")
>>>>>>> origin/main
