from app.models import db, Favorite

def seed_favorites():
    project1_favorite = Favorite(
        projectId=1,
        userId=1,
    )

    db.session.add(project1_favorite)

    db.session.commit()

def undo_favorites():
    db.session.execute('TRUNCATE favorites RESTART IDENTITY CASCADE;')
    db.session.commit()