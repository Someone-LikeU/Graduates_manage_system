# encoding=utf-8
'''
@author:   pip install zjj =_=
@software: Pycharm
@time:     20/12/24 19:49
@filename: config.py
@contact:  1326632773@qq.com
'''
import pymysql as psql

class DB:
	
	def __init__(self):
		self.DB = psql.connect('localhost', 'root',
		                     '123', 'graduatesdb', charset = 'utf8')
	
graDB = DB()