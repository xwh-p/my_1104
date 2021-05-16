from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# from flas_cors import CORS
from flask_apscheduler import APScheduler

db = SQLAlchemy()
migrate = Migrate()
aps = APScheduler()

def init_ext(app):
    # CORS(app,supports_credtials=True,resource="/*")
    db.init_app(app=app)
    migrate.init_app(app=app,db=db)
    aps.init_app(app)
    aps.start()