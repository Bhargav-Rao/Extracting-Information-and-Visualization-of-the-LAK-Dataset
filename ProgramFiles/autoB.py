'''This program finds the variables declared in the nodes and matches them with the segregated relations
'''

import re
import os 
import shutil

lst = []

for i in os.listdir("./batches"):
	if (i[0] == 'R'):
		lst.append(i)
lstcount = 0

for fil in sorted(lst):
	lstcount +=1
	fp3 = open ("R"+str(lstcount)+".cyp","w")
	print "R"+str(lstcount)+".cyp"+" created"
	fp1 = open ("./batches/"+fil,"r")
	for i in fp1.readlines():
		label = re.search("(\(.*\)).*(\(.*\))",i)
		a =  (label.groups())
		for j in a:
			key = j[1:-1]+":"
			fp2 = open ("Nodes.cyp","r")
			for k in fp2.readlines():
				if key in k:
					pos = re.search ("identifier",k)
					n=pos.end()
					while not (k[n]=='"'):
						n+=1
					n+=1
					m=n
					while not (k[m]=='"'):
						m+=1
					fp3.write("MATCH "+key[:-1]+" WHERE "+key[:-1]+".identifier = "+ k[n-1:m+1]+"\n")
		fp3.write(i)
	fp1 = open ("./batches/"+fil,"r")				
	'''for i in fp1.readlines():
		fp3.write(i)'''
	
	fp3.close()				


    


