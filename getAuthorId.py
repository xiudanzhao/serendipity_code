#存储在Authors上


#get something about author
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

cursor.execute("select authorId,count(paperId) as times from PaperAuthorAffiliations_E group by authorId order by times desc;")
pKEs=cursor.fetchall()
i=0
for pKE in pKEs:
	cursor.execute("INSERT INTO Authors_E(authorId,ArticleTime) VALUES (%s,%s)",pKE)
	i =+ 1
	if(i==1500):
		break
connection.commit()
print("finish e's commit")


cursor.execute("select authorId,count(paperId) as times from PaperAuthorAffiliations_C group by authorId order by times desc;")
pKCs=cursor.fetchall()
i=0
for pKC in pKCs:
	cursor.execute("INSERT INTO Authors_C(authorId,ArticleTime) VALUES (%s,%s)",pKC)
	i =+ 1
	if(i==1500):
		break
connection.commit()
print("finish c's commit")


cursor.execute("select authorId,count(paperId) as times from PaperAuthorAffiliations_P group by authorId order by times desc;")
pKPs=cursor.fetchall()
i=0
for pKP in pKPs:
	cursor.execute("INSERT INTO Authors_P(authorId,ArticleTime) VALUES (%s,%s)",pKP)
	i =+ 1
	if(i==1500):
		break
connection.commit()
print("finish p's commit")
