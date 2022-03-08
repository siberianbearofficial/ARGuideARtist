from flask import Flask, render_template
import config
from emulate_db_response import get_photos_from_db
from data import db_session
from one import get_markers, get_routs, get_navigations


db_session.global_init("db/argid.sqlite")
app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    markers = get_markers()
    routs = get_routs()
    navigations = get_navigations()
    print(markers)
    print(routs)
    print(navigations)
    return 'Hello World my test file'


@app.route('/test')
def test_func():
    return render_template('gallery.html')


@app.route('/photo_booth')
def photo_booth():
    return render_template('photo_booth.html')


@app.route('/get_gallery_photos')
def get_gallery_photos():
    return get_photos_from_db()


if __name__ == '__main__':
    app.run()
