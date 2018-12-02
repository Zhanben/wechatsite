from app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand
import logging

app = create_app('default')
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='logs/flask-site.log',
                        filemode='a')
    manager.run()
