# from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired, ValidationError
from pydantic import EmailStr, Field, validator, BaseModel
from app.exception import Failed
from app.web.models import User
from app.web.vaildators import Unique


class UserForm(Form):
    __rejson__ = ["userId", "userName", "email", "createTime"]
    userid: str = StringField(description="用户id", validators=[Unique(User, User.userid)])
    username: str = StringField(description="用户名",validators=[Length(min=3,max=10,message="用户名长度必须在3到10位之间")])
    password: str = StringField(description="密码", validators=[DataRequired()])
    email: str = StringField(description="邮箱号")
    # gender: str = Field(description="性别",Unique())


if __name__ == '__main__':
    # u = UserForm(userid=1, username="1", password="222", age="11", email="333")
    u = UserForm(username="1")
    print(u.validate())
    print(u.errors)