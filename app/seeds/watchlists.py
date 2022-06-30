from app.models import db, Watchlist

def seed_watchlists():
    first = Watchlist(
        name="My First List", userId=1, listId=1
    )
    second = Watchlist(
        name="Electronics", userId=1, listId=1
    )

    db.session.add(first)
    db.session.add(second)

    db.session.commit()

def undo_watchlists():
    db.session.execute('TRUNCATE watchlists RESTART IDENTITY CASCADE;')
    db.session.commit()
