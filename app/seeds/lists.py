from app.models import db, List

def seed_lists():
    first=List(
        stockId=1, watchlistId=1
    )
    listStock = List(
        stockId=5, watchlistId=1
    )

    db.session.add(first)
    db.session.add(listStock)

    db.session.commit()

def undo_lists():
    db.session.execute('TRUNCATE lists RESTART IDENTITY CASCADE;')
    db.session.commit()
