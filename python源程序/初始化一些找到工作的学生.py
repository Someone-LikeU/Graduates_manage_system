# encoding=utf-8
'''
@author:   pip install zjj =_=
@software: Pycharm
@time:     21/1/1 20:07
@filename: 初始化一些找到工作的学生.py
@contact:  1326632773@qq.com
'''
from 造公司表 import getRandomContact, getRandomPersonPhone, getRandomPostCode, getRandomEmail
from config import graDB
import random
from random import randint
import numpy as np
import xlrd
import csv

comments = ['该生表现出色，工作能力强，业务能力优秀',
            '这个学生表现不错，值得表扬',
            '工作努力，为人很好，值得称赞',
            '业务能力强，好相处，为人善良，好说话',
            '工作态度不端正，和同事相处不融洽']


if __name__ == '__main__':
	db = graDB.DB
	cursor = db.cursor()
	stuFile = open('fake_students.csv', 'r')
	stuReader = csv.reader(stuFile)
	compFile = open('fake_companys.csv', 'r')
	compReader = csv.reader(compFile)
	stuData = [row for row in stuReader]
	comData = [row for row in compReader]
	comData_index = [i for i in range(comData.__len__())]
	# print(stuData[0])
	
	db = graDB.DB
	cursor = db.cursor()
	
	num = 100
	for i in range(num):
		row = stuData[i]
		# company = random.choice(comData)
		idx = np.random.choice(comData_index, replace = False)
		company = comData[idx]
		cname = company[0]
		ccontact = company[2]
		ccontactPhone = company[3]
		fileAcc = '人事部'
		fileAccCont = getRandomContact()
		fileAccCOntPhone = getRandomPersonPhone()
		print(row[1], row[0], row[10],
			      cname, ccontact, ccontactPhone, fileAcc, fileAccCont, fileAccCOntPhone)
		# try:
		# 	sql = "insert into graduatesjob values('%s', '%s', '%s', '%s', " \
		# 	      "'%s', '%s', '%s', '%s', '%s')"%(row[1], row[0], row[10],
		# 	      cname, ccontact, ccontactPhone, fileAcc, fileAccCont, fileAccCOntPhone)
		# 	cursor.execute(sql)
		#
		# 	db.commit()
		# 	print(cursor.fetchall())
		# except Exception as e:
		# 	print('Something wrong', e)
		
		# 插入评论表
		try:
			com = random.choice(comments)
			sql2 = "insert into graduatescomments values('%s', '%s', '%s', '%s', '%s')" %\
			      (cname, ccontact, row[1], row[0], com)
			cursor.execute(sql2)
			
			db.commit()
			print(cursor.fetchall())
		except Exception as e:
			print('Something wrong', e)
			
		
		
			
	
	