from flask import Blueprint, request
from app.models import db

views_bp = Blueprint('views', __name__)

@views_bp.route('/add', methods=["PUT"])
def update_views():
    data = request.json
    # projectId = data["projectId"]["projectId"]

    # view = Views.query.filter(projectId == Views.projectId).first()
    # view.viewCount+=1
    # db.session.commit()
    print("VIEW DATA:", data)

    return {"DATA": data}