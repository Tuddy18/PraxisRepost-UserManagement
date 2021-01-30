from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from app.domain.json_serializable import JsonSerializable


class User(db.Model, JsonSerializable):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    password = Column(String(120))

    def __repr__(self):
        return '<User [%r]>' % (self.email)