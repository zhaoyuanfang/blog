# -*- coding:UTF-8 -*-
from flask import render_template,flash,redirect
from app import app
from app.forms import LoginForm
@app.route('/')
@app.route('/index')
def index():
	user = {'username':'duke'}
	posts = [
		{
			'author':{'username':'Yuanfang'},
			'body':'example-1'
		},
		{
			'author':{'username':'Yuanfang'},
			'body':'example-2'
		}
		]
	return render_template('index.html',title='Mine',user=user,posts=posts)


@app.route('/login',methods=['GET','POST'])
def login(): 
	form = LoginForm()
	if form.validate_on_submit(): 
		flash('用户登录的名户名是:{} , 是否记住我:{}'.format(form.username.data,form.remember_me.data)) 
		return redirect('/index')
	return render_template('login.html',title='登录',form=form)
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('user\'s username is:{}, whether rememberme:{}'.format(form.username.data,form.remember_me.data))
		return redirect('/index')
	return render_template('login.html',title='Login',form=form)
