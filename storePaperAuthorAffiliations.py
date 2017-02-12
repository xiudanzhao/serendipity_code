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

#get the paperid in economy
cursor.execute("select paperId from PaperKeywords_E")
pKEs=cursor.fetchall()
set_e=set()
for pKE in pKEs:
	set_e.add(pKE[0])

#get the paperid in computer
cursor.execute("select paperId from PaperKeywords_C")
pKCs=cursor.fetchall()
set_c=set()
for pKC in pKCs:
	set_c.add(pKC[0])

#get the paperid in phycise
cursor.execute("select paperId from PaperKeywords_P")
pKPs=cursor.fetchall()
set_p=set()
for pKP in pKPs:
	set_p.add(pKP[0])

print('set')
f=open('../Serendipity_data/PaperAuthorAffiliations.txt','r')
i=0

for line in f:

	line=line.strip().split("\t")

	if (line[0] in set_e):
		cursor.execute("INSERT INTO PaperAuthorAffiliations_E(paperId,authorId,affiliationId,originalANc,normalizedAN) VALUES (%s, %s,%s,%s,%s)",tuple(line[0:5]))


	elif (line[0] in set_c):
		cursor.execute("INSERT INTO PaperAuthorAffiliations_C(paperId,authorId,affiliationId,originalANc,normalizedAN) VALUES (%s, %s,%s,%s,%s)",tuple(line[0:5]))
		
		
	elif (line[0] in set_p):
		cursor.execute("INSERT INTO PaperAuthorAffiliations_P(paperId,authorId,affiliationId,originalANc,normalizedAN) VALUES (%s, %s,%s,%s,%s)",tuple(line[0:5]))

	i =+ 1
	if(i==100):
		i=0
		connection.commit()

connection.commit()		

cursor.close()
connection.close()