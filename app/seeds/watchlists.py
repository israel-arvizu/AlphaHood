from app.models import db, Watchlist

def seed_watchlists():
    third = Watchlist(
        name="Portfolio", userId=1
    )
    db.session.add(third)

    db.session.commit()

def undo_watchlists():
    db.session.execute('TRUNCATE watchlists RESTART IDENTITY CASCADE;')
    db.session.commit()
