from flask import Flask, render_template,url_for,flash,redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
from dotenv import load_dotenv
from pathlib import Path
import os


app = Flask(__name__)

# Load the .env file from the config folder
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / "config" / ".env")
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database creation
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # I will add the default image later.
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"




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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created successfully for {form.username.data}✅", "success")
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'khaled.elsayed2206@gmail.com' and form.password.data == 'password':
            flash(f"🎉 You have been successfully logged in!", "success")
            return redirect(url_for('home'))
        else:
            flash("❌ Login failed! Please check your email and password.", "danger")
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
    
    