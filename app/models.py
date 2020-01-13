from . import db


# TODO: MVC-M
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer)
    address = db.Column(db.String(64))

    def __repr__(self):
        return '<Student %r>' % self.id
