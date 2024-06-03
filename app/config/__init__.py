

class BaseConfig:
    PER_PAGE = 10
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/dongfang"
    SECRET_KEY = "12345678"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
