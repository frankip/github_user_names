from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class UserForm(FlaskForm):
    user_name = StringField('Search user',validators=[Required()])
    