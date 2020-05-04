from flask import escape, request, render_template as view,url_for,flash,redirect
from blogger.forms import RegistrationForm, LoginForm
from blogger.models import User, Post
from blogger import app
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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return view('register.html',title='Register',form=form)


@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data=="abdo@gamil.com" and form.password.data =="admin":
            flash(f'Welcome Back Mr {form.email.data}!','success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccess login! check email or password','danger')
    return view('login.html',title='Login',form=form)
