
from app.web.models import User, db
from app.web.schema import UserForm


def json_d(class_name, class_data):
    jsond = {}
    for i in class_name.__rejson__:
        jsond[i] = getattr(class_data, i.lower())
    return jsond

def add_user(**json):
    try:
        usr = User.create(**json, commit=True)
        return dict(userid=usr.userid)
    except Exception as e:
        return dict(userid="None")


def query_user_info(**json):
    user_info = User.get(**json)
    if isinstance(user_info, list):
        for i in range(len(user_info)):
            user_info[i] = json_d(UserForm, user_info[i])
        return user_info
    elif user_info is not None:
        return json_d(UserForm, user_info)
    else:
        return dict(code=1, messagge="数据库提交错误")


def update_user(**json):
    try:
        user = User.get(userid=json["userid"])
        if user:
            usr = user.update(**json, commit=True)
            return dict(userid=usr.userid)
        return dict(message="数据更新失败，数据不存在")
    except Exception as e:
        return dict(userid="None")

def delete_user(**json):
    """
        userid=1001, username=1001
    """
    try:
        if "userid" in json:
            userid_l = json["userid"]
            for userid in userid_l:
                user = User.get(userid=userid)
                if user.status==1:
                    usr = user.delete()
                    return dict(message="删除成功")
                return dict(message="删除失败，数据已经为删除状态")
    except:
        raise Exception("数据库连接错误")
