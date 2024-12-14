from . import (
    auth_bp,
    comment_bp,
    # favorite_bp,
    image_bp,
    instruction_bp,
    project_bp,
    search_bp,
    user_bp,
    views_bp,
    frontend_bp,
)

def register_routes(app):
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(project_bp, url_prefix='/api/projects')
    app.register_blueprint(comment_bp, url_prefix='/api/comments')
    app.register_blueprint(search_bp, url_prefix='/api/search')
    app.register_blueprint(image_bp, url_prefix='/api/images')
    app.register_blueprint(instruction_bp, url_prefix='/api/instructions')
    app.register_blueprint(views_bp, url_prefix='/api/views')
    # app.register_blueprint(favorite_bp, url_prefix='/api/favorite')
    app.register_blueprint(frontend_bp)