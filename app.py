from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from create_app import create_app, db

# import the tables so that can be create


db.create_all()
db.session.commit()
app = create_app()





migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()