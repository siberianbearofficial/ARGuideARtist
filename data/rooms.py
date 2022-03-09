import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase

class Rooms(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'rooms'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    room_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)