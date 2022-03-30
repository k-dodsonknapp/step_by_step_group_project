from dis import Instruction
from flask import Blueprint, request
from sqlalchemy import insert, update
from app.models import db, Project, Instruction, Supply, Comment, User
from app.forms.project_form import ProjectForm

project_routes = Blueprint('projects', __name__)


@project_routes.route('/')
def projects():
    projects = Project.query.all()
    list = [project.to_dict() for project in projects]

    for project in list:
        id = project["userId"]
        username = User.query.get(id).to_dict()["username"]
        project["username"] = username

    return {"projects": list}


@project_routes.route('/<int:id>')
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


@project_routes.route('/<int:id>', methods=['PUT'])
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

@project_routes.route('/<int:id>', methods=['DELETE'])
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

    project = Project.query.get(id)
    db.session.delete(project)
    db.session.commit()

    return {'message': 'success'}


@project_routes.route('/new', methods=['POST'])
def create_project():
    data = request.json
    instructions = data['instructions']
    supplies = data['supplies']
    print("JJJJJJJJJ", supplies)

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


@project_routes.route('/<category>')
def projects_by_category(category):
    projects = Project.query.filter(Project.category == category)
    return {'projects': [project.to_dict() for project in projects]}
