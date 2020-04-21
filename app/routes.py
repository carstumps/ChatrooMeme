from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, ChangePasswordForm, \
    NewProfileForm, CreatePostForm, EditBioForm

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
        'topic': 'Big Cats',
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

topics = '''Food
Exercise
Love
Big Cats
Cars
Elvis
Video Games
Juices'''.split('\n')

current_user = 'Joe Exotic'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Topic',
                           current_user=current_user,
                           topics=topics)


# The following components deal with profiles and their information

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',
                           title='Sign In',
                           form=form)


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
    for iter_user in users:
        if iter_user['username'] is current_user:
            user = iter_user
    return render_template('profile.html',
                           title='Profile - {}'.format(current_user),
                           user=user,
                           form=form)


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
