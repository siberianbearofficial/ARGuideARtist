from flask import Flask, render_template
import config
from emulate_db_response import get_photos_from_db
from data import db_session
from one import get_markers, get_routs, get_navigations, get_navigation_r, get_naprav, get_marsh, rooms
from two import sec_exp, like_exp, pos_exp
from json import dumps


db_session.global_init("db/argid.sqlite")
app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    markers = get_markers()
    routs = get_routs()
    navigations = get_navigations()
    navigations_r = get_navigation_r()
    room = rooms()
    print(room)
    print(markers)
    print(routs)
    print(navigations)
    print(navigations_r)
    return 'Hello World my test file'


@app.route('/test')
def test_func():
    return render_template('gallery.html')


@app.route('/test_video')
def test_video_func():
    return render_template('test_video.html')


@app.route('/testtest')
def testtest_func():
    return render_template('testtest.html')


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

@app.route('/admin_statistic')
def adm_stat():
    return sec_exp() #служебная статистка

@app.route('/statistic')
def pol_stat():
    return dumps([like_exp(), pos_exp()]) #пользовательская статистика

if __name__ == '__main__':
    app.run()
