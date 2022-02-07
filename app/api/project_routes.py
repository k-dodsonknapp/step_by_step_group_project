from dis import Instruction
from flask import Blueprint
from app.models import Project, Instruction, Supply, Commnet

project_routes = Blueprint('projects', __name__)


@project_routes.route('/')
def projects():
    projects = Project.query.all()
    return {'projects': [project.to_dict() for project in projects]}


@project_routes.route('/<int:id>')
def project(id):
    project = Project.query.get(id)
    instructions = Instruction.query.filter(Instruction.projectId == id)
    supplies = Su
    return project.to_dict()


@project_routes.route('/:category')
def projects_by_category(category):
    projects = Project.query.filter(Project.category == category)
    return {'projects': [project.to_dict() for project in projects]}
