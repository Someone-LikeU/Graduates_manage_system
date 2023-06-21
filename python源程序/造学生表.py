# encoding=utf-8
'''
@author:   pip install zjj =_=
@software: Pycharm
@time:     20/12/24 15:40
@filename: 造学生表.py
@contact:  1326632773@qq.com
'''
import csv
import random
from random import randint
import pymysql as psql
import numpy as np
import ipdb
import os
from 造公司表 import getRandomContact, getRandomPersonPhone, getRandomPostCode, getRandomEmail

stu_id = 201700000
idCard = None
firstName = [x for x in '赵钱孙李周武郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜云苏潘葛奚范彭郎']
lastName = [x for x in '艳丽伟强敏芳娜洋军勇杰秀英磊娟静虎雨宇鑫金又双叒叕水淼是第几个吉翁三八节的几个']
sex = ['男', '女']
p_sex = [0.5, 0.5]
nation = ['汉', '水', '苗', '壮', '蒙古', '回', '藏', '土家']
p_nation = [0.93, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
poliStatus = ['中共党员', '中共预备党员', '共青团员']
p_poli = [0.3, 0.2, 0.5]
original = '河北省、山西省、辽宁省、吉林省、黑龙江省、江苏省、浙江省、安徽省、福建省、江西省、山东省、河南省、湖北省、湖南省、广东省、海南省、四川省、贵州省、云南省、陕西省、甘肃省、青海省、台湾省、内蒙古自治区、广西壮族自治区、西藏自治区、宁夏回族自治区、新疆维吾尔自治区、北京市、天津市、上海市、重庆市、香港、澳门'.split('、')
address = None
postcode = None
Birthday_s = [[str(x) for x in range(1995, 2001)], # 年
			  ['0' + str(x) if x < 10 else str(x) for x in range(1, 13)], # 月
			  ['0' + str(x) if x < 10 else str(x) for x in range(1, 32)]] # 日
phone = None
email_list = [chr(ord('a') + x) for x in range(26)] + [str(x) for x in range(10)]
school = '合肥工业大学宣城校区'
departments = ['计算机与信息系', '化工系', '文法学院', '管理学院', '经济系', '机械工程学院']
majors = ['计算机科学与技术', '化学工程', '法学', '管理学', '国际贸易', '机械工程']
depar_major_dict = dict(zip(departments, majors))
regisTime = '2017'
background_cultivate = {'本科':'4', '硕士':'3', '博士':'3'}
background = list(background_cultivate.keys())
p_back = [0.8, 0.15, 0.05]
foreignLang = '英语'
foreignLangRank = ['四级', '六级']
p_rank = [0.7, 0.3]
foreignLangScore = None
hasJob = 'n'
AddrDict = dict()
cities = []
countrysides = []
alreadyName = dict()


def getRandomContact():
	res = random.choice(firstName)
	temp = [random.choice(lastName) for _ in range(randint(1, 2))]
	return res + ''.join(temp)


def getRandomBirthday():
	res = [random.choice(Birthday_s[0]), random.choice(Birthday_s[1])]
	if res[1] not in ['01', '03', '05', '07', '08', '10', '12']:
	    res.append(Birthday_s[2][randint(0, 29)])
	else :
	    res.append(random.choice(Birthday_s[2]))
	# print(res)
	# ipdb.set_trace()
	return '/'.join(res)
	
def getRandomIdenti(birthday):
    res = ''.join([str(randint(0, 9)) for _ in range(6)])
    res += birthday.replace('/', '')
    res += ''.join([str(randint(0, 9)) for _ in range(4)])
    return res

def geneAddrDict():
    with open('area.txt', 'r') as file:
        for line in file:
            temp = line[:-1].split('---')
            t2 = temp[1].split('|')
            cities.append(temp[0])
            for x in t2:
                countrysides.append(x)
    
    # print('cities:', cities, 'countrysides:', countrysides)
    

def getRandAddress():
    province = random.choice(original)
    city = random.choice(cities)
    countryside = random.choice(countrysides)
    road = getRandomContact()
    return province + city + countryside + road
    
def writeFakeStu(nums, filename):
    with open(filename, 'w', newline = '') as file:
        writer = csv.writer(file)
        for i in range(nums):
            sno = str(stu_id + i)
            sname = getRandomContact()
            alreadyName[sname] = alreadyName.get(sname, 0) + 1
            ssex = np.random.choice(sex, p = p_sex)
            snation = np.random.choice(nation, p = p_nation)
            spolistatus = np.random.choice(poliStatus, p = p_poli)
            soriginal = random.choice(original)
            saddress = getRandAddress()
            spostcode = getRandomPostCode()
            sbirthday = getRandomBirthday()
            sid = getRandomIdenti(sbirthday)
            sphone = getRandomPersonPhone()
            semail = getRandomEmail(15)
            sschool = school
            sdepartment = random.choice(departments)
            smajor = depar_major_dict[sdepartment]
            sregistime = regisTime
            sbackground = np.random.choice(background, p = p_back)
            scultivate = np.random.choice(['定向', '非定向'], p = [0.95, 0.05])
            sforeienLang = foreignLang
            sforerienLangRank = np.random.choice(foreignLangRank, p = p_rank)
            sforeienLangScore = str(randint(425, 650))
            shasjob = hasJob
            writer.writerow((sno, sname, sid, ssex, snation, spolistatus,
                             soriginal, saddress, spostcode, sbirthday,
                             sphone, semail, sschool, sdepartment, smajor,
                             sregistime, sbackground, scultivate, sforeienLang,
                             sforerienLangRank, sforeienLangScore, shasjob
                             ))
            



if __name__ == '__main__':
	# 初始信息
	geneAddrDict()
	stu_num = 5000
	filename = 'fake_students_2.csv'
	if not os.path.exists(filename):
		writeFakeStu(stu_num, filename)
	# 开始随机生成

	host_ = 'localhost'
	user = 'root'
	pwd = '123'
	db = 'graduatesdb'
	connecter = psql.connect(host = host_, user = user,
							 password = pwd, database = db,
							 charset = 'utf8')
	db = connecter
	cursor = connecter.cursor()
	with open(filename, 'r') as file:
		reader = csv.reader(file)
		datas = [row for row in reader]
		print(datas)
		sql = "insert into graduates values(%s, %s, %s, %s, %s, %s, %s, " \
		      "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		try:
			cursor.executemany(sql, datas)
			db.commit()
			print("造学生表SQL操作已提交")
			datalist = cursor.fetchall()
			print(datalist)
		
		except Exception as e:
			print('发生异常', e, '操作回滚')
			# graDB.rollback()
			db.rollback()
	