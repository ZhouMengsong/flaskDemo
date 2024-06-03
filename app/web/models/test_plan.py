from . import Base, db

"""
    测试计划
"""

class TestPlan(Base):
    __tablename__ = 'testplan'
    planid = db.Column(db.Integer, nullable=False)
    planname = db.Column(db.String(100), nullable=False)
    plandesc = db.Column(db.String(500), nullable=False)
    authorid = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, default=1)
