from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, ValidationError


class KahootSmashForm(FlaskForm):
    pin = StringField('Game PIN', validators=[DataRequired()])
    numBots = IntegerField('Number of Bots', validators=[DataRequired()])
    baseName = StringField('Name of Bots', validators=[DataRequired()])
    submit = SubmitField('Slam Game!')
