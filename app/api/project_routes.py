from dis import Instruction
from flask import Blueprint
from app.models import Project, Instruction, Supply, Comment, User

project_routes = Blueprint('projects', __name__)


@project_routes.route('/')
def projects():
    projects = Project.query.all()
    return {'projects': [project.to_dict() for project in projects]}


@project_routes.route('/<int:id>')
def project(id):
    project = Project.query.get(id).to_dict()
    # project = project.to_dict()
    owner = User.query.filter(User.id == project.userId).first()
    supplies = Supply.query.filter(Supply.projectId == id).all()
    instructions = Instruction.query.filter(Instruction.projectId == id).all()
    comments = Comment.query.filter(Comment.projectId == id).all()

    return {'project': {
        'title': project.title,
        'owner': owner.to_dict(),
        'overview': project.overview,
        'supplies': [supply.to_dict() for supply in supplies],
        'instructions': [instruction.to_dict() for instruction in instructions],
        'comments': [comment.to_dict() for comment in comments]
    }}


@project_routes.route('/:category')
def projects_by_category(category):
    projects = Project.query.filter(Project.category == category)
    return {'projects': [project.to_dict() for project in projects]}
