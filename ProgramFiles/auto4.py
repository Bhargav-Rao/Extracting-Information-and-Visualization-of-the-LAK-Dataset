'''This program links the nodes needing dbpedia links into relations
'''

import re
fp1 = open("Relat.nt","r")
fp2 = open("Types.cyp","a")

lst = {'http://xmlns.com/foaf/0.1/based_near':'based_near',
'http://purl.org/dc/terms/subject' : 'subject'}

for a in lst:
	fp1.seek(0)
	for i in fp1.readlines(0):
		if a in i:
			
			t= re.search('<http://data.linkededucation.org/resource/lak/',i)
			e = re.search('>',i)
			m=""
			for j in i[t.start()+46:e.start()]:
				if j.isalnum():
					m+=j
				else:
					m+='_'
			n=''
			t= re.search('http://dbpedia.org/resource/',i)
			for j in i[t.start()+28:-4]:
				if j.isalnum():
					n+=j
				else:
					n+='_'
			
			
			s= "CREATE ("+m+')-[:'+lst[a]+'{type:"'+lst[a]+'"}]->('+lst[a]+'_'+n+')'
			
			fp2.write(s+"\n")
			


