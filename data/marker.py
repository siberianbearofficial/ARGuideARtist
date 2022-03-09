import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Marker(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'markers'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    marker = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    exp_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    info = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    room_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    visiting_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)