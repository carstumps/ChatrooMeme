from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, \
    BooleanField, SubmitField, TextAreaField, \
    FileField, SelectField
from wtforms.validators import DataRequired, InputRequired, \
    EqualTo, Required


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


t = '''Food
Excersise
Love
Big Cats
Cars
Elvis
Video Games
Juices
'''.split('\n')

c = [(i + 1, t[i]) for i in range(len(t))]


class CreatePostForm(FlaskForm):
    topic = SelectField('Choose a topic', validators=[DataRequired()], choices=c)
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Post', validators=[DataRequired()])
    image = FileField('Add an image')
    submit = SubmitField('Submit')


class ChangePasswordForm(FlaskForm):
    password = PasswordField('New Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Change')


class EditBioForm(FlaskForm):
    bio = TextAreaField("Edit Bio")
    submit = SubmitField('Submit')


class NewProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    bio = TextAreaField("Add a bio (you can change this any time)")
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Submit')
