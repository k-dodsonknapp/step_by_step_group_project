from app.models import db, Project


# demo projects
def seed_project():
    bird_house= Project(
        userId=1, 
        title="How to build a bird house.", 
        titleImage="idk", 
        overview="This is how to construct a bird house!",
        category="Crafts"
    )

    casino_clock= Project(
        userId=2, 
        title="Casino'clock - Playing card flap display / clock", 
        titleImage="https://content.instructables.com/ORIG/F8U/KR3T/KZCPHOFJ/F8UKR3TKZCPHOFJ.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=16727930c4e9a859906b057dd58a338d", 
        overview="""
            One of the main difficulty to make a split flap display with 3D printer is the fabrication of flaps. 
            Therefore I used off-the-shelf playing cards for flaps, and made a funny and crazy clock with minimum number of parts. 
            Simple design : each display unit consists of only 3 types of parts. Sensor is not used to find the origin. 
            Funny motion : by arranging cards randomly, you can enjoy busy motion of flaps 
            WiFi time acquisition : current time is acquired via WiFi using ntp
            """,
        category="Circuits"
    )

    # bird_house= Project(
    #     userId=1, 
    #     title="How to build a bird house.", 
    #     titleImage="idk", 
    #     overview="This is how to construct a bird house!",
    #     category="Crafts"
    # )

    db.session.add(bird_house)
    db.session.add(casino_clock)
    db.session.commit()

def undo_project():
    db.session.execute('TRUNCATE projects RESTART IDENTITY CASCADE;')
    db.session.commit()

