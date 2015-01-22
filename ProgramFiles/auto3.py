'''This program converts the resources needing dbpedia links into new nodes
'''
import re
fp1 = open("subject.nt","r")
fp2 = open("Types.cyp","a")

final = set()

for i in fp1.readlines():
	s=""
	t= re.search("<http://dbpedia.org/resource/",i)
	s=i[t.start()+29:-4]
	final.add(s)
	
for i in sorted(final):
	s=""
	for j in i:
		if j.isalnum() or j == '_':
			s=s+j
		else:
			s=s+'_'
	fp2.write("CREATE (subject_" + s +  ':subject { identifier : "http://dbpedia.org/resource/'+i+'"  , name : "'+i+'"})\n')


fp1 = open("based.nt","r")

final = set()

for i in fp1.readlines():
	s=""
	t= re.search("<http://dbpedia.org/resource/",i)
	s=i[t.start()+29:-4]
	final.add(s)
	
for i in sorted(final):
	s=""
	for j in i:
		if j.isalnum() or j == '_':
			s=s+j
		else:
			s=s+'_'
	fp2.write("CREATE (based_near_" + s +  ':based_near { identifier : "http://dbpedia.org/resource/'+i+'"  , name : "'+i+'"})\n')
	

fp1 = open("LAK-DATASET-DUMP.nt","r")

for i in fp1.readlines():
	if 'http://data.semanticweb.org/ns/swc/ontology#completeGraph' in i:
		t = re.search('http://data.semanticweb.org/ns/swc/ontology#completeGraph',i)
		start = t.end() + 48
		s=""
		iden=""
		for j in i[start:-4]:
			if j.isalnum() or j == '_':
				s=s+j
			else:
				s=s+'_'
			iden = iden + j
		fp2.write('CREATE (' + s+':completeGraph { identifier : "' + iden + '"})\n')
			
