from .db import db




class Watchlist (db.Model):
    __tablename__="watchlists"


    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(100), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"))


    lists = db.relationship("List", back_populates="watchlists", cascade="all,delete-orphan")
    users = db.relationship("User", back_populates="watchlists", cascade="all,delete" )


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'userId': self.userId,

        }
