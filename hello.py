from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f'<b>{function()}</b>'

    return wrapper


def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'

    return wrapper


def make_underline(function):
    def wrapper():
        return f'<u>{function()}</u>'

    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/KAq5w47R9rmTuvWOWa/giphy.gif" width="200">'


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def say_bye():
    return 'Bye!'


@app.route('/username/<name>/<int:id_int>/<path:path>')
def greet(name, id_int, path):
    return f'Hello, {name}! You have an ID of: {id_int}, You path is: {path}'


if __name__ == '__main__':
    app.run(debug=True)
