from flask import Blueprint, send_from_directory, current_app


frontend_bp = Blueprint('frontend', __name__)

# Serve React's index.html for frontend routes
@frontend_bp.route('/')
@frontend_bp.route('/<path:path>')
def catch_all(path=None):
    if path and path.startswith('api/'):  # Check if it's an API route
        return 'Not Found', 404
    return send_from_directory(app.static_folder, 'index.html')