import logging
from app import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand

app = create_app('default')
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s[%(name)s][%(levelname)s] :%(levelno)s: %(message)s",
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='logs/weChatService.log',
                        filemode='a')
    manager.run()
