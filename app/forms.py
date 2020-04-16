from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, FileField, FieldList
from wtforms.validators import DataRequired, InputRequired, EqualTo


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class CreatePostForm(FlaskForm):
    topic = FieldList('Choose a topic')
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Post', validators=[DataRequired()])
    image = FileField('Add an image')
    submit = SubmitField('Submit')


class ChangePasswordForm(FlaskForm):
    password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Change')


class EditBioForm(FlaskForm):
    bio = TextAreaField("Edit Bio")
    submit = SubmitField('Submit')


class NewProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    bio = TextAreaField("Add a bio (you can change this any time)")
    password = PasswordField('Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password')
    submit = SubmitField('Submit')
