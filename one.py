import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from data import db_session
from data.marker import Marker
from data.routs import Rout
from data.navigation import Navigation
from data.navigation_routs import Navigations_rout
from data.rooms import Rooms
from data.records import Records
from json import dumps


# def create():
# session = db_session.create_session()
# bookOne = Item()
# bookOne.name = 'mama'
# bookOne.count = 155
# bookOne.price = 155
# session.add(bookOne)
# session.commit()
# session.close()

def rooms():
    session = db_session.create_session()
    room = session.query(Rooms).all()

    room_ls = list()
    for rm in room:
        item_dict = {'id': rm.id, 'room_name': rm.room_name}
        room_ls.append(item_dict)

    session.close()
    return room_ls


def get_markers():
    session = db_session.create_session()
    markers = session.query(Marker).all()

    markers_list = list()
    for mrk in markers:
        item_dict = {'id': mrk.id, 'marker': mrk.marker, 'exp_name': mrk.exp_name, 'info': mrk.info,
                     'room_id': mrk.room_id,
                     'visiting_id': mrk.visiting_id, 'model': mrk.model, 'type_model': mrk.type_model}
        markers_list.append(item_dict)

    session.close()

    return markers_list


def get_exhibit(eid):
    eid -= 1
    for mrk in get_markers():
        if mrk['id'] == eid:
            return dumps([mrk['info'], mrk['model'], mrk['type_model']])


def get_list_of_markers():
    ready = list()
    for marker in get_markers():
        ready.append([marker['id'] + 1, marker['marker']])
    return dumps(ready)


def get_routs():
    session = db_session.create_session()
    routs = session.query(Rout).all()

    routs_list = list()
    for rt in routs:
        route = [str(x + 1) for x in list(map(int, rt.routs.split('/')))]
        item_dict = {'id': rt.id, 'routs': "/".join(route), 'name_routs': rt.name_routs}
        routs_list.append(item_dict)

    session.close()

    return routs_list


def gg_routs():
    return dumps(get_routs())


def get_whole_root_by_id(id_):
    for r in get_routs():
        if r['id'] == id_:
            return r['routs']


def get_navigations():
    session = db_session.create_session()
    navigations = session.query(Navigation).all()

    navigations_list = list()
    for nv in navigations:
        item_dict = {'id': nv.id, 'navigation': nv.navigation, 'a_exp_id': nv.a_exp_id, 'b_exp_id': nv.b_exp_id}
        navigations_list.append(item_dict)

    session.close()

    return navigations_list


# def get_navigation_r():
#     session = db_session.create_session()
#     navigation = session.query(Navigations_rout).all()
#
#     navigation_r_list = list()
#     for nvr in navigation:
#         item_dict = {'id': nvr.id, 'routs_id': nvr.routs_id, 'navigation': nvr.navigation}
#         navigation_r_list.append(item_dict)
#
#     session.close()
#
#     return navigation_r_list

def get_rec():
    session = db_session.create_session()
    records = session.query(Records).all()

    rec_list = list()
    for rec in records:
        item_dict = {'id': rec.id, 'time': rec.time, 'exibitId': rec.exibitId,
                     'timeSpentInFrontSec': rec.timeSpentInFrontSec,
                     'visualFeedback': rec.visualFeedback, 'description': rec.description,
                     'completeness': rec.completeness}
        rec_list.append(item_dict)

    session.close()
    return rec_list


def get_navigation_r():
    session = db_session.create_session()
    navigation = session.query(Navigations_rout).all()

    navigation_r_list = list()
    for nvr in navigation:
        item_dict = {'id': nvr.id, 'routs_id': nvr.routs_id, 'navigation': nvr.navigation}
        navigation_r_list.append(item_dict)

    session.close()

    return navigation_r_list


def get_naprav(A, B):
    A, B = A - 1, B - 1
    a = None
    nv = get_navigations()
    try:
        for i in range(len(nv)):
            result_list = [v for k, v in nv[i].items()]
            for j in result_list:
                if j == result_list[2] and j == A:
                    for z in result_list:
                        if z == result_list[3] and z == B:
                            a = result_list[1]
        return a
    except:
        print('ошибка')


def get_marsh():
    c1 = []
    r = get_routs()

    for i in range(len(r)):
        res_ls = [v for k, v in r[i].items()]
        for j in res_ls:
            if j == res_ls[1]:
                c1.append(j)

    return dumps(c1)
