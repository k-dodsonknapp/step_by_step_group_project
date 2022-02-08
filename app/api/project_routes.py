from dis import Instruction
from flask import Blueprint, request
from app.models import Project, Instruction, Supply, Comment, User
from app.forms.project_form import ProjectForm

project_routes = Blueprint('projects', __name__)


@project_routes.route('/')
def projects():
    projects = Project.query.all()
    return {'projects': [project.to_dict() for project in projects]}


@project_routes.route('/<int:id>')
def project(id):
    project = Project.query.get(id).to_dict()
    owner = User.query.filter(User.id == project['userId']).first()
    supplies = Supply.query.filter(Supply.projectId == id).all()
    instructions = Instruction.query.filter(Instruction.projectId == id).all()
    comments = Comment.query.filter(Comment.projectId == id).all()

    return {'project': {
        'title': project['title'],
        'owner': owner.to_dict(),
        'overview': project['overview'],
        'supplies': [supply.to_dict() for supply in supplies],
        'instructions': [instruction.to_dict() for instruction in instructions],
        'comments': [comment.to_dict() for comment in comments]
    }}


@project_routes.route('/new', methods=['POST'])
def create_project():
    projectForm = ProjectForm()

    # print(projectForm['title'])
    projectForm['csrf_token'].data = request.cookies['csrf_token']
    if projectForm.validate_on_submit():
        print(projectForm.data['title'])
        return {'message': 'validated'}

    return {'message': 'Not validated'}

@project_routes.route('/<category>')
def projects_by_category(category):
    projects = Project.query.filter(Project.category == category)
    return {'projects': [project.to_dict() for project in projects]}
