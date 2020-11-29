from app import db
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.domain.json_serializable import JsonSerializable


class Faculty(db.Model, JsonSerializable):
    __tablename__ = 'Faculty'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    specializations = relationship("Specialization", back_populates="faculty")

    def __repr__(self):
        return '<Faculty: %r>' % (self.name)


class Specialization(db.Model, JsonSerializable):
    __tablename__ = 'Specialization'
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    language = Column(String(120))
    faculty_id = Column(Integer, ForeignKey('Faculty.id'))
    faculty = relationship("Faculty", back_populates="specializations", lazy='joined')

    def __repr__(self):
        return '<Specialization: %r %r, %r>' % (self.name, self.language, self.faculty.name)