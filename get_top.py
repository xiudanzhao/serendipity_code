#! /usr/bin/env python
# -*- coding: utf-8 -*-
#得到每个行业的前1000个人,然后其余的存储在top_1000_E,这个表里面都包括author text,title text,year int(4),first int(4),collaborator text

import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='serendipity',
        charset='utf8',
        )
cursor=connection.cursor()


#得到第一列author
cursor.execute("select authorId,count(paperId) as times from PaperAuthorAffiliations_E group by authorId order by times desc limit 1000;")

pKEs=cursor.fetchall()
for pKE in pKEs:
    cursor.execute("INSERT INTO top_1000_E(author) VALUES (%s)",pKE[0])
connection.commit()


cursor.execute("select authorId,count(paperId) as times from PaperAuthorAffiliations_C group by authorId order by times desc limit 1000;")

pKEs=cursor.fetchall()
for pKE in pKEs:
    cursor.execute("INSERT INTO top_1000_C(author) VALUES (%s)",pKE[0])
connection.commit()



cursor.execute("select authorId,count(paperId) as times from PaperAuthorAffiliations_P group by authorId order by times desc limit 1000;")

pKEs=cursor.fetchall()
for pKE in pKEs:
    cursor.execute("INSERT INTO top_1000_P(author) VALUES (%s)",pKE[0])
connection.commit()


#处理title
title=dict()
cursor.execute("select author from top_1000_C;")
authors=cursor.fetchall()
#用dict把Author和title连接起来
for (author,) in authors:
	title[author]=list()#authors 是由tuple组成的


cursor.execute("select paperId,authorId from PaperAuthorAffiliations_C;")
result = cursor.fetchall()
for (paperId,authorId) in result:
	if authorId in title:
		title[authorId].append(paperId)

#update data
for (key,value) in title.items():
	titles="#".join(value)#变字符串
	cursor.execute("UPDATE top_1000_C SET title = %s WHERE author= %s",(titles,key))
connection.commit()




title=dict()
cursor.execute("select author from top_1000_P;")
authors=cursor.fetchall()
#用dict把Author和title连接起来
for (author,) in authors:
	title[author]=list()


cursor.execute("select paperId,authorId from PaperAuthorAffiliations_P;")
result = cursor.fetchall()
for (paperId,authorId) in result:
	if authorId in title:
		title[authorId].append(paperId)

#update data
for (key,value) in title.items():
	titles="#".join(value)#变字符串
	cursor.execute("UPDATE top_1000_P SET title = %s WHERE author= %s",(titles,key))
connection.commit()




title=dict()
cursor.execute("select author from top_1000_E;")
authors=cursor.fetchall()
#用dict把Author和title连接起来
for (author,) in authors:
	title[author]=list()


cursor.execute("select paperId,authorId from PaperAuthorAffiliations_E;")
result = cursor.fetchall()
for (paperId,authorId) in result:
	if authorId in title:
		title[authorId].append(paperId)

#update data
for (key,value) in title.items():
	titles="#".join(value)#变字符串
	cursor.execute("UPDATE top_1000_E SET title = %s WHERE author= %s",(titles,key))
connection.commit()



#得到year
id_year=dict()
cursor.execute("select paperId,paperPY from Papers_C;")
result=cursor.fetchall()
for (k,v) in result:
	id_year[k]=v#找到paperId和year的对应

title=dict()#存放author和title的对应关系
year=dict()#存放author和year的对应关系

cursor.execute("select author,title from top_1000_C;")
result=cursor.fetchall()
for (author,titles) in result:
	#分割
	title[author]=titles.split("#")
	year[author]=list()
	for s_title in title[author]:
		year[author].append(id_year[s_title])

	min_year=min(int(temp) for temp in year[author])
	years="#".join(year[author])
	cursor.execute("UPDATE top_1000_C SET year = %s,first=%s WHERE author= %s",(years,min_year,author)) 
connection.commit()

#得到collaborator
title=dict()
collaborator=dict()
cursor.execute("select author,title from top_1000_C;")
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
	cursor.execute("UPDATE top_1000_C SET collaborator=%s WHERE author= %s",(collaborators,author)) 
connection.commit()


#得到year
id_year=dict()
cursor.execute("select paperId,paperPY from Papers_E;")
result=cursor.fetchall()
for (k,v) in result:
	id_year[k]=v#找到paperId和year的对应

title=dict()#存放author和title的对应关系
year=dict()#存放author和year的对应关系

cursor.execute("select author,title from top_1000_E;")
result=cursor.fetchall()
for (author,titles) in result:
	#分割
	title[author]=titles.split("#")
	year[author]=list()
	for s_title in title[author]:
		year[author].append(id_year[s_title])

	min_year=min(int(temp) for temp in year[author])
	years="#".join(year[author])
	cursor.execute("UPDATE top_1000_E SET year = %s,first=%s WHERE author= %s",(years,min_year,author)) 
connection.commit()

#得到collaborator
title=dict()
collaborator=dict()
cursor.execute("select author,title from top_1000_E;")
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
	cursor.execute("UPDATE top_1000_E SET collaborator=%s WHERE author= %s",(collaborators,author)) 
connection.commit()


#得到year
id_year=dict()
cursor.execute("select paperId,paperPY from Papers_P;")
result=cursor.fetchall()
for (k,v) in result:
	id_year[k]=v#找到paperId和year的对应

title=dict()#存放author和title的对应关系
year=dict()#存放author和year的对应关系

cursor.execute("select author,title from top_1000_P;")
result=cursor.fetchall()
for (author,titles) in result:
	#分割
	title[author]=titles.strip().split("#")
	year[author]=list()
	for s_title in title[author]:
		try:
			year[author].append(id_year[s_title])

		except Exception as e:
			year[author].append("2020")#数据有问题,有的数据在PaperAuthorAffiliations_P却不在paper_P中
			

	min_year=min(int(temp) for temp in year[author])
	years="#".join(year[author])
	cursor.execute("UPDATE top_1000_P SET year = %s,first=%s WHERE author= %s",(years,min_year,author)) 
connection.commit()

#得到collaborator
title=dict()
collaborator=dict()
cursor.execute("select author,title from top_1000_P;")
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
	cursor.execute("UPDATE top_1000_P SET collaborator=%s WHERE author= %s",(collaborators,author)) 
connection.commit()



cursor.close()
connection.close()
