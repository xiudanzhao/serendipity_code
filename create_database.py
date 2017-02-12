#!/usr/bin/python
# -*- coding: UTF-8 -*-

#这个文件是为了把目前得到的数据全部先都存在数据中
#方便以后的存取

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

cursor.execute("""
	CREATE table PaperKeywords_E(
         id int(10) AUTO_INCREMENT PRIMARY KEY,
		 paperId text,
		 keyWords text,
		 parentStudyId text)
""")
cursor.execute("""
	CREATE table PaperKeywords_C(
         id int(10) AUTO_INCREMENT PRIMARY KEY,
		 paperId text,
		 keyWords text,
		 parentStudyId text)
""")
cursor.execute("""
	CREATE table PaperKeywords_P(
         id int(10) AUTO_INCREMENT PRIMARY KEY,
		 paperId text,
		 keyWords text,
		 parentStudyId text)
""")


cursor.execute("""
	CREATE table PaperAuthorAffiliations_E(
	id int(10) AUTO_INCREMENT PRIMARY KEY,
	paperId text,
	authorId text,
	affiliationId text,
	originalANc text,
	normalizedAN text)
""")
cursor.execute("""
	CREATE table PaperAuthorAffiliations_C(
	id int(10) AUTO_INCREMENT PRIMARY KEY,
	paperId text,
	authorId text,
	affiliationId text,
	originalANc text,
	normalizedAN text)
""")
cursor.execute("""
	CREATE table PaperAuthorAffiliations_P(
	id int(10) AUTO_INCREMENT PRIMARY KEY,
	paperId text,
	authorId text,
	affiliationId text,
	originalANc text,
	normalizedAN text)
""")



cursor.execute("""
	CREATE table Papers_E(
	id int(10) AUTO_INCREMENT PRIMARY KEY,
	paperId text,
	originalPN text,
	normalizedPN text,
	paperPY text)
""")
cursor.execute("""
	CREATE table Papers_C(
	id int(10) AUTO_INCREMENT PRIMARY KEY,
	paperId text,
	originalPN text,
	normalizedPN text,
	paperPY text)
""")
cursor.execute("""
	CREATE table Papers_P(
	id int(10) AUTO_INCREMENT PRIMARY KEY,
	paperId text,
	originalPN text,
	normalizedPN text,
	paperPY text)
""")


cursor.execute("""
	CREATE table Authors_E(
	id int(10) AUTO_INCREMENT PRIMARY KEY,
	authorId text,
	authorName text)
""")
cursor.execute("""
	CREATE table Authors_C(
	id int(10) AUTO_INCREMENT PRIMARY KEY,
	authorId text,
	authorName text)
""")
cursor.execute("""
	CREATE table Authors_P(
	id int(10) AUTO_INCREMENT PRIMARY KEY,
	authorId text,
	authorName text)
""")

cursor.close()
connection.close()