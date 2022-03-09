from flask import Flask, render_template
import config
from emulate_db_response import get_photos_from_db
from data import db_session
from one import get_markers, get_routs, get_navigations, get_navigation_r, get_naprav, get_marsh


db_session.global_init("db/argid.sqlite")
app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    markers = get_markers()
    routs = get_routs()
    navigations = get_navigations()
    navigations_r = get_navigation_r()
    print(markers)
    print(routs)
    print(navigations)
    print(navigations_r)
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

@app.route('/navigation/<A>/<B>')
def navigation(A, B):
    return get_naprav(int(A), int(B))

@app.route('/marsh')
def marsh():
    return get_marsh()

if __name__ == '__main__':
    app.run()
