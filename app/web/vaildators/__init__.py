from wtforms.validators import ValidationError


class Unique:

    def __init__(self, db_class, db_column, msg=None):
        self.db_class = db_class
        self.db_column = db_column
        if msg is None:
            self.msg = "数据已经存在"
        else:
            self.msg = msg

    def __call__(self, form, field):
        res = self.db_class.query.filter(self.db_column==field.data).first()
        if res:
            raise ValidationError(self.msg)
        return res