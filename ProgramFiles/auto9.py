'''This program creates batches of 600 relations each, as the memory on induvidual systems is highly restricted
'''

fp1 = open ("Relations.cyp","r")
count = 1
countlines = 0
fp2 = open("./batches/R1.cyp","w")
for i in fp1.readlines():
	countlines+=1
	fp2.write(i)
	if (countlines == 600):
		count +=1
		countlines = 0
		fp2 = open("./batches/R"+str(count)+".cyp","w")
	
	
