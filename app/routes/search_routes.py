from flask import Blueprint
from app.models.supply import Supply
from app.models.project import Project
from app.models.instruction import Instruction


search_bp = Blueprint('search', __name__)

@search_bp.route('/<searchKeyWord>')
def searchResults(searchKeyWord):
    project_by_name = Project.query.filter(Project.title.ilike(f'%{searchKeyWord}%')).all()
    name_list = [recipe.to_dict() for recipe in project_by_name]
    project_by_supply = Project.query.join(Supply).filter(Supply.supply.ilike(f'%{searchKeyWord}%')).all()
    supply_list = [project.to_dict() for project in project_by_supply]
    project_by_instruction = Project.query.join(Instruction).filter(Instruction.instructions.ilike(f'%{searchKeyWord}%')).all()
    instruction_list = [project.to_dict() for project in project_by_instruction]
    project_set = set()
    project_list = [*name_list, *supply_list, *instruction_list]
    for project in project_list:
        project_set.add(project['id'])
    project1_list = []
    for id in project_set:
        project1_list.append(Project.query.get(id).to_dict())

    return {
        'projects': project1_list

    }