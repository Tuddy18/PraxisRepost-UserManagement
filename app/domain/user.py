from app import db
from app.domain.json_serializable import JsonSerializable


class User(db.Model, JsonSerializable):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))


    def __repr__(self):
        return '<User %r - %r %r>' % (self.email, self.firstname, self.lastname)