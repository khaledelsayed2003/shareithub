from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Welcome to my ShareItHub website!'

@app.route('/about')
def about_us():
    return 'ShareItHub is a multi-user blogging and social posting platform built with Python and Flask.'


if __name__ == "__main__":
    app.run(debug=True)
    
    