from flask_migrate import MigrateCommand
from flask_script import Manager

from app import create_app

app = create_app('develop')
app.app_context().push()
# 创建一个Manager对象
manager = Manager(app)
manager.add_command('db', MigrateCommand)   # 添加Migrate的所有子命令到db下

if __name__ == '__main__':
    manager.run()
