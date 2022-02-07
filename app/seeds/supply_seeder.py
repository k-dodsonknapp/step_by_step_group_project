from app.models import db, Supply

def seed_supplies():
    bird_house_supply1 = Supply(
        projectId=1,
        supply="wood",
        amount=6,
    )

    bird_house_supply2 = Supply(
        projectId=1,
        supply="wood glue",
        amount=1,
    )

    bird_house_supply3 = Supply(
        projectId=1,
        supply="shingles",
        amount=20,
    )


    db.session.add(bird_house_supply1)
    db.session.add(bird_house_supply2)
    db.session.add(bird_house_supply3)
    
    db.session.commit()

def undo_supplies():
    db.session.execute('TRUNCATE supplies RESTART IDENTITY CASCADE;')
    db.session.commit()