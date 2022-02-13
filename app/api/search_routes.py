from flask import Blueprint
from app.models import Supply, Project, Instruction


search_routes = Blueprint('search', __name__)


@search_routes.route('/<searchKeyWord>')
def searchResults(searchKeyWord):
    print('fetch req sent to backend' )
    project_by_name = Project.query.filter(Project.title.ilike(f'%{searchKeyWord}%')).all()
    # print('-----------', project_by_name)
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