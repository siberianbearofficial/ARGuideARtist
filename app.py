from flask import Flask, render_template
import config
from emulate_db_response import get_photos_from_db
from data import db_session
db_session.global_init("db/argid.sqlite")
app = Flask(__name__)
app.config.from_object(config)

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
