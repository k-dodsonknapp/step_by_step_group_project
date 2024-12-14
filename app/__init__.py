import os
from flask_cors import CORS
from flask import Flask, request, redirect
from flask_wtf.csrf import generate_csrf
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

from app.models.user import User
from app.models.db import db
from .config import Config
from app.seeds import seed_commands
from app.routes.routes import register_routes


migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()

from dotenv import load_dotenv

load_dotenv()

def create_app(config_class=Config):
    static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../react-app/build")
    app = Flask(__name__, static_folder=static_folder, static_url_path='/')
    # app = Flask(__name__)
    CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": f"{os.getenv('CORS_ORIGIN')}"}})
    app.config.from_object(config_class)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Conditional CSRF Protection
    if os.environ.get('FLASK_ENV') != 'development':
        csrf.init_app(app)
    else:
        print("CSRF protection is disabled in development mode.")

    with app.app_context():
        db.create_all()  # Ensure tables are created
    import logging
    logging.basicConfig(level=logging.DEBUG)

    app.cli.add_command(seed_commands)

    login_manager.login_view = 'auth.unauthorized'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    register_routes(app)

    # Handle redirect to HTTPS in production
    @app.before_request
    def https_redirect():
        if os.environ.get('FLASK_ENV') == 'production':
            if request.headers.get('X-Forwarded-Proto') == 'http':
                url = request.url.replace('http://', 'https://', 1)
                return redirect(url, code=301)

    # Inject CSRF token for security
    @app.after_request
    def inject_csrf_token(response):
        response.set_cookie(
            'csrf_token',
            generate_csrf(),
            secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
            samesite='Strict' if os.environ.get('FLASK_ENV') == 'production' else None,
            httponly=True
        )
        
        return response
    
    return app
