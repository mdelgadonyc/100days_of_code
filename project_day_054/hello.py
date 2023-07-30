# DAY 54 Exercise: Deco-Demo

from flask import Flask

app = Flask(__name__)


def make_italic(function):
    def add_italic(name):
        return f'<em> {function(name)} </em>'

    return add_italic


def make_underlined(function):
    def add_underlined(name):
        return f'<u> {function(name)} </u>'

    return add_underlined


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/username/<name>')
@make_italic
@make_underlined
def greet(name):
    return (f'<h1>Hi {name}! Welcome to my website!</h1>'
            f'<img src="https://media3.giphy.com/media/ASd0Ukj0y3qMM/giphy.gif" width="480" height="360">')


if __name__ == "__main__":
    app.run(debug=True)
