from .auth_routes import auth_bp
from .comment_routes import comment_bp
from .image_route import image_bp
from .instructions import instruction_bp
from .project_routes import project_bp
from .search_routes import search_bp
from .user_routes import user_bp
from .views import views_bp
from .frontend_routes import frontend_bp

# Expose blueprints for use elsewhere
__all__ = [
    "auth_bp",
    "comment_bp",
    "image_bp",
    "instruction_bp",
    "project_bp",
    "search_bp",
    "user_bp",
    "views_bp",
    "frontend_bp"
]