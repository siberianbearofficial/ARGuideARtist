from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World my test file'


@app.route('/test')
def test_func():
    return 'Hello test'


if __name__ == '__main__':
    app.run()
