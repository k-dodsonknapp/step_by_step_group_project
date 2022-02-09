from flask import Blueprint
from app.models import Supply, Project, Instruction


search_routes = Blueprint('search', __name__)


@search_routes.route('/<searchBar>')
def searchResults(searchBar):
    project_by_name = Project.query.filter(Project.title.ilike(f'{searchBar}%'))
    name_list = [recipe.to_dict() for recipe in project_by_name]
    project_by_supply = Project.query.join(Supply).filter(Supply.name.ilike(f'{searchBar}%'))
    supply_list = [project.to_dict() for project in project_by_supply]
    project_by_instruction = Project.query.join(Instruction).filter(Instruction.info.ilike(f'{searchBar}%'))
    instruction_list = [project.to_dict() for project in project_by_instruction]
    return {
        'projects': [*name_list, *supply_list, *instruction_list]

    }
