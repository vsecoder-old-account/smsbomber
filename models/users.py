import sqlalchemy as sa
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    username = sa.Column(sa.String, nullable=True)

class Banned(SqlAlchemyBase):
    __tablename__ = 'banned'

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)

class Admins(SqlAlchemyBase):
    __tablename__ = 'admins'

    id = sa.Column(sa.Integer,
                   primary_key=True, autoincrement=True)