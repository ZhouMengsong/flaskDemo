import json

from app.web import wb
from app.web import user as ur
from flask import make_response, request, jsonify
from app.web.schema import UserForm
from app.exception import Success, Created, Updated, Deleted


@wb.route("/addUser", methods=["POST"])
def user():
    # 分层处理思想
    # 1、字段基本验证层，2、字段逻辑验证器层，3、逻辑处理层 4、异常处理层 5、返回结果统一处理层
    form = json.loads(request.data)
    u = UserForm(**form)
    if u.validate():
        re = ur.add_user(**form)
        return Success(200, "用户创建成功", re)
    return Created(list(u.errors.values())[0][0])

@wb.route("/userList", methods=["GET"])
def user_list():
    re = ur.query_user_info(one=False, desc=True, order_by="update_time")
    return Success(200, "用户创建成功", re)

@wb.route("/userInfo/<int:userid>", methods=["GET"])
def user_info(userid):
    re = ur.query_user_info(one=True, userid=userid)
    return Success(200, "用户创建成功", re)

@wb.route("/userUpdate", methods=["POST"])
def update_user():
    form = json.loads(request.data)
    try:
        re = ur.update_user(**form)
        return Success(200, "用户更新成功", re)
    except:
        return Updated(list(u.errors.values())[0][0])

@wb.route("/userDelete", methods=["POST"])
def delete_user():
    form = json.loads(request.data)
    try:
        re = ur.delete_user(**form)
        return Success(200, "用户删除成功", re)
    except Deleted as e:
        return Deleted("删除失败")
