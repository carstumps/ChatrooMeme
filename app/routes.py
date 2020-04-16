from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, ChangePasswordForm, NewProfileForm, CreatePostForm, EditBioForm

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

topics = ['Big Cats', 'Food']

current_user = 'Joe Exotic'


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Topic',
                           topics=topics)


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    form = CreatePostForm()
    if form.validate_on_submit():
        '''
        posts.append({
            'username': current_user,
            'topic': form.topic.data,
            'title': form.title.data,
            'text': form.text.data,
            'image': form.image.data,
            'comments': []
        })
        '''
        redirect(url_for('profile'))
    return render_template('profile.html',
                           title=current_user,
                           current_user=current_user,
                           form=form)


@app.route('/new_profile', methods=['GET', 'POST'])
def new_profile():
    # complete
    form = NewProfileForm()
    if form.validate_on_submit():
        '''
        for user in users:
            if form.username == user['username']:
                return redirect(url_for('new_profile'))
        users.append({
            'username': form.username.data,
            'password': form.password.data,
            'bio': form.bio.data
        })
        '''
        return redirect(url_for('profile'))
    return render_template('new_profile.html',
                           title='New Profile',
                           form=form)


@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    # complete
    form = ChangePasswordForm()
    if form.validate_on_submit():
        '''
        for user in users:
            if user['username'] == current_user:
                user['password'] = form.password.data
                '''
        return redirect(url_for('profile'))
    return render_template('change_password.html',
                           title='Change Password',
                           form=form)


@app.route('/edit_bio', methods=['GET', 'POST'])
def edit_bio():
    # complete
    form = EditBioForm()
    if form.validate_on_submit():
        '''
        for user in users:
            if user['username'] == current_user:
                user['password'] = form.bio.data
        '''
        return redirect(url_for('profile'))
    return render_template('change_password.html',
                           title='Change Password',
                           form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # complete
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me = {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('profile'))
    return render_template('login.html',
                           title='Sign In',
                           form=form)
