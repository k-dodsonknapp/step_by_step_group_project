from flask import Blueprint, request
from app.models import db
from app.models.favorite import Favorite

favorite_routes = Blueprint("favorite", __name__)

@favorite_routes.route('/')
def get_all_views():
    favorites = Favorite.query.all()
    
    return {"favorite": [favorite.to_dict() for favorite in favorites]}