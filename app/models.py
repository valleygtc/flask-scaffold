from . import db


# TODO: MVC-M
class PlanTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime, nullable=False)
    task = db.Column(db.String(64), nullable=False)
    detail = db.Column(db.Text, nullable=False)
    status = db.Column(db.Integer)
    operator = db.Column(db.String(32))

    def __repr__(self):
        return '<PlanTask %r>' % self.id
