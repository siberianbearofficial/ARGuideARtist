from flask import Flask, render_template
from emulate_db_response import get_photos_from_db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World my test file'


@app.route('/test')
def test_func():
    return render_template('gallery.html')


@app.route('/get_gallery_photos')
def get_gallery_photos():
    return get_photos_from_db()


if __name__ == '__main__':
    app.run()
