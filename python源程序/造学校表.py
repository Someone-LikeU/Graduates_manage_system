# encoding=utf-8
'''
@author:   pip install zjj =_=
@software: Pycharm
@time:     20/12/24 17:32
@filename: 造学校表.py
@contact:  1326632773@qq.com
'''
import csv
from config import graDB


if __name__ == '__main__':
	with open('schools.csv', 'r') as file:
		reader = csv.reader(file)
		graduateDB = graDB.DB
		cursor = graduateDB.cursor()
		datas = [row for row in reader]
		for row in datas:
			print(tuple(row))
		sql = "INSERT INTO schools values (%s, %s, %s, %s, %s, %s, %s)"
		try:
			# print('进入try')
			num_affected = cursor.executemany(sql, datas)
			graduateDB.commit()
			print('sql操作已提交')
			datalist = cursor.fetchall()
			print(num_affected, 'rows affected', datalist)
		except Exception as e:
			print('发生异常', e, '操作回滚')
			# graDB.rollback()
			graduateDB.rollback()
		
		graduateDB.close()