import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
        port=3306,
        user='root',
        password='123',
        db='serendipity',
        charset='utf8',
        )
cursor=connection.cursor()

s1=set()
s2=set()
s3=set()
sinter=set()

#得到合作者的id
cursor.execute("select author1,author2,early_year from wzy_c;")
results=cursor.fetchall()
for result in results:

	s1.clear()     #为每个author1的合作者建立一个set，将每个在early_year之前的合作者都加进去
	
	cursor.execute("select author2 from wzy_c where author1=%s and early_year<%s;",(result[0],result[2]))
	collas=cursor.fetchall()
	for colla in collas:
		s1.add(colla)


	s3.clear()  #找到author2为作者，发表时间在early_year之前的所以论文id
	cursor.execute("select paperId from Papers_C join PaperAuthorAffiliations_C on Papers_C.paperID=PaperAuthorAffiliations_C.paperID where authorId=%s and paperPY<%s;",(result[1],result[2]))

	ids=cursor.fetchall()
	for id in ids:
		s3.add(id)

	s2.clear() #对于s3中找到的所有论文，将其作者都加入到s2中
	for paperid in s3:
		cursor.execute("select authorID from PaperAuthorAffiliations_C where paperId=%s;",(paperid))
		imports=cursor.fetchall()
		for import in imports:
			s2.add(import)
	
	if result[0] in s2:  
		s2.remove(result[0])

	if result[1] in s2:
		s2.remove(result[1])

	sinter.clear()
	sinter=s1.intersection(s2)
	
	length=sinter.len()
	li=list(sinter)
	lis="#".join(li)
	
	sql = 'INSERT INTO wzy_c (common_neighbor, common_neighbor_num) where author1=%s and author2=%s VALUES (%s, %s)'
        cursor.execute(sql, (lis,length,result[0],result[1]));


connection.commit()


























