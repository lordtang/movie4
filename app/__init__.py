# coding:utf8
from flask import Flask

# 实例化Flask对象
app = Flask(__name__)
# 下面用于开启调试模式
app.debug = True

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")
