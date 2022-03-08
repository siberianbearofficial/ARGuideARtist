import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase
from data.item import Item
from data import db_session

session = db_session.create_session()
item = Item()
session.add(item)
session.commit()
session.close()