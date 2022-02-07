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

    db.session.add(bird_house)
    db.session.commit()

def undo_project_seeders():
    db.session.execute('TRUNCATE projects RESTART IDENTITY CASCADE;')
    db.session.commit()

