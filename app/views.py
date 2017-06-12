from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Bob'}
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
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('login requested for OpenID="'+form.openid.data+'",remember_me='+str(form.remember_me.data))
        return redirect('/index')
    return render_template("login.html",
                           title="Sign In",
                           form=form)
