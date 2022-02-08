from flask_wtf import FlaskForm
from wtforms import StringField, TextField
from wtforms.validators import DataRequired


class ProjectForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    titleImage = TextField('titleImage', validators=[DataRequired()])
    overview = TextField('overview', validators=[DataRequired()])
    category = StringField('category', validators=[DataRequired()])
