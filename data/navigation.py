import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Navigation(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'navigation'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    a_exp_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    b_exp_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    navigation = sqlalchemy.Column(sqlalchemy.String, nullable=False)
