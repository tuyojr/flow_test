# a very simple python app that uses Flask to create a web server
# and returns a simple message when the root URL is accessed

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to this simple python app created using Flask."

@app.route('/about')
def about():
    return "This is a simple web app created using Flask."

@app.route('/contact')
def contact():
    return "You can email me at: olutuyod@outlook.com"


if __name__ == '__main__':
    app.run(debug=True)