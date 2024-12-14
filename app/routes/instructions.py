from flask import Blueprint, request
from app.models import db
from app.models.instruction import Instruction


instruction_bp = Blueprint('instructions', __name__)

@instruction_bp.route('/<int:id>/update', methods=["PUT"])
def update_instructions(id):
    data = request.json
    # projectId = data['projectId'] 

    instructions = Instruction.query.filter(Instruction.id == id).all()
    for instruction in instructions:
        db.session.delete(instruction)
    
    # for instruction in data:
    #     row = Instruction(
    #         projectId=instruction['projectId'],
    #         stepOrder=instruction["stepOrder"],
    #         stepTitle=instruction["stepTitle"],
    #         instructions=instruction["instructions"],
    #         photoUrl=instruction["photoUrl"],
    #         videoUrl=instruction["videoUrl"],
    #     )
    #     db.session.add(row)
    # db.session.commit()
    return {"message": "success"}