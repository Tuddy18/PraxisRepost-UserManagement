from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from app.domain.json_serializable import JsonSerializable


class User(db.Model, JsonSerializable):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    email = Column(String(120))
    password = Column(String(120))
    firstname = Column(String(120))
    lastname = Column(String(120))

    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': type
    }

    def __repr__(self):
        return '<User[%r] %r - %r %r>' % (self.type, self.email, self.firstname, self.lastname)