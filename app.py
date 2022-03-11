from flask import Flask, render_template
import config
from emulate_db_response import get_photos_from_db
from one import *
from two import *
from json import dumps

#db_session.global_init("db/argid.sqlite")
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
    return render_template('home_page.html')


@app.route('/test')
def test_func():
    return render_template('gallery.html')


@app.route('/metric')
def metric_func():
    return render_template('metric.html')


@app.route('/admin_metric')
def admin_metric_func():
    return render_template('admin_metric.html')


@app.route("/stars")
def stars():
    return render_template('stars.html')


@app.route("/admin_stars")
def admin_stars():
    return render_template('admin_stars.html')


@app.route("/st")
def st():
    return render_template('st.html')


@app.route("/sta")
def sta():
    return render_template('sta.html')


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


@app.route('/exposition/<route_id>')
def exposition(route_id):
    return render_template('exposition.html', route_id=int(route_id), whole_route=get_whole_root_by_id(int(route_id)))


@app.route('/choose_exposition')
def choose_exposition():
    return render_template('choose_exposition.html')


@app.route('/get_exhibit/<exhibit_id>')
def get_exhibit_func(exhibit_id):
    got = get_exhibit(int(exhibit_id))
    print('GOT:', got)
    return got


@app.route('/get_marker')
def get_marker():
    return get_list_of_markers()


@app.route('/get_marker_by_id/<mid>')
def get_marker_by_id(mid):
    return get_current_marker(int(mid))


@app.route('/testtest')
def testtest_func():
    return render_template('testtest.html')


@app.route('/simple')
def simple_html_func():
    return render_template('simple_html.html')


@app.route('/photo_booth')
def photo_booth():
    return render_template('photo_booth.html')


@app.route('/get_gallery_photos')
def get_gallery_photos():
    return get_photos_from_db()


@app.route('/navigation/<a>/<b>')
def navigation(a, b):
    napr = get_naprav(int(a), int(b))
    print(napr)
    return dumps(napr)


@app.route('/marsh')
def marsh():
    return gg_routs()


@app.route('/admin_statistic')
def adm_stat():
    return sec_exp()  # служебная статистка


@app.route('/adm_str')
def adm_str():
    return like_exp_sr()


@app.route('/test_admin_statistic')
def test_adm_stat():
    a = {"Exp 1": [538, 61, 268.88146426496223], "Exp 2": [658, 122, 374.86247216035633],
         "Exp 3": [538, 61, 266.76745329400194], "Exp 4": [538, 61, 264.8294342832837],
         "Exp 5": [539, 61, 271.0042656916514], "Exp 6": [659, 121, 378.04987320371936],
         "Exp 7": [659, 122, 384.47377326565146], "Exp 8": [539, 61, 267.6633081444165]}
    return a


@app.route('/statistic')
def pol_stat():
    return dumps([like_exp(), pos_exp(), pos_zal()])  # пользовательская статистика


@app.route('/test_statistic')
def pol_test_stat():
    a = {"Exp 1": 3.103234553554135, "Exp 2": 3.250556792873051, "Exp 3": 3.0658800393313665,
         "Exp 4": 3.4887282007656317, "Exp 5": 3.216737761527524, "Exp 6": 3.0808678500986195,
         "Exp 7": 2.8639570985040925, "Exp 8": 3.0848026868178002}
    b = {"Exp 1": 1721, "Exp 2": 1796, "Exp 3": 2034, "Exp 4": 2351, "Exp 5": 1641, "Exp 6": 1183, "Exp 7": 1181,
         "Exp 8": 1191}
    return dumps([a, b])  # пользовательская статистика


if __name__ == '__main__':
    app.run()
