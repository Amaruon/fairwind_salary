from __main__ import app

db = app.db


class Names(db.Model):
    __tablename__ = 'names'
    __table_args__ = dict(schema='salary')

    ru_name = db.Column(db.String(50), primary_key=True, nullable=False)
    eng_name = db.Column(db.String(50), primary_key=True, nullable=False)
    pms = db.relationship('Pms', backref='names')


class Project(db.Model):
    __tablename__ = 'projects'
    __table_args__ = dict(schema='salary')

    project = db.Column(db.String(6), primary_key=True, nullable=False)
    pms = db.relationship('Pms', backref='projects')


class Pms(db.Model):
    __tablename__ = 'pms'
    __table_args__ = dict(schema='salary')

    date = db.Column(db.Date, primary_key=True, nullable=False)
    week = db.Column(db.Integer, nullable=False)
    project = db.Column(db.String(6), db.ForeignKey('salary.projects.project'), primary_key=True)
    worker_name = db.Column(db.String(50), db.ForeignKey('salary.names.eng_name'), primary_key=True)
    func_addon = db.Column(db.String(2))
    work_start = db.Column(db.Time)
    work_end = db.Column(db.Time)
    total_with_lunch = db.Column(db.Integer)
