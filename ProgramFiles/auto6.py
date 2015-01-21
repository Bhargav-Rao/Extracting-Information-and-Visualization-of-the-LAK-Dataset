'''This program converts the created homepage links to relations 
'''


fp1 = open("Relat.nt","r")
fp2 = open("Types.cyp","a")

for i in fp1.readlines():
	if 'http://xmlns.com/foaf/0.1/homepage' in i:
		m = ""
		end = 46
		while i[end] is not '>':
			if i[end].isalnum() :
				m+=i[end]
			else:
				m+='_'
			end+=1
		n=""
		end = -1
		while i[end] is not '<':
			end-=1
		for j in i[end+1:-4]:
			if j.isalnum() :
				n+=j
			else:
				n+='_'
		fp2.write("CREATE ("+m+')-[:homepage {type : "homepage"}]->('+n+')\n')

