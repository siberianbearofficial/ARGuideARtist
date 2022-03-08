import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Rout(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'routs'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    routs = sqlalchemy.Column(sqlalchemy.String, nullable=False)
