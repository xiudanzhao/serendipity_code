#! /usr/bin/env python
# -*- coding: utf-8 -*-
#在top_1000_*的数据表中把他们的academic age算出来,到2017年

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
cursor.execute("select author,(2017-first) as aca from top_1000_C;")
result=cursor.fetchall()
for (k,v) in result:
	cursor.execute("UPDATE top_1000_C SET academic_age=%s WHERE author=%s",(v,k))
connection.commit()


cursor.execute("select author,(2017-first) as aca from top_1000_P;")
result=cursor.fetchall()
for (k,v) in result:
	cursor.execute("UPDATE top_1000_P SET academic_age=%s WHERE author=%s",(v,k))
connection.commit()


cursor.execute("select author,(2017-first) as aca from top_1000_E;")
result=cursor.fetchall()
for (k,v) in result:
	cursor.execute("UPDATE top_1000_E SET academic_age=%s WHERE author=%s",(v,k))
connection.commit()


cursor.close()
connection.close()
