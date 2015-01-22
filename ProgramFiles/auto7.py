'''This program converts the list of authors into CypherRelations
'''


import re
fp1 = open('Relat.nt','r')
fp2 = open('Types.cyp','a')

for i in fp1.readlines():
	if 'http://purl.org/ontology/bibo/authorList' in i:
		end = 10
		cnt = 0
		s=''
		m=""
		while cnt<2:
			if i[end] == '<':
				cnt+=1
			end+=1
		while i[end] is not '>':
			m+=i[end]
			end+=1
		s= 'CREATE ('
		for j in m[45:]:
			if j.isalnum():
				s+=j
			else:
				s+='_'		
		s+=':authorList {identifier:"' + m[45:]+'"}) \n'
		fp2.write(s)
		fp3 = open('Relat.nt','r')
		for j in fp3.readlines():
			mm = m+'> <h'
			if mm in j:
				x = "CREATE ("
				end = 46
				while j[end] is not '>':
					end+=1
				for d in j[46:end]:
					if d.isalnum():
						x+=d
					else:
						x+='_'
				
				x+=')-[:author'
				t= re.search("rdf-syntax-ns#_",j)
				end = t.start()+15
				while j[end] is not '>':
					x+=j[end]	
					end+=1	
				x+='{type:"author"}]->('
				end+=48
				while j[end] is not '>':
					if j[end].isalnum():
						x+=j[end]
					else:
						x+='_'
					end+=1
				x+=')\n'
				fp2.write(x)

