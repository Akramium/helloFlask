from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
def say_bye():
    return 'Bye!'


@app.route('/username/<name>/<int:id_int>/<path:path>')
def greet(name, id_int, path):
    return f'Hello, {name}! You have an ID of: {id_int}, You path is: {path}'


if __name__ == '__main__':
    app.run(debug=True)
