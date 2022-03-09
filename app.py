from flask import Flask, render_template
import config
from json import dumps
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

@app.route('/metric')
def metric_func():
    return render_template('metric.html')

@app.route("/stars")
def stars():
    return render_template('stars.html')

@app.route("/st")
def st():
    return render_template('st.html')

@app.route("/zal")
def zal():
    return render_template('zal.html')

@app.route("/accaunt")
def accaunt():
    return render_template('accaunt.html')

@app.route('/getmetric')
def getmetric_func():
    metriclist = [
        {'id':1, 'time':'2022-03-06 09:52:11','exibitId':1, "timeSpentInFrontSec":193, "visualFeedback":3, "description":5, "completeness":4},
        {'id':2, 'time':'2022-03-06 10:03:35','exibitId':6, "timeSpentInFrontSec":588, "visualFeedback":3, "description":4, "completeness":2},
        {'id':3, 'time':'2022-03-06 09:47:00','exibitId':7, "timeSpentInFrontSec":545, "visualFeedback":5, "description":5, "completeness":2},
        {'id':4, 'time':'2022-03-06 10:13:44','exibitId':5, "timeSpentInFrontSec":255, "visualFeedback":4, "description":5, "completeness":3},
        {'id':5, 'time':'2022-03-06 10:19:30','exibitId':4, "timeSpentInFrontSec":227, "visualFeedback":3, "description":2, "completeness":3},
        {'id':6, 'time':'2022-03-06 09:39:00','exibitId':3, "timeSpentInFrontSec":151, "visualFeedback":2, "description":3, "completeness":4},
        {'id':7, 'time':'2022-03-06 09:42:26','exibitId':4, "timeSpentInFrontSec":267, "visualFeedback":4, "description":5, "completeness":2},
        {'id':8, 'time':'2022-03-06 09:47:45','exibitId':2, "timeSpentInFrontSec":275, "visualFeedback":5, "description":2, "completeness":2},
        {'id':9, 'time':'2022-03-06 09:53:11','exibitId':7, "timeSpentInFrontSec":462, "visualFeedback":1, "description":5,"completeness":1},
        {'id':10, 'time':'2022-03-06 10:02:26','exibitId':1, "timeSpentInFrontSec":213, "visualFeedback":5, "description":3, "completeness":5}]

    return dumps(metriclist)

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
