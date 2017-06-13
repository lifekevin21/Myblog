from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'always easy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://kevin:lifeguokuan@localhost:3306/blog_db'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 导入Flask-SQLAlchemy
# 创建了一个 db 对象，这是我们的数据库
# 导入一个新的模块，叫做 models

db = SQLAlchemy(app)
from app import views, models
