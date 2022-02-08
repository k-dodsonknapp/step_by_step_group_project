from app.models import db, Comment

def seed_comments():
    bird_house_comment1= Comment(
        userId=2,
        projectId=1,
        comment="Hi <user> I was wondering what type of glue you recommend?"
    )

    bird_house_comment2= Comment(
        userId=3,
        projectId=1,
        comment="Wow this is so cool! I am going to use this to teach my granddaughter how to build this! Thanks!"
    )

    casino_clock_comment1= Comment(
        userId=1,
        projectId=2,
        comment="Wow this is so cool! I am going to build this for my brother. Thanks for taking the time."
    )

    casino_clock_comment2= Comment(
        userId=2,
        projectId=2,
        comment="Thanks! This is so cool."
    )

    one_board_mug_comment1= Comment(
        userId=1,
        projectId=3,
        comment="I love the idea! Will definitely be making this in the future."
    )

    one_board_mug_comment2= Comment(
        userId=1,
        projectId=3,
        comment="Thanks! This is so cool."
    )

    db.session.add(bird_house_comment1)
    db.session.add(bird_house_comment2)
    db.session.add(casino_clock_comment1)
    db.session.add(casino_clock_comment2)
    db.session.add(one_board_mug_comment1)
    db.session.add(one_board_mug_comment2)


    db.session.commit()


def undo_comments():
    db.session.execute('TRUNCATE comments RESTART IDENTITY CASCADE')
    db.session.commit()