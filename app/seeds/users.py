from app.models.db import db
from app.models.user import User
import os


environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# Adds a demo user, you can add other users here if you want
def seed_users():
    users = [
        User(
            username='Demo', 
            email='demo@aa.io', 
            password='password',
            userPhoto="https://content.instructables.com/ORIG/FKD/JFBJ/IGTYAVRR/FKDJFBJIGTYAVRR.jpg?auto=webp&frame=1&width=300&fit=bounds&md=8e63dc008e0fe12bc802cdf742fd0085",
        ),
        User(
            username='marnie', 
            email='marnie@aa.io', 
            password='password',
            userPhoto="https://www.dogfoodadvisor.com/wp-content/uploads/2019/10/Puppy-for-DFA-Dog-Food-Recall-Card-500x333.jpg",
        ),
        User(
            username='bobbie', 
            email='bobbie@aa.io', 
            password='password',
            userPhoto="https://www.cesarsway.com/wp-content/uploads/2019/10/AdobeStock_190562703-768x535.jpeg.webp"
        ),
        User(
            username="Daphne", 
            email="daphne@mail.io", 
            password='password',
            userPhoto="https://ggsc.s3.amazonaws.com/images/made/images/uploads/The_Science-Backed_Benefits_of_Being_a_Dog_Owner_300_200_int_c1-1x.jpg"
        ),
        User(
            username="Moose", 
            email="moose@mail.io", 
            password='password',
            userPhoto="https://cdn-prod.medicalnewstoday.com/content/images/articles/322/322868/golden-retriever-puppy.jpg"
        ),
        User(
            username="Barry", 
            email="barry@mail.io", 
            password='password',
            userPhoto="https://images.newscientist.com/wp-content/uploads/2022/04/05152010/SEI_97255351.jpg?width=800"
        )
    ]

    for user in users:
        print(user.username)

        # Only encode if userPhoto is a string
        if user.userPhoto and isinstance(user.userPhoto, str):
            user.userPhoto = user.userPhoto.encode("utf-8")

        db.session.add(user)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")

    db.session.execute("SELECT setval(pg_get_serial_sequence('users', 'id'), 1, false);")
    db.session.commit()