from app.models import db, Instruction

def instruction_seed():

    bird_project1= Instruction(
        projectId=1,
        stepOrder=1
    )