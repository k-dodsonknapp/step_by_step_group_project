# from flask import Blueprint, request
# from app.models import db
# from app.models.favorite import Favorite

# favorite_bp = Blueprint("favorite", __name__)

# @favorite_bp.route('/')
# def get_all_favorites():
#     favorites = db.session.query(Favorite).all()
#     # Explicitly remove the session to return the connection
#     db.session.remove()

#     return {"favorite": [favorite.to_dict() for favorite in favorites]}

# @favorite_bp.route('/<int:id>')
# def get_one_projects_favorites(id):
#     favorites = db.session.query(Favorite.projectId == id).all()
#     db.session.remove()
#     return {"favorite": [favorite.to_dict() for favorite in favorites]}
    

# @favorite_bp.route('/add', methods=["POST"])
# def add_favorite():
#     data = request.json

#     userId = data["userId"]
#     projectId = data["projectId"]

#     new_favorite = Favorite(
#         userId = userId,
#         projectId = projectId
#     )

#     db.session.add(new_favorite)
#     db.session.commit()

#     return new_favorite.to_dict()
#     # return {}

# @favorite_bp.route("/delete", methods=["DELETE"])
# def delete_favorite():
#     data = request.json
#     id = data["id"]

#     favorite = Favorite.query.get(id)
#     if favorite:
#         db.session.delete(favorite)
#         db.session.commit()
#     return {"message": "Delete Successful"}