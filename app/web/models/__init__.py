from app import db
from datetime import datetime
from app.tools.utils import camel2line

class Base(db.Model):
    __abstract__ = True

    def __init__(self):
        name: str = self.__class__.__name__
        if not hasattr(self, "__tablename__"):
            self.__tablename__ = camel2line(name)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_time = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    update_time = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False)
    status = db.Column(db.Integer, default=1)

    @classmethod
    def get(cls, start=None, count=None, one=True, desc=False, **kwargs):
        # 应用软删除，必须带有delete_time
        if kwargs.get("status") is 1:
            kwargs["status"] = 0
        if one:
            return cls.query.filter().filter_by(**kwargs).first()
        if desc:
            if "order_by" in kwargs:
                return cls.query.order_by(cls.update_time.desc()).offset(start).limit(count).all()
        return cls.query.filter().filter_by(**kwargs).offset(start).limit(count).all()

    @classmethod
    def create(cls, **kwargs):
        one = cls()
        for key in kwargs.keys():
            # if key == 'from':
            #     setattr(one, '_from', kwargs[key])
            # if key == 'parts':
            #     setattr(one, '_parts', kwargs[key])
            if hasattr(one, key):
                setattr(one, key, kwargs[key])
        db.session.add(one)
        if kwargs.get("commit") is True:
            db.session.commit()
        return one

    def update(self, **kwargs):
        for key in kwargs.keys():
            # if key == 'from':
            #     setattr(self, '_from', kwargs[key])
            if hasattr(self, key):
                setattr(self, key, kwargs[key])
        db.session.add(self)
        if kwargs.get("commit") is True:
            db.session.commit()
        return self

    def delete(self):
        # 删除状态等于0
        self.status = 0
        self.update_time = datetime.now()
        db.session.add(self)
        db.session.commit()


from .user import *
from .projects import *
from .cases import *
from .test_plan import *

