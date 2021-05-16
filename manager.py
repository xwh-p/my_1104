import os
from flask_script import Manager
from flask_migrate import MigrateCommand
from App import creaate_app

env = os.environ.get("FLASK") or "default"

app = creaate_app(env)

manager = Manager(app)

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()