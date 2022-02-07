from app.models import db, Instruction

def instruction_seed():

    bird_project1= Instruction(
        projectId=1,
        stepOrder=1,
        instructions="Gather your materials", 
        photoUrl="Picture of materials", 
        videoUrl="Video of materials"
    )

    bird_project2= Instruction(
        projectId=1,
        stepOrder=2,
        instructions="Take two pieces of wood and use wood glue put the two together", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action"
    )

    bird_project3= Instruction(
        projectId=1,
        stepOrder=3,
        instructions="Repeat step 2 with the last two pieces of the square", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action"
    )

    bird_project4= Instruction(
        projectId=1,
        stepOrder=4,
        instructions="Add roof", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action"
    )

    bird_project5= Instruction(
        projectId=1,
        stepOrder=5,
        instructions="Add shingles to roof", 
        photoUrl="Picture of wood pieces and glue", 
        videoUrl="Video of the action"
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