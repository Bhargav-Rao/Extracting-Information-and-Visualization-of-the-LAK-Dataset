'''This program sorts the dataset into nodes and relations

Important Note - If the Neo4j is the enterprise edition, then this is the endpoint. The created dataset can be directly loaded to the Server
'''


fp1 = open("Types.cyp",'r')
fp2 = open ("LAK-DATASET-DUMP.cyp",'w')
for i in sorted(fp1.readlines()):
	if ')-[:' in i and ']->(' in i:
		pass
	else:
		fp2.write(i)
		
fp1.seek(0)
for i in sorted(fp1.readlines()):
	if ')-[:' in i and ']->(' in i:
		fp2.write(i)
