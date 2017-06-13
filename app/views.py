from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app import app, db, lm, models
from .forms import LoginForm
from .models import User


# @user_loader回调， 这个回调从会话中存储的用户 ID 重新加载用户对象
# 它应该接受一个用户的 unicodeID 作为参数，并且返回相应的用户对象。
# 如果 ID 无效的话，它应该返回None (而不是抛出异常)。
# (在这种情况下，ID 会被手动从会话中移除且处理会继续)
# load_user( )用来返回用户唯一标识
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


# before_request( )用来储存一个标志，判断用户是否登入
# current_user 获取当前登陆用户信息
# 被 @before_request 绑定的函数会在请求收到时执行( 网上说会在请求收到前执行，不太明白)
# g保存的是当前请求的全局变量，不同的请求会有不同的全局变量
@app.before_request
def before_request():
    g.user = current_user


# 用户登入登出视图用@login_required， 有些地方（比如修改密码）方法上需要加上
# fresh_login_required而不是login_required，两者的区别在于前者必须是用户手动登陆
# 后者还包含了cookie自动登陆的情况，@login_required还用来确保只有登入用户可见
@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    posts = [
        {'author': {'nickname': 'John'},
         'body': 'Beautiful day in Portland!'},
        {'author': {'nickname': 'Susan'},
         'body': 'The Avergers movie was so cool!'}
    ]
    return render_template("index.html",
                           title="Home",
                           user=user,
                           posts=posts)


# 导入LoginForm，视图接受GET和POST请求
# 实例化一个LoginForm
# form.validate_on_submit()判断是否提交
# 提交后用flash( )传递数据
# redirect( )是url跳转

# if g.user is not None and g.user.is_authenticated( ): 的判断用户是否登入，是否允许登入
# if models.User.query.filter_by(nickname=form.openid.data).first( ):判断输入与数据库里
# 是否一致
# User.query.filter_by(nickname=form.openid.data).first_or_404( )如果输入与数据库
# 不一致，请求返回404
# login_user( )是将用户登入(个人理解)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        if models.User.query.filter_by(nickname=form.openid.data).first():
            user = User.query.filter_by(nickname=form.openid.data).first_or_404()
            login_user(user)
            return redirect(url_for('index'))
        else:
            return render_template('login.html',
                                   title="Sign In",
                                   error='[NO]',
                                   form=form)
    return render_template("login.html",
                           title="Sign In",
                           form=form)


# logout_user( )用户登出，并清除cookie
# redirect(url_for('视图处理函数名'))跳转页面
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
