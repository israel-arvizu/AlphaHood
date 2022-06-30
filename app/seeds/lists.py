from app.models import db, List

def seed_lists():
    first=List(
        stockId=1, listIdentifier=1
    )
    listStock = List(
        stockId=2, listIdentifier=1
    )

    db.session.add(first)
    db.session.add(listStock)

    db.session.commit()

def undo_lists():
    db.session.execute('TRUNCATE lists RESTART IDENTITY CASCADE;')
    db.session.commit()
