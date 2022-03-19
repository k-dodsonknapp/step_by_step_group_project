from app.models import db, Comment

def seed_comments():
    bird_house_comment1= Comment(
        userId=2,
        projectId=1,
        comment="Hi <user> I was wondering what type of glue you recommend?",
        username="marnie",
    )

    bird_house_comment2= Comment(
        userId=3,
        projectId=1,
        comment="Wow this is so cool! I am going to use this to teach my granddaughter how to build this! Thanks!",
        username="bobbie",
    )

    casino_clock_comment1= Comment(
        userId=1,
        projectId=2,
        comment="Wow this is so cool! I am going to build this for my brother. Thanks for taking the time.",
        username="Demo",
    )

    casino_clock_comment2= Comment(
        userId=2,
        projectId=2,
        comment="Thanks! This is so cool.",
        username="marnie",
    )

    one_board_mug_comment1= Comment(
        userId=1,
        projectId=3,
        comment="I love the idea! Will definitely be making this in the future.",
        username="Demo",
    )

    one_board_mug_comment2= Comment(
        userId=1,
        projectId=3,
        comment="Thanks! This is so cool.",
        username="Demo",
    )

    one_board_mug_comment2= Comment(
        userId=2,
        projectId=4,
        comment="looks delicious! frying the burgers on onions seems like a great trick too! thanks for sharing :) good luck with your book!",
        username="marnie",
    )

    one_board_mug_comment2= Comment(
        userId=1,
        projectId=4,
        comment="looks delicious! thanks for sharing!",
        username="Demo",
    )

    james_webb_comment1=Comment(
        userId=2,
        projectId=5,
        comment="Amazing Job!",
        username="marnie",
    )

    james_webb_comment2=Comment(
        userId=3,
        projectId=5,
        comment="Very nice. And ten billion dollars cheaper than the original. Thanks for sharing your work :-)",
        username="bobbie",
    )

    james_webb_comment3=Comment(
        userId=3,
        projectId=5,
        comment="Such a cute and clever project!",
        username="bobbie",
    )

    slowmo_bird_comment1=Comment(
        userId=1,
        projectId=6,
        comment="Love the pics! Unfortunately, when I had the bird feeder on my south deck, whose door is opposite my computer desk, and had gone through the trouble of also putting in a solar-powered water fountain so the birds had somewhere to drink, the (&&##(@*&& expletive deleted) racoons got into it and caused a lot of damage. :( No more birdie pics and/or videos :((",
        username="Demo",
    )

    slowmo_bird_comment2=Comment(
        userId=2,
        projectId=6,
        comment="""
                    Well thought out project and instruct-able, thank you for posting.
                    Did you try a video or two?
                    I may try this setup using my trail cameras as I don't have a camera like yours.
                """,
        username="marnie",
    )

    slowmo_bird_comment3=Comment(
        userId=3,
        projectId=6,
        comment="""
                    Fantastic work. I can not wait to try it out and see the results, thank you very much.
                """,
        username="bobbie",
    )

    dragonfly1=Comment(
        userId=1,
        projectId=7,
        comment="""
                    This is fun!
                    Do you have a link to the Tinkercad design for those who want to download or customize one?
                """,
        username="Demo",
    )

    dragonfly2=Comment(
        userId=2,
        projectId=7,
        comment="""
                    This is a great little project, nice work!

                    That last photo would make an excellent cover image, if you're inclined to edit. That would help this get some more clicks I think! : )
                """,
        username="marnie",
    )

    db.session.add(bird_house_comment1)
    db.session.add(bird_house_comment2)
    db.session.add(casino_clock_comment1)
    db.session.add(casino_clock_comment2)
    db.session.add(one_board_mug_comment1)
    db.session.add(one_board_mug_comment2)
    db.session.add(james_webb_comment1)
    db.session.add(james_webb_comment2)
    db.session.add(james_webb_comment3)
    db.session.add(slowmo_bird_comment1)
    db.session.add(slowmo_bird_comment2)
    db.session.add(slowmo_bird_comment3)
    db.session.add(dragonfly1)
    db.session.add(dragonfly2)


    db.session.commit()


def undo_comments():
    db.session.execute('TRUNCATE comments RESTART IDENTITY CASCADE')
    db.session.commit()