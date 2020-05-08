from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, ChangePasswordForm, \
    NewProfileForm, CreatePostForm, EditBioForm, \
    CreateCommentForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask import request
from werkzeug.urls import url_parse
from flask_login import login_required
from app import db
from app.forms import RegistrationForm

'''
users = [
    {
        'username': 'Joe Exotic',
        'password': 'orangejuice',
        'bio': 'It is really damp in here!'
    },
    {
        'username': 'Justin Dabberson',
        'password': 'leftiesRule',
        'bio': 'I love the beach!'
    }
]
'''
posts = [
    {
        'username': 'Justin Dabberson',
        'topic': 'Food',
        'title': 'I love Chicken',
        'text': 'I love chicken, it is oh so yummy in my tummy.',
        'image': '',
        'comments': [
            {
                'username': 'Joe Exotic',
                'text': 'Baby...'
            },
            {
                'username': 'Joe Exotic',
                'text': 'I eat tigers for breakfast!'
            }
        ]
    },
    {
        'username': 'Joe Exotic',
        'topic': 'Food',
        'title': 'I love big cats!',
        'text': 'Big Cats are sooo great... I love them too much!',
        'image': '',
        'comments': [
            {
                'username': 'Justin Dabberson',
                'text': 'Where did they all go?'
            },
            {
                'username': 'Joe Exotic',
                'text': 'To Jeff Lowe!! D:<'
            }
        ]
    }
]

data = {
    'username': 'Justin Dabberson',
    'topic': 'Food',
    'title': 'I love Chicken',
    'text': 'I love chicken, it is oh so yummy in my tummy.',
    'image': '',
    'comments': [
        {
            'username': 'Joe Exotic',
            'text': 'Baby...'
        },
        {
            'username': 'Joe Exotic',
            'text': 'I eat tigers for breakfast!'
        }
    ]
}


topics = '''Food
Exercise
Love
Big Cats
Cars
Elvis
Video Games
Juices'''.split('\n')

#current_user = 'Joe Exotic'

# The following components are part of the flow of the app


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html',
                           title='Topics',
                           posts=posts)


@app.route('/')
@app.route('/topic', methods=['GET', 'POST'])
def topic():
    form = CreatePostForm()
    return render_template('topic.html',
                           title='Topic',
                           posts=posts,
                           form=form)


@app.route('/')
@app.route('/post', methods=['GET', 'POST'])
def post():
    form = CreateCommentForm()
    return render_template('post.html',
                           title='Post',
                           data=data,
                           form=form)


# The following components deal with profiles and their information

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        #login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        #flash('Login requested for user {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
        #return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = CreatePostForm()
    if form.validate_on_submit():
        redirect(url_for('profile'))
    user = {
        'username': '',
        'password': '',
        'bio': ''
    }
    #for iter_user in users:
    #    if iter_user['username'] is current_user:
    #        user = iter_user
    #return render_template('profile.html',
    #                       title='Profile - {}'.format(current_user),
    #                       user=user,
    #                       form=form)


@app.route('/new_profile', methods=['GET', 'POST'])
def new_profile():
    form = NewProfileForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('new_profile.html',
                           title='New Profile',
                           form=form)


@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        return redirect(url_for('profile'))
    return render_template('change_password.html',
                           title='Change Password',
                           form=form)


@app.route('/edit_bio', methods=['GET', 'POST'])
def edit_bio():
    form = EditBioForm()
    if form.validate_on_submit():
        return redirect(url_for('profile'))
    return render_template('edit_bio.html',
                           title='Change Password',
                           form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)