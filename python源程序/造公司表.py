# encoding=utf-8
'''
@author:   pip install zjj =_=
@software: Pycharm
@time:     20/12/24 20:38
@filename: 造公司表.py
@contact:  1326632773@qq.com
'''
from config import graDB
import random
from random import randint
import xlrd
import csv
import os


firstName = [x for x in '赵钱孙李周武郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜云苏潘葛奚范彭郎']
lastName = [x for x in '艳丽伟强敏芳娜洋军勇杰秀英磊娟静虎雨宇鑫金又双叒叕水淼是第几个吉翁三八节的几个尚德机构问题啤酒与他人']
ctypes = ['党政机关', '科研设计单位', '高等教育单位', '中等、初等教育',
         '医疗、卫生单位', '艰苦行业事业', '其它事业单位', '国有企业']
original = '河北省、山西省、辽宁省、吉林省、黑龙江省、江苏省、浙江省、安徽省、福建省、江西省、山东省、河南省、湖北省、湖南省、广东省、海南省、四川省、贵州省、云南省、陕西省、甘肃省、青海省、台湾省、内蒙古自治区、广西壮族自治区、西藏自治区、宁夏回族自治区、新疆维吾尔自治区、北京市、天津市、上海市、重庆市、香港、澳门'.split('、')
file = xlrd.open_workbook('公司表.xlsx')
table = file.sheet_by_index(0)
companyNames = table.col_values(1, start_rowx = 1, end_rowx = 120)
cities = []
countrysides = []
alreadyName = dict()


def geneAddrDict():
	with open('area.txt', 'r') as file:
		for line in file:
			temp = line[:-1].split('---')
			t2 = temp[1].split('|')
			cities.append(temp[0])
			for x in t2:
				countrysides.append(x)


def getRandAddress():
    province = random.choice(original)
    city = random.choice(cities)
    countryside = random.choice(countrysides)
    road = getRandomContact()
    return province + city + countryside + road


def getRandomPersonPhone():
	res = ['1'] + [str(randint(0, 9)) for _ in range(10)]
	return ''.join(res)

def getRandomOfficePhone(maxlen):
	length = randint(10, maxlen)
	res = [str(randint(0, 9)) for _ in range(length)]
	res = ''.join(res)
	return res[:4] + '-' + res[4:]

def getRandomEmail(maxlen):
	length = randint(6, maxlen - 6)
	res = ''.join([chr(ord('a') + randint(0, 25)) for _ in range(length)])
	res += '@qq.com' if randint(0, 1) else '@163.com'
	return res

def getRandomPostCode():
	res = [str(randint(1, 9)) for _ in range(6)]
	return ''.join(res)


def getRandomCompanyName():
	res = random.choice(companyNames)
	while '个体' in res:
		res = random.choice(companyNames)
	return res
	
def getRandomContact():
	res = random.choice(firstName)
	temp = [random.choice(lastName) for _ in range(randint(1, 2))]
	res += ''.join(temp)
	alreadyName[res] = alreadyName.get(res, 0) + 1
	
	if alreadyName[res] > 1:
		while alreadyName[res] > 1:
			res = getRandomContact()
	return res

def getRandomCcode(maxlen = 20):
	size = randint(10, maxlen)
	res = [str(randint(0, 9)) for _ in range(size)]
	return ''.join(res)
	
	
def writeFakeCompays(nums):
	with open("fake_companys.csv", "w", newline = '') as f:
		writer = csv.writer(f)
		for i in range(nums):
			cname = getRandomCompanyName()
			code = getRandomCcode()
			contact = getRandomContact()
			if '***' in cname:
				cname = cname.replace('***', contact)
			contactPhone = getRandomPersonPhone()
			ctype = random.choice(ctypes)
			officePhone = getRandomOfficePhone(15)
			Caddress = getRandAddress()
			email = getRandomEmail(20)
			postcode = ''.join([str(randint(0, 9)) for _ in range(6)])
			writer.writerow((cname, code, contact, contactPhone, ctype,
			                 officePhone, Caddress, email, postcode))
			print((cname, code, contact, contactPhone, ctype,
			                 officePhone, Caddress, email, postcode))


if __name__ == '__main__':
	company_num = 50
	datas = []
	db = graDB.DB
	cursor = db.cursor()
	geneAddrDict()
	if not os.path.exists('fake_companys.csv'):
		writeFakeCompays(50)
	
	with open('fake_companys.csv', 'r') as file:
		reader = csv.reader(file)
		datas = [row for row in reader]
		sql = "insert into company values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		try:
			cursor.executemany(sql, datas)
			db.commit()
			print("SQL操作已提交")
			datalist = cursor.fetchall()
			print(datalist)
			
		except Exception as e:
			print('发生异常', e, '操作回滚')
			# graDB.rollback()
			db.rollback()
			
			
		
		

