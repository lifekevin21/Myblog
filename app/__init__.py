from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from app import views, models


app = Flask(__name__)
app.config.from_object('config')

# 导入Flask-SQLAlchemy
# 创建了一个 db 对象，这是我们的数据库
# 导入一个新的模块，叫做 models
db = SQLAlchemy(app)
