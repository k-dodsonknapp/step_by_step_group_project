# from flask_wtf import FlaskForm
# from wtforms import StringField, FileField
# from wtforms.validators import DataRequired, ValidationError
# from flask_wtf.file import FileAllowed
# from app.models.user import User
# from flask import session
# from PIL import Image
# import io


# def user_exists(form, field):
#     # Checking if user exists
#     email = field.data
#     user = User.query.filter(User.email == email).first()
#     if user:
#         raise ValidationError('Email address is already in use.')


# def username_exists(form, field):
#     # Checking if username is already in use
#     username = field.data
#     user = User.query.filter(User.username == username).first()
#     if user:
#         raise ValidationError('Username is already in use.')
    

# def valid_photo(form, field):
#     file_data = field.data
#     print(file_data, 'file_data')
#     if not file_data:
#         raise ValidationError("No file provided.")
    
#     try:
#         # Read the file and check if it's a valid image
#         file_data.seek(0)  # Reset file pointer
#         image = Image.open(io.BytesIO(file_data.read()))
#         image.verify()  # Verify the file is a valid image
#     except Exception:
#         raise ValidationError("Uploaded file is not a valid image.")



# class SignUpForm(FlaskForm):
#     username = StringField('username', validators=[DataRequired(), username_exists])
#     email = StringField('email', validators=[DataRequired(), user_exists])
#     password = StringField('password', validators=[DataRequired()])
#     userPhoto = FileField(
#         'userPhoto',
#         validators=[
#             FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!'),
#             valid_photo,
#         ]
#     )
