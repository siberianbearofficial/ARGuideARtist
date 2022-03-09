import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Rout(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'navigation_routs'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    routs_id = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    navigation = sqlalchemy.Column(sqlalchemy.String, nullable=False)
