import os
BASE_DIR=os.path.abspath(os.path.dername(__file__))
class Config(object):
	SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@localhost:3306/flaskblog?charset=utf8'
	SQLALCHEMY_TRACK_MODIFICATIONS=False
