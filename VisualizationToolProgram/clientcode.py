
options = {"Proceedings":[ "month","series","booktitle","identifier","year"],
"Person":[ "name","firstName","lastName","label","mbox_sha1sum","identifier"],
"InProceedings":["body","title","abstract","label","month","year","identifier"  ],   
"Organization":[ "identifier","name","label"],
"Reference":["identifier","text"]}

relations = [
["creator","Person","InProceedings"],
["maker","Person","InProceedings"],
["made","Person","InProceedings"],
["member","Person","Organization"],
["affiliation","Person","Organization"],
["hasPart","Proceedings","InProceedings"],
["hasReference","Reference","InProceedings"],
["sameAs","Reference","Reference"]
]


getrequest = []
getaddl = None
query = ""
chk = input ("Enter 1 for node and 2 for relation\n")
#chk = '1'
if (chk=="2"):
	
	print ("Enter the node1 for the relation")
	for i,x in enumerate(sorted(options.keys())):
		print (str(i+1)+" "+x)
	op1 = int(input("\n"))
	op1lab = list(sorted(options.keys()))[op1-1]
	print ("Enter the node2 for the relation")
	for i,x in enumerate(sorted(options.keys())):
		print (str(i+1)+" "+x)
	op2 = int(input("\n"))
	op2lab = list(sorted(options.keys()))[op2-1]
	
	print ("Enter the output node required ")
	print ("1",op1lab)
	print ("2",op2lab)
	print ("3 both")
	op3 = int(input("\n"))
	op3lab = "null"
	if (op3 == 1):
		op3lab = op1lab
	elif (op3 == 2):
		op3lab = op2lab
	elif (op3 != 3):
		print ("Error")
	op3val = 0
	getrequest = []
	getaddl = None
	if (op3 != 3):
		for i,x in enumerate(sorted(options[op3lab])):
			print (str(i+1)+" "+x)
		print ("Enter number of columns required")
		num = int(input("\n"))
		while (num > 4 or num <=0):
			print ("Number of columns out of range.\nHas to be less than 4")
			num = int(input("\n"))
		print ("Enter the options")
		vals = []
		for i in range (num):
			inp = int(input())
			vals.append(inp)
		getrequest = []
		for i in vals:
			t = list(sorted(options[op3lab]))
			getrequest.append(t[i-1])
	else:
		for i,x in enumerate(sorted(options[op1lab])):
			print (str(i+1)+" "+x)
		print ("Enter number of columns required in node1")
		num = int(input("\n"))
		while (num > 4 or num <=0):
			print ("Number of columns out of range.\nHas to be less than 4")
			num = int(input("\n"))
		print ("Enter the options")
		vals = []
		for i in range (num):
			inp = int(input())
			vals.append(inp)
		for i in vals:
			t = list(sorted(options[op1lab]))
			getrequest.append(t[i-1])			
			
			
		for i,x in enumerate(sorted(options[op2lab])):
			print (str(i+1)+" "+x)
		print ("Enter number of columns required in node2")
		num = int(input("\n"))
		while (num > len(op2lab) or num > 4 or num <=0):
			print ("Number of columns out of range.\nHas to be less than 4")
			num = int(input("\n"))
		print ("Enter the options")
		vals = []
		for i in range (num):
			inp = int(input())
			vals.append(inp)
		getaddl = []
		for i in vals:
			t = list(sorted(options[op2lab]))
			getaddl.append(t[i-1])				
    
	print ("Enter number of rows to limit (0 for no upperbound)")
	lim = int(input("\n"))
	count = 0
	consta = " WHERE "
	while True:
		count +=1
		print ("Want to add conditions (0 for no condition)")
		con = int(input("\n"))
		if not (con==0):
			if count >1:
				consta+=" and "
			nodlab = input("Enter 1 to add condition for node 1 else 2 to add condition for node 2\n")
			if (nodlab == "1"):
				for i,x in enumerate(sorted(options[op1lab])):
					print (str(i+1)+" "+x)
				connum = int(input("Enter choice\n"))
				concon = input ("Enter condition\n")
				t = list(sorted(options[op1lab]))
				consta = consta + "a."
			elif (nodlab == "2"):
				for i,x in enumerate(sorted(options[op2lab])):
					print (str(i+1)+" "+x)
				connum = int(input("Enter choice\n"))
				concon = input ("Enter condition\n")
				t = list(sorted(options[op2lab]))
				consta = consta + "b."
			consta = consta +t[connum-1]+'= "'+concon+'"'
		else:
			break	
	rel = ""
	relas = []
	
	for l in relations:
		 for i in l[1:]:
		     if i == op1lab or i == op2lab:
		         pass
		     else: 
		         break
		 else:
		     relas.append(l[0])
	if relas is []:
	    rel = ''
	else:
	    print ("Do enter type of relation (Note all will return same value)")
	    for i,x in enumerate(sorted(relas)):
	    	    print (str(i+1)+" "+x)
	    relval = -1
	    while relval not in range(len(relas)+1):
	    	    relval = int(input("Enter choice (0 for all) \n"))
	    if relval is 0:
	        rel = ''
	    else: 
	        rel = list(sorted(relas))[relval-1]	    
	    rel = ":`{}`".format(rel)
	    
	    
	query = "MATCH (a:"+op1lab+")-["+rel+"]-(b:"+op2lab+")"
	if len(consta) > 7:
		query+=consta
	if (op3 == 3):
		query+= " RETURN a,b"
	elif (op3 == 1):
		query+= " RETURN a"
	elif (op3 == 2):
		query+= " RETURN b"
	if lim>0:
		query = query +" LIMIT "+ str (lim)
	
	
elif(chk=="1"):
	print ("Enter which node to select")

	for i,x in enumerate(sorted(options.keys())):
		print (str(i+1)+" "+x)
	op1 = int(input("\n"))
	while (op1>5 or op1<1):
		op1 = int(input("Enter the SL no (between 1 and 5)\n"))
	
	op1lab = list(sorted(options.keys()))[op1-1]
	for i,x in enumerate(sorted(options[op1lab])):
		print (str(i+1)+" "+x)
	print ("Enter number of columns required")
	num = int(input("\n"))
	while (num > 4 or num <=0):
		print ("Number of columns out of range.\nHas to be less than 4")
		num = int(input("\n"))	
	print ("Enter the options")
	vals = []
	for i in range (num):
		vals.append(int(input()))

	for i in vals:
		t = list(sorted(options[op1lab]))
		getrequest.append(t[i-1])
	print ("Enter number of rows to limit (0 for no upperbound)")
	lim = int(input("\n"))
	consta = " WHERE "
	count = 0
	while True:
		count +=1
		print ("Want to add conditions (0 for no condition)")
		con = int(input("\n"))
		if not (con==0):
			if count >1:
				consta+=" and "
			for i,x in enumerate(sorted(options[op1lab])):
				print (str(i+1)+" "+x)
			connum = int(input("Enter choice\n"))
			concon = input ("Enter condition\n")
			t = list(sorted(options[op1lab]))
			consta = consta + "a."+t[connum-1]+'= "'+concon+'"'
		else:
			break
	
	
	query = "MATCH (a:"+op1lab+")"
	if len(consta) > 7:
		query+=consta
	
	query += " RETURN a " 
	if lim>0:
		query = query +"LIMIT "+ str (lim)
	
	
	
	
fp = open("Intermediate2","w")
fp.write(query)
fp.close
fp = open("Intermediate1","w")
fp.write(str(getrequest))
if getaddl:
    fp.write("\n"+str(getaddl))
fp.close
