import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from data import item
from data import db_session
from data.item import Item

def create():
    session = db_session.create_session()
    bookOne = Item()
    bookOne.name = 'mama'
    bookOne.count = 155
    bookOne.price = 155
    session.add(bookOne)
    session.commit()
    session.close()
