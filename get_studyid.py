f=open('../Serendipity_data/FieldOfStudyHierarchy.txt','r')
l1=set()
l2=set()
l3=set()
#先查找出最基本的，再循环查找
for line in f:
	line=line.strip().split("\t")
	#经济相关领域
	if (line[2] == '09ACE10E'):
		l1.add(line[0])
	#计算机相关领域
	elif (line[2] == '0271BC14'):
		l2.add(line[0])
	#物理相关领域
	elif (line[2] == '073B64E4'):
		l3.add(line[0])


for i in range(0,2):
	for line in f:
		line=line.strip().split("\t")
		#经济相关领域
		if (line[2] in l1):
			l1.add(line[0])
		#计算机相关领域
		elif (line[2] in l2):
			l2.add(line[0])
		#物理相关领域
		elif (line[2] in l3):
			l3.add(line[0])


file_E=open('../Serendipity_data/study_e.txt','w')
file_E.write("\t".join(i for i in l1))


file_C=open('../Serendipity_data/study_c.txt','w')
file_C.write("\t".join(i for i in l2))

file_P=open('../Serendipity_data/study_p.txt','w')
file_P.write("\t".join(i for i in l3))