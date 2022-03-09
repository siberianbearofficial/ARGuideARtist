from flask import Flask, render_template
import config
from emulate_db_response import get_photos_from_db
from data import db_session
from one import get_markers, get_routs, get_navigations, get_navigation_r, get_naprav, get_marsh, rooms, get_list_of_markers
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
        {'id': 1, 'time': '2022-03-06 09:52:11', 'exibitId': 1, "timeSpentInFrontSec": 193, "visualFeedback": 3,
         "description": 5, "completeness": 4},
        {'id': 2, 'time': '2022-03-06 10:03:35', 'exibitId': 6, "timeSpentInFrontSec": 588, "visualFeedback": 3,
         "description": 4, "completeness": 2},
        {'id': 3, 'time': '2022-03-06 09:47:00', 'exibitId': 7, "timeSpentInFrontSec": 545, "visualFeedback": 5,
         "description": 5, "completeness": 2},
        {'id': 4, 'time': '2022-03-06 10:13:44', 'exibitId': 5, "timeSpentInFrontSec": 255, "visualFeedback": 4,
         "description": 5, "completeness": 3},
        {'id': 5, 'time': '2022-03-06 10:19:30', 'exibitId': 4, "timeSpentInFrontSec": 227, "visualFeedback": 3,
         "description": 2, "completeness": 3},
        {'id': 6, 'time': '2022-03-06 09:39:00', 'exibitId': 3, "timeSpentInFrontSec": 151, "visualFeedback": 2,
         "description": 3, "completeness": 4},
        {'id': 7, 'time': '2022-03-06 09:42:26', 'exibitId': 4, "timeSpentInFrontSec": 267, "visualFeedback": 4,
         "description": 5, "completeness": 2},
        {'id': 8, 'time': '2022-03-06 09:47:45', 'exibitId': 2, "timeSpentInFrontSec": 275, "visualFeedback": 5,
         "description": 2, "completeness": 2},
        {'id': 9, 'time': '2022-03-06 09:53:11', 'exibitId': 7, "timeSpentInFrontSec": 462, "visualFeedback": 1,
         "description": 5, "completeness": 1},
        {'id': 10, 'time': '2022-03-06 10:02:26', 'exibitId': 1, "timeSpentInFrontSec": 213, "visualFeedback": 5,
         "description": 3, "completeness": 5}]

    return dumps(metriclist)


@app.route('/test_video')
def test_video_func():
    return render_template('test_video.html')


@app.route('/exposition')
def exposition():
    return render_template('exposition.html')


@app.route('/get_marker')
def get_marker():
    return get_list_of_markers()


@app.route('/testtest')
def testtest_func():
    return render_template('testtest.html')


@app.route('/photo_booth')
def photo_booth():
    return render_template('photo_booth.html')


@app.route('/get_gallery_photos')
def get_gallery_photos():
    return get_photos_from_db()


@app.route('/navigation/<a>/<b>')
def navigation(a, b):
    return get_naprav(int(a), int(b))


@app.route('/marsh')
def marsh():
    return get_marsh()


@app.route('/admin_statistic')
def adm_stat():
    return sec_exp()  # служебная статистка


@app.route('/test_admin_statistic')
def test_adm_stat():
    return '{"Exp 1":"Max: 538   Min: 61  Sr: 268.88146426496223","Exp 2":"Max: 658   Min: 122  Sr: 374.86247216035633","Exp 3":"Max: 538   Min: 61  Sr: 266.76745329400194","Exp 4":"Max: 538   Min: 61  Sr: 264.8294342832837","Exp 5":"Max: 539   Min: 61  Sr: 271.0042656916514","Exp 6":"Max: 659   Min: 121  Sr: 378.04987320371936","Exp 7":"Max: 659   Min: 122  Sr: 384.47377326565146","Exp 8":"Max: 539   Min: 61  Sr: 267.6633081444165"}'


@app.route('/statistic')
def pol_stat():
    return dumps([like_exp(), pos_exp()])  # пользовательская статистика


@app.route('/test_statistic')
def pol_test_stat():
    return '[{"Exp 1": "Sr: 3.103234553554135", "Exp 2": "Sr: 3.250556792873051", "Exp 3": "Sr: 3.0658800393313665", "Exp 4": "Sr: 3.4887282007656317", "Exp 5": "Sr: 3.216737761527524", "Exp 6": "Sr: 3.0808678500986195", "Exp 7": "Sr: 2.8639570985040925", "Exp 8": "Sr: 3.0848026868178002"}, {"Exp 1": 1721, "Exp 2": 1796, "Exp 3": 2034, "Exp 4": 2351, "Exp 5": 1641, "Exp 6": 1183, "Exp 7": 1181, "Exp 8": 1191}]'  # пользовательская статистика


if __name__ == '__main__':
    app.run()
