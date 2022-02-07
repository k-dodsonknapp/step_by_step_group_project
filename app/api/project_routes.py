from flask import Blueprint
from app.models import Project

project_routes = Blueprint('project', __name__)


@project_routes.route('/')

def project():
    projects = Project.query.all()
    
