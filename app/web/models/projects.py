from . import Base, db




class Projects(Base):
    __tablename__ = 'projects'
    proid = db.Column(db.Integer, nullable=False)
    proname = db.Column(db.String(100), nullable=False)
    prddesc = db.Column(db.String(500), nullable=False)
    authorid = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, default=1)
