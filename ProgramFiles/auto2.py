'''This program converts all the normal relationships into cypher text
'''

fp2 = open("Relat.nt","r")
fp3 = open("Types.cyp","a")


authors = {'http://purl.org/dc/elements/1.1/creator':'creator',
'http://xmlns.com/foaf/0.1/maker':'maker',
'http://data.semanticweb.org/ns/swc/ontology#isPartOf':'isPartOf',
'http://xmlns.com/foaf/0.1/made':'made',
'http://xmlns.com/foaf/0.1/member':'member',
'http://data.linkededucation.org/ns/linked-education.rdf#hasReference':'hasReference',
'http://swrc.ontoware.org/ontology#affiliation' : 'affiliation',
'http://data.semanticweb.org/ns/swc/ontology#completeGraph' : 'completeGraph',
'http://data.semanticweb.org/ns/swc/ontology#hasRelatedDocument' : 'hasRelatedDocument',

'http://data.semanticweb.org/ns/swc/ontology#hasPart' : 'hasPart',
'http://data.semanticweb.org/ns/swc/ontology#isPartOf' : 'isPartOf',
'http://data.semanticweb.org/ns/swc/ontology#relatedToEvent' : 'relatedToEvent',
'http://purl.org/ontology/bibo/authorList':'authorList',
'http://purl.org/dc/terms/hasPart':'hasPart',
'http://purl.org/dc/terms/isPartOf':'isPartOf',
'http://ns.nature.com/terms/hasCitation':'hasCitation'
}
for a in authors.keys():
	fp2.seek(0)
	for i in fp2.readlines():
		if a in i:
			
			cnt = 0
			end = -1
			while cnt<1:
				if i[end] == '<':
					cnt+=1
				end-=1
			end += 45
			m=""
				
			for j in i[end+2:-4]:
				if j.isalnum() or j == '_':
					m=m+j
				else:
					m=m+'_'
			
			end = 43
			while i[end] is not '>':
				end+=1
			n=""
			for j in i[46:end]:
				if j.isalnum() or j == '_':
					n=n+j
				else:
					n=n+'_'	
			if (authors[a] == 'creator' or authors[a] == 'maker' or authors[a] == 'member' or authors[a] == 'authorList'):
				fp3.write("CREATE ("+n+")-[:"+authors[a]+"{type:\""+authors[a]+"\"}]->("+m+")\n")	
			else:
				fp3.write("CREATE ("+m+")-[:"+authors[a]+"{type:\""+authors[a]+"\"}]->("+n+")\n")	
fp3.close()
