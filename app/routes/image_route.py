import os
from flask import Blueprint, request
from werkzeug.utils import secure_filename
from app.models import User

import psycopg2

image_bp = Blueprint("images", __name__)

# @image_bp.route("", methods=["POST"])
# # @login_required
# def upload_image():
#     if "image" not in request.files:
#         return {"errors": "image required"}, 400

#     image = request.files["image"]

#     if not allowed_file(image.filename):
#         return {"errors": "file type not permitted"}, 400
    
#     image.filename = get_unique_filename(image.filename)

#     upload = upload_file_to_s3(image)

#     if "url" not in upload:
#         # if the dictionary doesn't have a url key
#         # it means that there was an error when we tried to upload
#         # so we send back that error message
#         print('helllllo')
#         return upload, 400

#     url = upload["url"]
#     # flask_login allows us to get the current user from the request
#     # new_image = Image(user=current_user, url=url)
#     # db.session.add(new_image)
#     # db.session.commit()
#     return {"url": url}

@image_bp.route("", methods=["POST"])
def upload_image():

    print(request.files, 'hellow')
    print(request.files.get('image'))

    try:        
        file = request.files.get('image')
        user_id = request.form.get('userId')
        user = User.query.get(user_id)
    except Exception as e:
        return {"error": f"File not uploaded {e}"}
    # user = User.query.get('userId')

    # if file:
    #     filename = secure_filename(file.filename)
    #     user
    return {}, 200