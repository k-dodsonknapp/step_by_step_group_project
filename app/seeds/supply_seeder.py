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

    casino_clock_supply1=Supply(
        projectId=2,
        supply="A deck of French-suited playing card (bridge size : around 57 x 89mm)"
    )

    casino_clock_supply2=Supply(
        projectId=2,
        supply="Three 28BYJ-48 stepper motor with driver board comes with"
    )
    casino_clock_supply3=Supply(
        projectId=2,
        supply="Micro computer with 12 or more IO ports. I used M5stamp C3"
    )

    casino_clock_supply4=Supply(
        projectId=2,
        supply="Double sided adhesive tape"
    )

    casino_clock_supply5=Supply(
        projectId=2,
        supply="Some tapping screws"
    )

    casino_clock_supply6=Supply(
        projectId=2,
        supply="zip ties"
    )

    one_board_mug1=Supply(
        projectId=3,
        supply="Pine board or any wood of your choosing."
    )

    one_board_mug2=Supply(
        projectId=3,
        supply="Scroll saw"
    )

    one_board_mug3=Supply(
        projectId=3,
        supply="Wood glue"
    )

    one_board_mug4=Supply(
        projectId=3,
        supply="Wood oil/ conditioner"
    )

    one_board_mug5=Supply(
        projectId=3,
        supply="Dowel pins (if you want to add extra support for the handle)"
    )
    

    db.session.add(bird_house_supply1)
    db.session.add(bird_house_supply2)
    db.session.add(bird_house_supply3)
    db.session.add(casino_clock_supply1)
    db.session.add(casino_clock_supply2)
    db.session.add(casino_clock_supply3)
    db.session.add(casino_clock_supply4)
    db.session.add(casino_clock_supply5)
    db.session.add(casino_clock_supply6)
    db.session.add(one_board_mug1)
    db.session.add(one_board_mug2)
    db.session.add(one_board_mug3)
    db.session.add(one_board_mug4)
    db.session.add(one_board_mug5)
    
    db.session.commit()

def undo_supplies():
    db.session.execute('TRUNCATE supplies RESTART IDENTITY CASCADE;')
    db.session.commit()