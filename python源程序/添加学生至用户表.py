# encoding=utf-8
'''
@author:   pip install zjj =_=
@software: Pycharm
@time:     21/1/2 18:56
@filename: 添加学生至用户表.py
@contact:  1326632773@qq.com
'''
from config import graDB
import csv
import pymysql as pysql


if __name__ == '__main__':
	db = graDB.DB
	cursor = db.cursor()
	try:
		sql = "select sno from graduates"
		cursor.execute(sql)
		db.commit()
		stu_nos = cursor.fetchall()
		# print(type(stu_nos[0]))
		stu_no_datas = [stu_nos[i][0] for i in range(stu_nos.__len__())]
		# print(stu_no_datas[0][4:])
		# print(stu_no_datas)
		sqls = "insert into users values(%s, %s, %s)"
		sql_data = [[stu_no_datas[i], stu_no_datas[i][4:], 'student'] for i in range(stu_no_datas.__len__())]
		print("开始插入users表")
		# print(sql_data)
		cursor.executemany(sqls, sql_data)
		db.commit()
		print("插入成功")
		
		
	except Exception as e:
		print('Something wrong,', e)
	