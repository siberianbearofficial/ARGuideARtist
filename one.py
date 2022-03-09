import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from data import db_session
from data.marker import Marker
from data.routs import Rout
from data.navigation import Navigation
from data.navigation_routs import Navigations_rout


# def create():
    # session = db_session.create_session()
    # bookOne = Item()
    # bookOne.name = 'mama'
    # bookOne.count = 155
    # bookOne.price = 155
    # session.add(bookOne)
    # session.commit()
    # session.close()


def get_markers():
    session = db_session.create_session()
    markers = session.query(Marker).all()

    markers_list = list()
    for mrk in markers:
        item_dict = {'id': mrk.id, 'marker': mrk.marker, 'exp_name': mrk.exp_name, 'info': mrk.info}
        markers_list.append(item_dict)

    session.close()

    return markers_list


def get_routs():
    session = db_session.create_session()
    routs = session.query(Rout).all()

    routs_list = list()
    for rt in routs:
        item_dict = {'id': rt.id, 'routs': rt.routs}
        routs_list.append(item_dict)

    session.close()

    return routs_list


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


def get_navigation_r():
    session = db_session.create_session()
    navigation = session.query(Navigations_rout).all()

    navigation_r_list = list()
    for nvr in navigation:
        item_dict = {'id': nvr.id, 'routs_id': nvr.routs_id, 'navigation': nvr.navigation}
        navigation_r_list.append(item_dict)

    session.close()

    return navigation_r_list

