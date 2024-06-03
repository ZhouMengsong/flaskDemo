from app.web.models import Base,db



class Cases(Base):

    caseid = db.Column(db.Integer, nullable=False)
    casename = db.Column(db.String(100), nullable=False)
    casebody = db.Column(db.String(100), nullable=False)
    casedec = db.Column(db.String(500), nullable=False)
    authorid = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, default=1)
