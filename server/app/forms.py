from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, InputRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class TeamForm(FlaskForm):
    team_name = StringField('Team Name', validators=[DataRequired()])
    team_captain = StringField('Team Captain', validators=[DataRequired()])
    points = IntegerField('Points (so far)', validators=[InputRequired()])


class SelectTeamForm(FlaskForm):
    selected_team = SelectField('Selected Team', validators=[DataRequired()])


class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
