from flask import Blueprint, request
from app.models.db import db
from app.models.user import User
from app.forms import LoginForm
# from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user
import base64
from io import BytesIO


auth_bp = Blueprint('auth', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@auth_bp.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}


@auth_bp.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    form.csrf_token.data = request.cookies.get('csrf_token')  # Avoid key error if missing
    
    if form.validate_on_submit():
        user = User.query.filter(User.email == form.data['email']).first()
        try:
            photo_data = base64.b64encode(user.userPhoto)
            photo_file = BytesIO(photo_data)
            photo_file.seek(0)
        except Exception as e:
            return {'error': f'Error decoding photo: {str(e)}'}, 500
        
        login_user(user)
        return user.to_dict()
    
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_bp.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


def encode_image(user_photo):
    try:
        user_photo = base64.b64decode(user_photo)
        return user_photo
    except Exception as e:
        return {'Error': 'Unable to upload photo'}, 500
    
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

@auth_bp.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    # form = SignUpForm()
    form = None
    data = request.data
    # print(request.files['user'])
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    userPhoto = request.files.get('userPhoto')

    # form['csrf_token'].data = request.cookies['csrf_token']
    # if form.validate_on_submit():
    encoded_image = encode_image(userPhoto.read())
    print("Encoded Image:", encoded_image)
    user = User(
        username=username,
        email=email,
        password=password,
        userPhoto=encoded_image,
    )
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return user.to_dict()
    # return {'errors': validation_errors_to_error_messages(form.errors)}, 401


# @auth_bp.route('/signup', methods=['POST'])
# def sign_up():
#     """
#     Creates a new user and logs them in
#     """
#     form = request.json
#     print(form, "COOKIESSSS")
    # form['csrf_token'].data = request.cookies['csrf_token']
    # if True:
    #     encoded_image = encode_image(form.data['userPhoto'])
    #     user = User(
    #         username=form.data['username'],
    #         email=form.data['email'],
    #         password=form.data['password'],
    #         userPhoto=encoded_image,
    #     )
    #     db.session.add(user)
    #     db.session.commit()
    #     login_user(user)
    #     return user.to_dict()
    # return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_bp.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
