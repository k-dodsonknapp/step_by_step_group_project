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

    project15=Views(
        projectId=15,
        viewCount=0,
    )

    project16=Views(
        projectId=16,
        viewCount=0,
    )

    project17=Views(
        projectId=17,
        viewCount=0,
    )    
    
    project18=Views(
        projectId=18,
        viewCount=0,
    )

    project19=Views(
        projectId=19,
        viewCount=0,
    )

    project20=Views(
        projectId=20,
        viewCount=0,
    )

    project21=Views(
        projectId=21,
        viewCount=0,
    )

    project22=Views(
        projectId=22,
        viewCount=0,
    )

    project23=Views(
        projectId=23,
        viewCount=0,
    )

    project24=Views(
        projectId=24,
        viewCount=0,
    )

    project25=Views(
        projectId=25,
        viewCount=0,
    )

    project26=Views(
        projectId=26,
        viewCount=0,
    )

    project27=Views(
        projectId=27,
        viewCount=0,
    )

    project28=Views(
        projectId=28,
        viewCount=0,
    )

    project29=Views(
        projectId=29,
        viewCount=0,
    ) 

    project30=Views(
        projectId=30,
        viewCount=0,
    ) 

    project31=Views(
        projectId=31,
        viewCount=0,
    ) 

    project32=Views(
        projectId=32,
        viewCount=0,
    ) 

    project33=Views(
        projectId=33,
        viewCount=0,
    ) 

    project34=Views(
        projectId=34,
        viewCount=0,
    ) 

    project35=Views(
        projectId=35,
        viewCount=0,
    ) 

    project36=Views(
        projectId=36,
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
    db.session.add(project15)
    db.session.add(project16)
    db.session.add(project17)
    db.session.add(project18)
    db.session.add(project19)
    db.session.add(project20)
    db.session.add(project21)
    db.session.add(project22)
    db.session.add(project23)
    db.session.add(project24)
    db.session.add(project25)
    db.session.add(project26)
    db.session.add(project27)
    db.session.add(project28)
    db.session.add(project29)
    db.session.add(project30)
    db.session.add(project31)
    db.session.add(project32)
    db.session.add(project33)
    db.session.add(project34)
    db.session.add(project35)
    db.session.add(project36)

    db.session.commit()

def undo_views():
    db.session.execute('TRUNCATE views RESTART IDENTITY CASCADE;')
    db.session.commit()