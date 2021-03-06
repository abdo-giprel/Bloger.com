from flask import escape, request, render_template as view,url_for,flash,redirect
from blogger.forms import RegistrationForm, LoginForm
from blogger.models import User, Post
from blogger import app,db,bcrypt
from flask_login import login_user, current_user,logout_user,login_required


posts = [
    {
        'author':'ABDO giprel',
        'title': 'world',
        'content': 'first post content',
        'date_posted': 'April 21,2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return view('home.html',posts=posts)

@app.route('/about')
def about():
    return view('about.html',title='About')


@app.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user =User(username =form.username.data, email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account has bean created for {form.username.data}! You Can Login Now ','success')
        return redirect(url_for('login'))
    return view('register.html',title='Register',form=form)


@app.route('/login',methods=['POST','GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page =request.args.get('next')
            flash(f'Welcome {user.username}','success')
            return redirect (next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Unsuccess login! check email or password','danger')
    return view('login.html',title='Login',form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return view('account.html',title='Account')

