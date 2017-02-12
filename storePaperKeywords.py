#!/usr/bin/env python
# coding=utf-8

#存储paper、keywords、paperStudyID

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



f=open('../Serendipity_data/PaperKeywords.txt','r')
i=0
for line in f:
	line=line.strip().split("\t")
	if(line[2] == '09ACE10E'):
		cursor.execute("INSERT INTO PaperKeywords_E(paperId,keyWords,parentStudyId) VALUES (%s, %s, %s)",tuple(line))
	

	elif(line[2] == '0271BC14'):
		cursor.execute("INSERT INTO PaperKeywords_C(paperId,keyWords,parentStudyId) VALUES (%s, %s, %s)",tuple(line))


	elif(line[2] == '073B64E4'):
		cursor.execute("INSERT INTO PaperKeywords_P(paperId,keyWords,parentStudyId) VALUES (%s, %s, %s)",tuple(line))
	i =+ 1
	if(i==100):
		i=0	
		connection.commit()


connection.commit()
cursor.close()
connection.close()