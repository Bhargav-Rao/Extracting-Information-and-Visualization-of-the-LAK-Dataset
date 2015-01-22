import copy
import csv
import sys
#log = open("test.log","w")
reload(sys)  
sys.setdefaultencoding('utf8')
a = dict()
d = dict()
GUILIST = []
def parse(getlist, number):
	with open('export.csv','rb') as csvfile:
		
		s = csv.reader(csvfile,delimiter = ',',quotechar = '"')
		fstln = 00
		fst = []
		'''
		getlist = ["label" ,"identifier"]
		
		params = s.next()
		dics = s.next()
		
		for i in range (len(params)):
				if (str(type(eval(dics[i]))) == "<type 'dict'>"):
					if (len(eval(dics[i]).keys()) == 6):
						fst.append('a')
					elif (len(eval(dics[i]).keys()) == 7):
						fst.append('a')
					elif (len(eval(dics[i]).keys()) == 3):
						fst.append('o')
					elif (len(eval(dics[i]).keys()) == 5):
						fst.append('p')
					elif (len(eval(dics[i]).keys()) == 2):
						fst.append('r')'''
		#print (fst)
		
		for r in s:
			fstln+=1
			
			if fstln>1:
				
					tup = 0
				
					#for j in r:
					j = list(r)[number]
					tup+=1
					#log.write(j+"\n")
					
					if (len(getlist)==1):				
						#print "Tuple --- "+str(tup)+"\n\n\n"
						TEMPLIST = []
						if str(j) == '{}':
							print ("Null")
						else:
							cnd = 0
							a= eval(j)
							typ = str(type(a))
							#print (typ)
							if (typ == "<type 'dict'>"):	
								col_size = 69
								sl_num = 6
								if  (fstln == 2):
									print ('-'*77)
									sys.stdout.write("| ")
									sys.stdout.write("{:<5}".format("Slno") )
									for i in sorted(a.keys()):
										if (i in getlist):
											sys.stdout.write("| ")
											sys.stdout.write("{:<67}".format(i) )
											d[cnd] = i
											cnd+=1		
																			
									print ("| ")	
									print ('-'*77)
								
								sys.stdout.write("| ")
								sys.stdout.write("{:<5}".format(str(fstln-1) ))
								for i in getlist:
								   if ((i not in a.keys())):	
								      a[i] = "null"
								for i in sorted(a.keys()):
									if (i in getlist):
										sys.stdout.write("| ")
										let = ("%r"%a[i].encode('utf-8'))[1:-1]
										value = a[i]
										TEMPLIST.append(value)
										if (len(let) <= 67):

											sys.stdout.write("{:<67}".format(("%r"%a[i].encode('utf-8'))[1:-1] ))
										else:
											let = ("%r"%a[i].encode('utf-8'))[1:-1]
											while (len(let) > 67):
													sys.stdout.write("{:<67}".format(let[:67]) )
													if (i==d[0]):
														print ("| ")
														sys.stdout.write ("| "+" "*5+"| ")
													let = let [67:]
											sys.stdout.write("{:<67}".format(let) )
															
								print ("| ")	
								print ('-'*77)
								GUILIST.append(TEMPLIST)
	
	
						
					elif (len(getlist)==2):
						#print "Tuple --- "+str(tup)+"\n\n\n"
						TEMPLIST = []
						if str(j) == '{}':
							print ("Null")
						else:
							
							cnd = 0
							a= eval(j)
							typ = str(type(a))
							#print (typ)
							if (typ == "<type 'dict'>"):	
								col_size = 32
								sl_num = 6
								if  (fstln == 2):
									print ('-'*77)
									sys.stdout.write("| ")
									sys.stdout.write("{:<6}".format("Slno") )
									
									for i in sorted(a.keys()):
										if (i in getlist):
											sys.stdout.write("| ")
											sys.stdout.write("{:<32}".format(i) )
											d[cnd] = i
											cnd+=1
											
									print ("| ")	
									print ('-'*77)
								sys.stdout.write("| ")
								sys.stdout.write("{:<6}".format(str(fstln-1) ))
								for i in getlist:
								   if ((i not in a.keys())):	
								      a[i] = "null"
								for i in sorted(a.keys()):
									if (i in getlist):
										sys.stdout.write("| ")
										let = ("%r"%a[i].encode('utf-8'))[1:-1]
										value = a[i]
										TEMPLIST.append(value)
										if (len(let) <= 32):
											sys.stdout.write("{:<32}".format(("%r"%a[i].encode('utf-8'))[1:-1] ))
										else:
											let = ("%r"%a[i].encode('utf-8'))[1:-1]
											while (len(let) > 32):
													
													sys.stdout.write("{:<32}".format(let[:32]) )
													#if (fst[tup-1] == 'a'):
													
													if (i==d[0]):
														print ("| "+" "*32+"| ")
														sys.stdout.write ("| "+" "*6+"| ")
													elif (i==d[1]):
														print ("| ")
														sys.stdout.write ("| "+" "*6+"| "+" "*32+"| ")
													let = let [32:]
											sys.stdout.write("{:<32}".format(let) )
								print ("| ")	
								print ('-'*77)
								GUILIST.append(TEMPLIST)
					elif (len(getlist)==3):				
						#print "Tuple --- "+str(tup)+"\n\n\n"
						TEMPLIST = []
						if str(j) == '{}':
							print ("Null")
						else:
							cnd = 0
							a= eval(j)
							typ = str(type(a))
							#print (typ)
							if (typ == "<type 'dict'>"):	
								col_size = 43
								sl_num = 6
								if  (fstln == 2):
									print ('-'*77)
									sys.stdout.write("| ")
									sys.stdout.write("{:<5}".format("Slno") )
									for i in sorted(a.keys()):
										if (i in getlist):
											sys.stdout.write("| ")
											sys.stdout.write("{:<21}".format(i) )
											d[cnd] = i
											cnd+=1		
																			
									print ("| ")	
									print ('-'*77)
								
								sys.stdout.write("| ")
								sys.stdout.write("{:<5}".format(str(fstln-1) ))
								for i in getlist:
								   if ((i not in a.keys())):	
								      a[i] = "null"
								
								for i in sorted(a.keys()):
									if (i in getlist):
										sys.stdout.write("| ")
										let = ("%r"%a[i].encode('utf-8'))[1:-1]
										value = a[i]
										TEMPLIST.append(value)
										if (len(let) <= 21):
											sys.stdout.write("{:<21}".format(("%r"%a[i].encode('utf-8'))[1:-1] ))
										else:
											let = ("%r"%a[i].encode('utf-8'))[1:-1]
											
											while (len(let) > 21):
													sys.stdout.write("{:<21}".format(let[:21]) )
													if (i==d[0]):
														print ("| "+" "*21+"| "+" "*21+"| ")
														sys.stdout.write ("| "+" "*5+"| ")
													elif (i==d[1]):
														print ("| "+" "*21+"| ")
														sys.stdout.write ("| "+" "*5+"| "+" "*21+"| ")
													elif (i==d[2]):
														print ("| ")
														sys.stdout.write ("| "+" "*5+"| "+" "*21+"| "+" "*21+"| ")
													let = let [21:]
											sys.stdout.write("{:<21}".format(let) )
															
								print ("| ")	
								print ('-'*77)
								GUILIST.append(TEMPLIST)
	
	
	
					elif (len(getlist)==4):				
						#print "Tuple --- "+str(tup)+"\n\n\n"
						TEMPLIST = []
						if str(j) == '{}':
							print ("Null")
						else:
							cnd = 0
							a= eval(j)
							typ = str(type(a))
							#print (typ)
							if (typ == "<type 'dict'>"):	
								col_size = 32
								sl_num = 6
								if  (fstln == 2):
									print ('-'*77)
									sys.stdout.write("| ")
									sys.stdout.write("{:<6}".format("Slno") )
									for i in sorted(a.keys()):
										if (i in getlist):
											sys.stdout.write("| ")
											sys.stdout.write("{:<15}".format(i) )
											d[cnd] = i
											cnd+=1		
																			
									print ("| ")	
									print ('-'*77)
								
								sys.stdout.write("| ")
								sys.stdout.write("{:<6}".format(str(fstln-1) ))
								for i in getlist:
								   if ((i not in a.keys())):	
								      a[i] = "null"
								
								for i in sorted(a.keys()):
									if (i in getlist):
										sys.stdout.write("| ")
										let = ("%r"%a[i].encode('utf-8'))[1:-1]
										value = a[i]
										TEMPLIST.append(value)
										if (len(let) <= 15):
											sys.stdout.write("{:<15}".format(("%r"%a[i].encode('utf-8'))[1:-1] ))
										else:
											let = ("%r"%a[i].encode('utf-8'))[1:-1]
											while (len(let) > 15):
													sys.stdout.write("{:<15}".format(let[:15]) )
													if (i==d[0]):
														print ("| "+" "*15+"| "+" "*15+"| "+" "*15+"| ")
														sys.stdout.write ("| "+" "*6+"| ")
													elif (i==d[1]):
														print ("| "+" "*15+"| "+" "*15+"| ")
														sys.stdout.write ("| "+" "*6+"| "+" "*15+"| ")
													elif (i==d[2]):
														print ("| "+" "*15+"| ")
														sys.stdout.write ("| "+" "*6+"| "+" "*15+"| "+" "*15+"| ")
													elif (i==d[3]):
														print ("| ")
														sys.stdout.write ("| "+" "*6+"| "+" "*15+"| "+" "*15+"| "+" "*15+"| ")
													let = let [15:]
											sys.stdout.write("{:<15}".format(let) )
															
								print ("| ")	
								print ('-'*77)
								GUILIST.append(TEMPLIST)
	
	
			else:
				#fst = r
				#print fst
				pass
				
fp = open ("Intermediate1")
i = fp.readlines()
#print (i)
l = eval(i[0])
GUILIST.append(sorted(l))
parse (l,0)
final = open("Intermediate3","w")
final.write(repr(GUILIST))
GUILIST = []
if len(i) == 2:
    final.write("\n")
    l = eval(i[1])
    GUILIST.append(sorted(l))
    parse (l,1)
    final.write(repr(GUILIST))

final.close()
