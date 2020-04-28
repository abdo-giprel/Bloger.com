from flask import Flask, escape, request, render_template as view,url_for

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)
