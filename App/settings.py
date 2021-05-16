from datetime import timedelta

ADMIN_USERS = ("root", "admin")


def func1():
    pass


def get_db_uri(dbinfo):
    backend = dbinfo.get("backend")
    driver = dbinfo.get("driver")
    user = dbinfo.get("user")
    password = dbinfo.get("password")
    host = dbinfo.get("host")
    port = dbinfo.get("port")
    name = dbinfo.get("name")

    return "{}+{}://{}:{}@{}:{}/{}".format(backend, driver, user, password, host, port, name)


class Config:
    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_MAX_OVERFLOW = 20
    SQLALCHEMY_POOL_SIZE = 50

    SECRECT_KEY = "123"
    JSON_AS_ASCII = False

    PERMANET_SESSION_LIFETIME = timedelta(days=7)
    PROPAGETE_EXCEPTION = True

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # 调度任务
    JOBS = [
        {
            'id': 'task_one',
            'func': func1,
            'args': None,
            'trigger': 'cron',
            'hour': '1',
            'minute': '00',
            'second': '10'
        },
    ]
    # 时区
    SCHEDULER_TIMEZONE = "Asia/Shanghai"
    SCHDULER_JOB_DEFAULT = {
        'coalesce': False,
        'max_instances': 3
    }
    SCHEDULER_API_ENABLED = True


class DevelopConfig(Config):
    DEBUG = True

    dbinfo = {
        "backend": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "rock1204",
        "host": "localhost",
        "port": "3306",
        "name": "FlaskTPP1809"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class TestingConfig(Config):
    TESTING = True

    dbinfo = {
        "backend": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "rock1204",
        "host": "localhost",
        "port": "3306",
        "name": "FlaskTPP1809"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):
    dbinfo = {
        "backend": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "rock1204",
        "host": "localhost",
        "port": "3306",
        "name": "FlaskTPP1809"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    DEBUG = True

    dbinfo = {
        "backend": "mysql",
        "driver": "pymysql",
        "user": "root",
        "password": "rock1204",
        "host": "localhost",
        "port": "3306",
        "name": "FlaskTPP1809"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}
