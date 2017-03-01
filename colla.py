#! /usr/bin/env python
# -*- coding: utf-8 -*-
# 把所有合作者的信息也统计一下

import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='serendipity',
        charset='utf8',
        )
cursor=connection.cursor()

#得到合作者的id
cursor.execute("select collaborator from top_1000_C;")
results=cursor.fetchall()
for result in results:
	collaborators=result[0].strip().split("#")
	for collaborator in collaborators:
		cursor.execute("INSERT INTO collaborator_C(author) VALUES (%s)",collaborator)
connection.commit()

cursor.execute("select collaborator from top_1000_P;")
results=cursor.fetchall()
for result in results:pu
	collaborators=result[0].strip().split("#")
	for collaborator in collaborators:
		cursor.execute("INSERT INTO collaborator_P(author) VALUES (%s)",collaborator)
connection.commit()

cursor.execute("select collaborator from top_1000_E;")
results=cursor.fetchall()
for result in results:
	collaborators=result[0].strip().split("#")
	for collaborator in collaborators:
		cursor.execute("INSERT INTO collaborator_E(author) VALUES (%s)",collaborator)
connection.commit()


#得到title
title=dict()
cursor.execute("select author from collaborator_C;")
authors=cursor.fetchall()
for (author,) in authors:
	title[author]=list()
cursor.execute("select paperId,authorId from PaperAuthorAffiliations_C;")
result = cursor.fetchall()
for (paperId,authorId) in result:
	if authorId in title:
		title[authorId].append(paperId)
for (key,value) in title.items():
	titles="#".join(value)#变字符串
	cursor.execute("UPDATE collaborator_C SET title = %s WHERE author= %s",(titles,key))
connection.commit()


title=dict()
cursor.execute("select author from collaborator_P;")
authors=cursor.fetchall()
for (author,) in authors:
	title[author]=list()
cursor.execute("select paperId,authorId from PaperAuthorAffiliations_P;")
result = cursor.fetchall()
for (paperId,authorId) in result:
	if authorId in title:
		title[authorId].append(paperId)
for (key,value) in title.items():
	titles="#".join(value)#变字符串
	cursor.execute("UPDATE collaborator_P SET title = %s WHERE author= %s",(titles,key))
connection.commit()

title=dict()
cursor.execute("select author from collaborator_E;")
authors=cursor.fetchall()
for (author,) in authors:
	title[author]=list()
cursor.execute("select paperId,authorId from PaperAuthorAffiliations_E;")
result = cursor.fetchall()
for (paperId,authorId) in result:
	if authorId in title:
		title[authorId].append(paperId)
for (key,value) in title.items():
	titles="#".join(value)#变字符串
	cursor.execute("UPDATE collaborator_E SET title = %s WHERE author= %s",(titles,key))
connection.commit()

#得到year

id_year=dict()
cursor.execute("select paperId,paperPY from Papers_C;")
result=cursor.fetchall()
for (k,v) in result:
	id_year[k]=v#找到paperId和year的对应

title=dict()#存放author和title的对应关系
year=dict()#存放author和year的对应关系

cursor.execute("select author,title from collaborator_C;")
result=cursor.fetchall()
for (author,titles) in result:
	#分割
	title[author]=titles.split("#")
	year[author]=list()
	for s_title in title[author]:
		year[author].append(id_year[s_title])

	min_year=min(int(temp) for temp in year[author])
	years="#".join(year[author])
	cursor.execute("UPDATE collaborator_C SET year = %s,first=%s WHERE author= %s",(years,min_year,author)) 
connection.commit()


id_year=dict()
cursor.execute("select paperId,paperPY from Papers_E;")
result=cursor.fetchall()
for (k,v) in result:
	id_year[k]=v#找到paperId和year的对应

title=dict()#存放author和title的对应关系
year=dict()#存放author和year的对应关系

cursor.execute("select author,title from collaborator_E;")
result=cursor.fetchall()
for (author,titles) in result:
	#分割
	title[author]=titles.split("#")
	year[author]=list()
	for s_title in title[author]:
		year[author].append(id_year[s_title])

	min_year=min(int(temp) for temp in year[author])
	years="#".join(year[author])
	cursor.execute("UPDATE collaborator_E SET year = %s,first=%s WHERE author= %s",(years,min_year,author)) 
connection.commit()


id_year=dict()
cursor.execute("select paperId,paperPY from Papers_P;")
result=cursor.fetchall()
for (k,v) in result:
	id_year[k]=v#找到paperId和year的对应

title=dict()#存放author和title的对应关系
year=dict()#存放author和year的对应关系

cursor.execute("select author,title from collaborator_P;")
result=cursor.fetchall()
for (author,titles) in result:
	#分割
	title[author]=titles.split("#")
	year[author]=list()
	for s_title in title[author]:
		year[author].append(id_year[s_title])

	min_year=min(int(temp) for temp in year[author])
	years="#".join(year[author])
	cursor.execute("UPDATE collaborator_P SET year = %s,first=%s WHERE author= %s",(years,min_year,author)) 
connection.commit()

#得到collaborator
title=dict()
collaborator=dict()
cursor.execute("select author,title from collaborator_C;")
result=cursor.fetchall()
cursor.execute("select paperId,authorId from PaperAuthorAffiliations_C;")
paperId_authorId=cursor.fetchall()
for (author,titles) in result:
	title[author]=set(titles.split("#"))#得到每个作者写过的title
	collaborator[author]=set()#不重复
	
	for (paperId,authorId) in paperId_authorId:
		if paperId in title[author]:
			collaborator[author].add(authorId)
	collaborator[author].remove(author)#去掉自己
	collaborators="#".join(list(collaborator[author]))
	cursor.execute("UPDATE collaborator_C SET collaborator=%s WHERE author= %s",(collaborators,author)) 
connection.commit()

title=dict()
collaborator=dict()
cursor.execute("select author,title from collaborator_E;")
result=cursor.fetchall()
cursor.execute("select paperId,authorId from PaperAuthorAffiliations_E;")
paperId_authorId=cursor.fetchall()
for (author,titles) in result:
	title[author]=set(titles.split("#"))#得到每个作者写过的title
	collaborator[author]=set()#不重复
	
	for (paperId,authorId) in paperId_authorId:
		if paperId in title[author]:
			collaborator[author].add(authorId)
	collaborator[author].remove(author)#去掉自己
	collaborators="#".join(list(collaborator[author]))
	cursor.execute("UPDATE collaborator_E SET collaborator=%s WHERE author= %s",(collaborators,author)) 
connection.commit()

title=dict()
collaborator=dict()
cursor.execute("select author,title from collaborator_P;")
result=cursor.fetchall()
cursor.execute("select paperId,authorId from PaperAuthorAffiliations_P;")
paperId_authorId=cursor.fetchall()
for (author,titles) in result:
	title[author]=set(titles.split("#"))#得到每个作者写过的title
	collaborator[author]=set()#不重复
	
	for (paperId,authorId) in paperId_authorId:
		if paperId in title[author]:
			collaborator[author].add(authorId)
	collaborator[author].remove(author)#去掉自己
	collaborators="#".join(list(collaborator[author]))
	cursor.execute("UPDATE collaborator_P SET collaborator=%s WHERE author= %s",(collaborators,author)) 
connection.commit()



cursor.close()
connection.close()
