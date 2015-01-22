'''This program converts all the data sorted out into nodes
'''

import sys
import re
fp1 = open("Types.nt","r")
fp2 = open("Types.cyp","w")
#Convert all the rdf:type into new nodes
for i in fp1.readlines():
	fp2.write("CREATE (")
	j=46
	while i[j] is not '>':
		if i[j].isalnum() or i[j] == '_':
			fp2.write(i[j])
		else:
			fp2.write('_')
		j+=1
	rgtmrk = j
	prevtype = i[46:rgtmrk]
	fp2.write(':')
	j=len(i)-1
	while True:
		if (i[j] == '#'):
			break
		elif (i[j] == '/'):
			break
		j-=1
	fp2.write(i[j+1:-4]+' { identifier : "' + prevtype +'"' )
	fp3 = open("Nodes.nt","r")
	cnt = 0
	fst = -1
	for k in fp3.readlines():
		if k[46:rgtmrk+1] == (prevtype+">"):
			'''The code for the nodes begin here'''
			fst+=1
			#if fst is not 1:
			fp2.write (" , ")
			strt = rgtmrk +3
			while k[strt] is not ">":
				strt+=1
			while True:
				if (k[strt] == '#'):
					break
				elif (k[strt] == '/'):
					break
				strt-=1
			strt+=1
			while k[strt] is not '>':
				fp2.write(k[strt])
				strt +=1
			end=len(k)-1
			while True:
				if k[end] is '"':
					break
				end-=1
			fp2.write (" : " + k[strt+2:end+1] )
	fp2.write("} ) \n")	
fp2.close()



