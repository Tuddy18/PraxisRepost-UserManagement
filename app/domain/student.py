from app.domain.user import User
from app.domain.faculty import *
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class Student(User):
    __tablename__ = 'Student'
    id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    nr_mat = Column(Integer)
    specialization_id = Column(Integer, ForeignKey('Specialization.id'))
    specialization = relationship("Specialization", lazy='joined')

    __mapper_args__ = {
        'polymorphic_identity':'student',
    }

    def __repr__(self):
        return '<User %r - %r %r>' % (self.email, self.firstname, self.lastname)