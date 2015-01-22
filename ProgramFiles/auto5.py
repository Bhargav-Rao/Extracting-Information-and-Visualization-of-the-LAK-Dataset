'''This program creates new nodes for homepages
'''

fp1 = open('homepg.nt','r')
fp2 = open('Types.cyp','a')


for i in fp1.readlines():
	s=""
	end = -1
	while i[end] is not '<':
		end-=1
	for j in i[end+1:-4]:
		if j.isalnum():
			s+=j
		else:
			s+='_'
	
	fp2.write('CREATE (' + s + ':homepage {identifier : "'+ i[end+1:-4]+ '"})\n')



