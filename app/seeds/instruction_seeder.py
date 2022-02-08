from app.models import db, Instruction

def seed_instructions():

    bird_project1= Instruction(
        projectId=1,
        stepOrder=1,
        stepTitle="Get materials",
        instructions="Gather your materials", 
        photoUrl="https://imgprd19.hobbylobby.com/2/0e/4f/20e4f0a77628cacbbbb622fb4a01f7728b821d88/350Wx350H-116392-1019-px.jpg", 
        videoUrl="Video of materials"
    )

    bird_project2= Instruction(
        projectId=1,
        stepOrder=2,
        stepTitle="Start square",
        instructions="Take two pieces of wood and use wood glue put the two together", 
        photoUrl="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSbYADPGL1BShmV9Nw9K12GCVu5SAR1pZ_0cBKV9AYyaakIoj-rZMdQF2cDIkWaM15sIGA&usqp=CAU", 
        videoUrl="Video of the action"
    )

    bird_project3= Instruction(
        projectId=1,
        stepOrder=3,
        stepTitle="Add rest of square",
        instructions="Repeat step 2 with the last two pieces of the square", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action"
    )

    bird_project4= Instruction(
        projectId=1,
        stepOrder=4,
        stepTitle="Add Roof",
        instructions="Add roof", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action"
    )

    bird_project5= Instruction(
        projectId=1,
        stepOrder=5,
        stepTitle="Add Shingles",
        instructions="Add shingles to roof", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action"
    )

    casino_clock1=Instruction(
        projectId=2,
        stepOrder=1,
        instructions=""
    )
    
    db.session.add(bird_project1)
    db.session.add(bird_project2)
    db.session.add(bird_project3)
    db.session.add(bird_project4)
    db.session.add(bird_project5)

    db.session.commit()


def undo_instructions():
    db.session.execute('TRUNCATE instructions RESTART IDENTITY CASCADE;')
    db.session.commit()