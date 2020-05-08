from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, \
    BooleanField, SubmitField, TextAreaField, \
    FileField, SelectField
from wtforms.validators import DataRequired, InputRequired, \
    EqualTo, Email, ValidationError
from app.models import User

# The following component deals with creating a new post or comment

t = '''[Choose Topic]
Food
Exercise
Love
Big Cats
Cars
Elvis
Video Games
Juices'''.split('\n')

c = [(i + 1, t[i]) for i in range(len(t))]


class CreatePostForm(FlaskForm):
    topic = SelectField('Choose a topic', validators=[DataRequired()], choices=c)
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Post', validators=[DataRequired()])
    image = FileField('Add an image')
    submit = SubmitField('Submit')


class CreateCommentForm(FlaskForm):
    text = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Submit')


# The following components deal with profiles and their information


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


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


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
