# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired
from wtforms import TextAreaField

class UploadForm(FlaskForm):
    img = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])
    description = TextAreaField('Description', validators=[DataRequired()])