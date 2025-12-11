from flask import Flask

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Welcome to my ShareItHub website!'

if __name__ == "__main__":
    app.run(debug=True)
    
    