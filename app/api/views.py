from flask import Blueprint, request
from app.models import db
from app.models.views import Views

views_routes = Blueprint('views', __name__)

@views_routes.route('/')
def get_all_views():
    views = Views.query.all()

    return {'views': [view.to_dict() for view in views]}

@views_routes.route('/<int:id>')
def get_project_views(id):
    view = Views.query.filter(Views.projectId == id).first()
    return view.to_dict()

@views_routes.route('/new', methods=["POST"])
def create_views():
    data = request.json

    projectId = data["projectId"]
    viewCount = data['viewCount']

    new_view = Views(
        projectId=projectId,
        viewCount=viewCount,
    )
    db.session.add(new_view)
    db.session.commit()

    return new_view.to_dict()

@views_routes.route('/add', methods=["PUT"])
def update_views():
    data = request.json
    projectId = data["projectId"]["projectId"]

    view = Views.query.filter(projectId == Views.projectId).first()
    view.viewCount+=1
    db.session.commit()

    return {}