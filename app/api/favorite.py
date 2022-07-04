from flask import Blueprint, Request, request
from app.models import db
from app.models.favorite import Favorite

favorite_routes = Blueprint("favorite", __name__)

@favorite_routes.route('/')
def get_all_favorites():
    favorites = Favorite.query.all()

    return {"favorite": [favorite.to_dict() for favorite in favorites]}

@favorite_routes.route('/<int:id>')
def get_one_projects_favorites(id):
    favorites = Favorite.query.filter(Favorite.projectId == id).all()
    return {"favorite": [favorite.to_dict() for favorite in favorites]}
    

@favorite_routes.route('/add', methods=["POST"])
def add_favorite():
    data = request.json

    userId = data["userId"]
    projectId = data["projectId"]

    new_favorite = Favorite(
        userId = userId,
        projectId = projectId
    )

    db.session.add(new_favorite)
    db.session.commit()

    return new_favorite.to_dict()

@favorite_routes.route("/delete", methods=["DELETE"])
def delete_favorite():
    data = request.json
    id = data["id"]

    favorite = Favorite.query.get(id)
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
    return {"message": "Delete Successful"}