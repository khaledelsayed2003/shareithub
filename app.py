from flask import Flask, render_template,url_for

app = Flask(__name__)

posts = [
    {
        'author':"Khaled Elsayed",
        'title': "Python post!",
        'content': "Flask is a lightweight Python web framework that helps you build websites and web applications easily.",
        'date_posted': "December 12, 2025"
    },
    {
        'author':"Jane Schafer",
        'title': "Git post!",
        'content': "VCS stands for Version Control System",
        'date_posted': "December 13, 2025"
    },
    
]



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == "__main__":
    app.run(debug=True)
    
    