import neo4j

connection = neo4j.connect("http://localhost:7474")

def printfile(d):
	fp.write('"{')
	cnt = 0
	for k in (sorted(d.keys())):
		k = k.replace ('"',"'")
		d[k] = d[k].replace ('"',"'")
		cnt+=1  
		if cnt>1:
			fp.write(",")  				
		fp.write('""'+("%r"%k.encode('utf-8'))[1:-1]+'"":""'+("%r"%d[k].encode('utf-8'))[1:-1]+'""')


cursor = connection.cursor()
fp = open("export.csv","w")
fp2 = open("Intermediate2")
x = str(fp2.readline().strip('\n'))

if "DELETE" not in x:
	zz =cursor.execute(x)
	num = True
	for i in zz:
		c=0
		if num:
			fp.write("a")
			for ab in range(1,len(i)):
				fp.write(",a")
			fp.write("\n")
			num = False
		for j in i:
			if (len(i) == 1):
				d=eval(str(j))
				printfile(d)
				fp.write('}"\n')
			else:
				
				d = eval(str(j))
				printfile(d)
				c+=1
				#print (c,len(i))
				#print (i[0])
				
				if not (c == len(i)):
					fp.write('}",')
					
				else:
					#print ("end")
					fp.write('}"\n')
	    		
fp.close()

    		
