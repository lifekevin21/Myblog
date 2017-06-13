import os


CSRF_ENABLED = True
SECRET_KEY = 'never-try-this'

'''
# db文件创建在与创建脚本同一目录下
# SQLALCHEMY_DATABASE_URI是the Flask-SQLAlchemy必需的扩展。这是我们的数据库文件的路径。
# SQLALCHEMY_MIGRATE_REPO 是用来存储SQLAlchemy-migrate数据库文件的文件夹。
# SQLALCHEMY_TRACK_MODIFICATIONS 不设为True会报错(貌似这段代码没有也能正常运行)
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
'''