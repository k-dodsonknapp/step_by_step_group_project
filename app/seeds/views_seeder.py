from app.models import db, Views

def seed_views():
    project1=Views(
        projectId=1,
        viewCount=0,
    )
    project2=Views(
        projectId=2,
        viewCount=0,
    )
    project3=Views(
        projectId=3,
        viewCount=0,
    )
    project4=Views(
        projectId=4,
        viewCount=0,
    )
    project5=Views(
        projectId=5,
        viewCount=0,
    )
    project6=Views(
        projectId=6,
        viewCount=0,
    )
    project7=Views(
        projectId=7,
        viewCount=0,
    )
    project8=Views(
        projectId=8,
        viewCount=0,
    )

    project9=Views(
        projectId=9,
        viewCount=0,
    )

    project10=Views(
        projectId=10,
        viewCount=0,
    )

    project11=Views(
        projectId=11,
        viewCount=0,
    )

    project12=Views(
        projectId=12,
        viewCount=0,
    )

    project13=Views(
        projectId=13,
        viewCount=0,
    )
    
    project14=Views(
        projectId=14,
        viewCount=0,
    )

    db.session.add(project1)
    db.session.add(project2)
    db.session.add(project3)
    db.session.add(project4)
    db.session.add(project5)
    db.session.add(project6)
    db.session.add(project7)
    db.session.add(project8)
    db.session.add(project9)
    db.session.add(project10)
    db.session.add(project11)
    db.session.add(project12)
    db.session.add(project13)
    db.session.add(project14)


    db.session.commit()

def undo_views():
    db.session.execute('TRUNCATE views RESTART IDENTITY CASCADE;')
    db.session.commit()