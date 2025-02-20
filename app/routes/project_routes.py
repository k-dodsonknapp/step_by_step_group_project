from dis import Instruction
from flask import Blueprint, request
from app.models.db import db
from app.models.project import Project
from app.models.supply import Supply
from app.models.comment import Comment
from app.models.user import User
from app.models.instruction import Instruction


project_bp = Blueprint('projects', __name__)

@project_bp.route('/')
def projects():
    projects = db.session.query(Project).all()
    db.session.remove()
    list = [project.to_dict() for project in projects]

    for project in list:
        id = project["userId"]
        user = User.query.get(id)
        print(user, 'USERINHERE')
        print(user.userPhoto)
    #     username = User.query.get(id).to_dict()["username"]
    #     project["username"] = username

    return {"projects": list}


@project_bp.route('/<int:id>')
def project(id):
    project = Project.query.get(id).to_dict()
    owner = User.query.filter(User.id == project['userId']).first()
    supplies = Supply.query.filter(Supply.projectId == id).all()
    instructions = Instruction.query.filter(Instruction.projectId == id).all()
    comments = Comment.query.filter(Comment.projectId == id).all()

    return {'project': {
        'projectId': id,
        'title': project['title'],
        'titleImage': project['titleImage'],
        'category': project['category'],
        'owner': owner.to_dict(),
        'overview': project['overview'],
        'supplies': [supply.to_dict() for supply in supplies],
        'instructions': [instruction.to_dict() for instruction in instructions],
        'comments': [comment.to_dict() for comment in comments]
    }}


@project_bp.route('/<int:id>', methods=['PUT'])
def update_project(id):
    data = request.json
    instructions = data['instructions']
    supplies = data['supplies']

    project = Project.query.get(id)
    project.title = data['title']
    project.titleImage = data['titleImage']
    project.overview = data['overview']
    project.category = data['category']

    projectInstructions = Instruction.query.filter(Instruction.projectId == id).all()
    for instruction in projectInstructions:
        db.session.delete(instruction)

    for instruction in instructions:
        row = Instruction(
            projectId=id,
            stepOrder=instruction["stepOrder"],
            stepTitle=instruction["stepTitle"],
            instructions=instruction["instructions"],
            photoUrl=instruction["photoUrl"],
            videoUrl=instruction["videoUrl"],
        )
        db.session.add(row)

    projectSupplies = Supply.query.filter(Supply.projectId == id).all()
    for supply in projectSupplies:
        db.session.delete(supply)

    for supply in supplies:
        row = Supply(projectId=id,
                    supply=supply['supply'],
                    amount=supply['amount'])
        db.session.add(row)
    db.session.commit()

    return {'message': 'success'}

@project_bp.route('/<int:id>', methods=['DELETE'])
def delete_project(id):

    projectInstructions = Instruction.query.filter(Instruction.projectId == id).all()
    for instruction in projectInstructions:
        db.session.delete(instruction)

    projectSupplies = Supply.query.filter(Supply.projectId == id).all()
    for supply in projectSupplies:
        db.session.delete(supply)

    projectComments = Comment.query.filter(Comment.projectId == id).all()
    for comment in projectComments:
        db.session.delete(comment)
    
    projectViews = Views.query.filter(Views.projectId == id).first()
    db.session.delete(projectViews)

    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()

    return {'message': 'success'}


@project_bp.route('/new', methods=['POST'])
def create_project():
    data = request.json
    instructions = data['instructions']
    supplies = data['supplies']

    project = Project(userId=data['userId'],
                      title=data['title'],
                      titleImage=data['titleImage'],
                      overview=data['overview'],
                      category=data['category'])

    db.session.add(project)
    db.session.commit()

    projectId = Project.query.order_by(Project.id.desc()).first().id

    for instruction in instructions:
        row = Instruction(projectId=projectId,
                          stepOrder=instruction['stepOrder'],
                          stepTitle=instruction['stepTitle'],
                          instructions=instruction['instructions'],
                          photoUrl=instruction['photoUrl'],
                          videoUrl=instruction['videoUrl'])
        db.session.add(row)
        db.session.commit()

    for supply in supplies:
        row = Supply(projectId=projectId,
                     supply=supply['supply'],
                     amount=supply['amount'])
        db.session.add(row)
        db.session.commit()

    return { 'projectId': projectId }


@project_bp.route('/<category>')
def projects_by_category(category):
    projects = Project.query.filter(Project.category == category)
    return {'projects': [project.to_dict() for project in projects]}


# @project_bp.route('/add/views', methods=["PUT"])
# def update_views():
#     data = request.json
#     print("VIEWS", data)
#     projectId = data["projectId"]["projectId"]

#     project = Project.query.filter(projectId == Project.projectId).first()
#     project.views += 1
#     db.session.commit()

#     return {}