'''This program is a small patch to make it work for the dataset of 2014 (as it was originally made for the 2013 dataset)
'''

fp2 = open("sameas.nt","r")
fp3 = open("Types.cyp","a")
import re
authors = {'http://www.w3.org/2002/07/owl#sameAs' : 'sameAs'}

for i in fp2.readlines():
    if 'http://www.w3.org/2002/07/owl#sameAs' in i:
    	  f = re.match("<(.*)>\t<(.*)>\t<(.*)>",i)
    	  if f:
    	      s = f.groups(0)[0]
    	      o = f.groups(0)[1]
    	      p = f.groups(0)[2]    
    	      if 'person' in s or 'organization' in s:
    	           	newp = ""
    	           	for i in p:
    	           	     if i.isalnum():
    	           	          newp+=i
    	           	     else:
    	           	          newp+='_'
    	           	fp3.write('CREATE ('+newp+':resource { identifier : "'+p+'"})\n')
    	           	news = ""
    	           	for i in s[45:]:
    	           	     if i.isalnum():
    	           	          news+=i
    	           	     else:
    	           	          news+='_' 
    	           	fp3.write("CREATE ("+news+")-[:sameAs{type:\"sameAs\"}]->("+newp+")\n")	  	           	
    	      else:
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
    	            else:
    	           		fp3.write("CREATE ("+m+")-[:sameAs{type:\"sameAs\"}]->("+n+")\n")



#fp3.write("CREATE ("+m+")-[:sameAs{type:\"sameAs\"}]->("+n+")\n")	
fp3.close()
