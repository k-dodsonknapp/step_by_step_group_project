from flask import Blueprint, request
# from sqlalchemy import 
from app.models import db, Instruction


instruction_routes = Blueprint('instructions', __name__)

@instruction_routes.route('/<int:id>/update', methods=["PUT"])
def update_instructions(id):
    data = request.json
    # projectId = data['projectId'] 
    print("LLLLLLLLLLLL", data)

    instructions = Instruction.query.filter(Instruction.projectId == id).all()
    
    print("KKKKKKKKKK", instructions)

    for instruction in instructions:
        row = Instruction(
            projectId=instruction['projectId'],
            stepOrder=instruction["stepOrder"],
            stepTitle=instruction["stepTitle"],
            instructions=instruction["instructions"],
            photoUrl=instruction["photoUrl"],
            videoUrl=instruction["videoUrl"],
        )
        db.session.add(row)
    db.session.commit()
    return {"message": "success"}