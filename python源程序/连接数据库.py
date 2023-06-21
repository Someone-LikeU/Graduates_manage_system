# encoding=utf-8
'''
@author:   pip install zjj =_=
@software: Pycharm
@time:     20/12/24 14:58
@filename: 连接数据库.py
@contact:  1326632773@qq.com
'''
import pymysql as psql


# class Connecter:
#
# 	def __init__(self, address, user, pwd, database):
# 		self.db = psql.connect(address, user, pwd, database, charset = 'uft8')
#


if __name__ == '__main__':
	
	address = 'localhost'
	user = 'root'
	pwd = '123'
	db = 'graduatesdb'
	connecter = psql.connect(host = address, user = user,
	                         password = pwd, database = db,
	                         charset = 'utf8')
	schools_message = [('合肥工业大学', '安徽省合肥市', '123456', '招生办', '周老师', '18812343421', 'peterporker@163.com'),
					   ('合肥工业大学宣城校区', '安徽省宣城市', '666777', '招生办', '范老师', '12377777777', 'lskdjsdgwes@163.com'),
					   ('中国科学技术大学', '安徽省合肥市', '666666', '招生办', '李老师', '12345678765', 'lskdjlgjs@163.com'),
	                   ('合肥学院', '安徽省合肥市', '654321', '招生办', '何老师', '12345689763', 'lfjdhiretcv@163.com'),
	                   ('宣城职业技术学院', '安徽省宣城市', '777777', '招生办', '赵老师', '13298763245', 'wqeoiuths@163.com'),
	                   ]
	try:
		with connecter.cursor() as cursor:
			sql = "select * from schools"
			cursor.execute(sql)
			res = cursor.fetchall() # 查询结果，以元组类型返回
			print(res)
	
	except:
		print('something wrong')
		
		
		