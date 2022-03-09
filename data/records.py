import sqlalchemy
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Records(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'records'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    time = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    exibitId = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    timeSpentInFrontSec = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    visualFeedback = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    completeness = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
