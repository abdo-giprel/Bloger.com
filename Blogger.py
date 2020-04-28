from flask import Flask, escape, request, render_template as view,url_for,flash,redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '6dc87ef97b330819078b05a81754c06c'

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


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('home'))
    return view('register.html',title='Register',form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return view('login.html',title='Login',form=form)


if __name__ == '__main__':
    app.run(debug=True)
