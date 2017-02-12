#!/usr/bin/python
# -*- coding: UTF-8 -*-

#prepare for W

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
	port=3306,
	user='root',
	password='123',
	db='serendipity',
	charset='utf8',
	)
cursor = connection.cursor()

cursor.execute("SELECT paperId,authorId FROM PaperAuthorAffiliations_E")
PaperAuthorYears = cursor.fetchall()

#最后的结果是想得到两个人的合作信息
cursor.execute("""
	CREATE table PaperAuthorYear_E(
	id int(10) AUTO_INCREMENT PRIMARY KEY,
	paperId text,
	authorId1 text,
	authorId2 text,
	paperPY text,
	originalAN1 text,
	normalizedAN1 text,
	originalAN2 text,
	normalizedAN2 text)
""")
#之后还需要再做得到所有的第一次合作之前或者是合作时候的信息，然后记录地理坐标，然后算出地理位置的距离


#把合作信息用dict表示出来
d=dict()

for PaperAuthorYear in PaperAuthorYears:
	if PaperAuthorYear[0] in d:
		d[PaperAuthorYear[0]].append(PaperAuthorYear[1])
	else:
		d[PaperAuthorYear[0]]=[PaperAuthorYear[1],]

for key,value in d:
	if len(value)>1:
		index_begin=0
		for name in value:
			authorId1=name
			index_end=index_begin+1
			while index_end < len(value):
				authorId2=value[index_end]
				#insert data
				cursor.execute("INSERT INTO PaperAuthorYear_E(paperId,authorId1,authorId2) VALUES (%s,%s,%s)",(key,authorId1,authorId2))
				index_end += 1
			if (index_begin == len(value)-2):
				break
			index_begin +=1
		connection.commit()





cursor.close()
connection.close()
