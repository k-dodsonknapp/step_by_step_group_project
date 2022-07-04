from app.models import db, Favorite

def seed_favorites():
    project1_favorite = Favorite(
        projectId=1,
        userId=1,
    )

    project_favorite2 = Favorite(
        projectId=1,
        userId=2,
    )

    db.session.add(project1_favorite)
    db.session.add(project_favorite2)

    db.session.commit()

def undo_favorites():
    db.session.execute('TRUNCATE favorites RESTART IDENTITY CASCADE;')
    db.session.commit()