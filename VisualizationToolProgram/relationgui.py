from tkinter import *
mapping = { "Month": "month","Series":"series", "Book Title":"booktitle", "Identifier":"identifier", "Year":"year", "Name":"name", "First Name":"firstName", "Last Name":"lastName", "Label": "label","mbox_sha1sum":"mbox_sha1sum" ,"Body":"body", "Title":"title" ,"Abstract":"abstract"}
root = Tk()
#root.attributes('-fullscreen', True)
root.geometry("1300x600")

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



welcome_label = Label(root,text = "Extraction of data and Visualization of LAK Dataset",font = 200)
welcome_label.pack()
var1=IntVar()
var2=IntVar()
var3=IntVar()	#this is for asking the user if he wants to add condition if it's value is 1 than he wants if it is 2 than he doesn't
list1=[]	#this list contains list of all the properties selected by the user for node1
list2=[]	#this list contains list of all the properties selected by the user for node2
cond1=[]	
cond2=[]
value1=[]	#this is list of list where in each sublist first element is property and 2nd is it's value entered for the condition in node1
value2=[]	#this is list of list where in each sublist first element is property and 2nd is it's value entered for the condition in node2
out=StringVar()			#this is selection b/w two nodes i.e. to have both nodes or either of the two
reltype=StringVar()			#this is type of the relation
limiter = Spinbox(root, values=(0,5,10,15,20,25,50,100))
ins1=''			#this is node1 selected
ins2=''			#this is node2 selected
z=0				#this is the limit value

def set_query():
    fp = open("Intermediate1",'w')
    global list1,list2
    list1 = [mapping[i] for i in list1]
    fp.write(str(list1))
    
    if list2:
        list2 = [mapping[i] for i in list2]
        fp.write("\n"+str(list2))
    fp.close()
    #MATCH (a:InProceedings)-[:`creator`]-(b:Person) RETURN a,b
    query = "MATCH (a:{})-[".format(ins1)
    if reltype.get() != 'all':
        query += ":`{}`".format(reltype.get())
    query += "]-(b:{}) ".format(ins2)
    
    conditions = []
    for i in value1:
        if i[1]:
            conditions.append('a.{} = "{}"'.format(i[0],i[1]))
    for i in value2:
        if i[1]:
            conditions.append('b.{} = "{}"'.format(i[0],i[1]))
    
    if conditions:
        query += "WHERE {} ".format((" and ".join(conditions)))
    #print ("out",out.get())
    if out.get() == "Both":
        query += "RETURN a,b"
    elif out.get() == ins1:
        query += "RETURN a"
    else:
        query += "RETURN b"
    if z != '0':
        query += " LIMIT {}".format (z)
    #print (query)
    fp = open("Intermediate2",'w')
    fp.write(query)
    fp.close()    
    root.destroy()

def cond():
	global value1,list1
	global value2,list2
	i1=iter(cond1)
	i2=iter(cond2)
	#root.destroy()
	root2=Tk()
	root2.geometry("600x500")
	label1=Label(root2,text="Enter the conditions for FIRST NODE",font=200)
	label1.pack()
	label1.place(bordermode=INSIDE,x=0,y=30)
	try:
		l1=Label(root2,text=next(i1)+':',font=200)
		l1.pack()
		l1.place(bordermode=INSIDE,x=0,y=70)
		t1=Entry(master=root2)
		t1.pack()
		t1.place(bordermode=INSIDE,x=120,y=70)
		l2=Label(root2,text=next(i1)+':',font=200)
		l2.pack()
		l2.place(bordermode=INSIDE,x=0,y=100)
		t2=Entry(master=root2)
		t2.pack()
		t2.place(bordermode=INSIDE,x=120,y=100)
		l3=Label(root2,text=next(i1)+':',font=200)
		l3.pack()
		l3.place(bordermode=INSIDE,x=0,y=130)
		t3=Entry(master=root2)
		t3.pack()
		t3.place(bordermode=INSIDE,x=120,y=130)
		l4=Label(root2,text=next(i1)+':',font=200)
		l4.pack()
		l4.place(bordermode=INSIDE,x=0,y=160)
		t4=Entry(master=root2)
		t4.pack()
		t4.place(bordermode=INSIDE,x=120,y=160)
		l5=Label(root2,text=next(i1)+':',font=200)
		l5.pack()
		l5.place(bordermode=INSIDE,x=0,y=190)
		t5=Entry(master=root2)
		t5.pack()
		t5.place(bordermode=INSIDE,x=120,y=190)
		l6=Label(root2,text=next(i1)+':',font=200)
		l6.pack()
		l6.place(bordermode=INSIDE,x=0,y=220)
		t6=Entry(master=root2)
		t6.pack()
		t6.place(bordermode=INSIDE,x=120,y=220)
		l7=Label(root2,text=next(i1)+':',font=200)
		l7.pack()
		l7.place(bordermode=INSIDE,x=0,y=250)
		t7=Entry(master=root2)
		t7.pack()
		t7.place(bordermode=INSIDE,x=120,y=250)
	except StopIteration:
		pass
	label2=Label(root2,text="Enter the conditions for SECOND NODE",font=200)
	label2.pack()
	label2.place(bordermode=INSIDE,x=280,y=30)
	try:
		l11=Label(root2,text=next(i2)+':',font=200)
		l11.pack()
		l11.place(bordermode=INSIDE,x=280,y=70)
		t11=Entry(master=root2)
		t11.pack()
		t11.place(bordermode=INSIDE,x=400,y=70)
		l12=Label(root2,text=next(i2)+':',font=200)
		l12.pack()
		l12.place(bordermode=INSIDE,x=280,y=100)
		t12=Entry(master=root2)
		t12.pack()
		t12.place(bordermode=INSIDE,x=400,y=100)
		l13=Label(root2,text=next(i2)+':',font=200)
		l13.pack()
		l13.place(bordermode=INSIDE,x=280,y=130)
		t13=Entry(master=root2)
		t13.pack()
		t13.place(bordermode=INSIDE,x=400,y=130)
		l14=Label(root2,text=next(i2)+':',font=200)
		l14.pack()
		l14.place(bordermode=INSIDE,x=280,y=160)
		t14=Entry(master=root2)
		t14.pack()
		t14.place(bordermode=INSIDE,x=400,y=160)
		l15=Label(root2,text=next(i2)+':',font=200)
		l15.pack()
		l15.place(bordermode=INSIDE,x=280,y=190)
		t15=Entry(master=root2)
		t15.pack()
		t15.place(bordermode=INSIDE,x=400,y=190)
		l16=Label(root2,text=next(i2)+':',font=200)
		l16.pack()
		l16.place(bordermode=INSIDE,x=280,y=220)
		t16=Entry(master=root2)
		t16.pack()
		t16.place(bordermode=INSIDE,x=400,y=220)
		l17=Label(root2,text=next(i2)+':',font=200)
		l17.pack()
		l17.place(bordermode=INSIDE,x=280,y=250)
		t17=Entry(master=root2)
		t17.pack()
		t17.place(bordermode=INSIDE,x=400,y=250)
	except StopIteration:
		pass
	def get():
		i1=iter(cond1)
		i2=iter(cond2)
		global value1,value2
		try:
			next(i1)
			value1.append([mapping[l1.cget("text")[:-1]],t1.get()])
			next(i1)
			value1.append([mapping[l2.cget("text")[:-1]],t2.get()])
			next(i1)
			value1.append([mapping[l3.cget("text")[:-1]],t3.get()])
			next(i1)
			value1.append([mapping[l4.cget("text")[:-1]],t4.get()])
			next(i1)
			value1.append([mapping[l5.cget("text")[:-1]],t5.get()])
			next(i1)
			value1.append([mapping[l6.cget("text")[:-1]],t6.get()])
			next(i1)
			value1.append([mapping[l7.cget("text")[:-1]],t7.get()])
		except StopIteration:
			pass
		try:
			next(i2)
			value2.append([mapping[l11.cget("text")[:-1]],t11.get()])
			next(i2)
			value2.append([mapping[l12.cget("text")[:-1]],t12.get()])
			next(i2)
			value2.append([mapping[l13.cget("text")[:-1]],t13.get()])
			next(i2)
			value2.append([mapping[l14.cget("text")[:-1]],t14.get()])
			next(i2)
			value2.append([mapping[l15.cget("text")[:-1]],t15.get()])
			next(i2)
			value2.append([mapping[l16.cget("text")[:-1]],t16.get()])
			next(i2)
			value2.append([mapping[l17.cget("text")[:-1]],t17.get()])
		except StopIteration:
			pass
		#print(value1)
		#print(value2)
		root2.destroy()
		set_query()
	button = Button(root2,text="SUBMIT",height = 2,width = 10,command = get)
	button.pack()
	button.place(bordermode=INSIDE, x=200, y=310)
	root2.mainloop()
	
def subn():
	if(var3.get()==1):
		button = Button(root,text="SUBMIT",height = 2,width = 10,command = cond)
		button.pack()
		button.place(bordermode=INSIDE, x=600, y=500)
	else:
		button = Button(root,text="SUBMIT",height = 2,width = 10,command = set_query)
		button.pack()
		button.place(bordermode=INSIDE, x=600, y=500)
			
def new():
	global z
	z=limiter.get()
	#print(z)
	limiter.config(state = DISABLED)
	Rc1.config(state = DISABLED)
	Rc2.config(state = DISABLED)
	relchoice=["all"]
	reltype.set(relchoice[0])
	def sub(event):
		if(var3.get()==1):
			button = Button(root,text="SUBMIT",height = 2,width = 10,command = cond)
			button.pack()
			button.place(bordermode=INSIDE, x=600, y=500)
		else:
			button = Button(root,text="SUBMIT",height = 2,width = 10,command = set_query)
			button.pack()
			button.place(bordermode=INSIDE, x=600, y=500)
		
    #if(out.get()=="Both"):
	label=Label(root,text="Select type of Relation (NOTE all will return same value)",font=200)
	label.pack()
	label.place(bordermode=INSIDE,x=690,y=300)
	for i in range(len(relations)):
		if((ins1 in relations[i][1:]) and (ins2 in relations[i][1:])):
			relchoice.append(relations[i][0])
	reloption=OptionMenu(root,reltype,*relchoice,command=sub)
	reloption.pack()
	reloption.place(bordermode=INSIDE,x=690,y=330)
    #else:
	subn()
		
def error():
	root1=Tk()
	root1.geometry("300x125+550+350")
	label = Label(root1,text="Maximum no. of columns in the table is 4",font=200)
	label.pack()
	label.place(bordermode=INSIDE,x=0,y=25)
	button = Button(root1,text="OK",height = 1,width = 7,command = root1.destroy)
	button.pack()
	button.place(bordermode=INSIDE, x=125, y=80)
	root1.mainloop()

def fun():
	Lb1.config(state = DISABLED)
	Lb2.config(state = DISABLED)
	label = Label(root,text="Give the limit for output",font = 150,height=1)
	label2 = Label(root,text="Select 0 for no limit",font = 150,height=1)
	label.pack(side = LEFT)
	label.place(bordermode=INSIDE, x=0, y=300)
	label2.pack(side = LEFT)
	label2.place(bordermode=INSIDE, x=0, y=330)

	global limiter
	button.config(state = DISABLED)
	limiter.pack()
	limiter.place(bordermode=INSIDE, x=30, y=360)
		
	label = Label(root,text="5.Do you want to add a condition?",font = 150,height=1)
	label.pack(side = LEFT)
	label.place(bordermode=INSIDE, x=350, y=300)
	
	Rc1.pack( anchor = W,side = LEFT )
	Rc1.place(bordermode=INSIDE, x=350, y=325)

	Rc2.pack( anchor = W,side = LEFT )
	Rc2.place(bordermode=INSIDE, x=350, y=350)	
	
def sender1(event):
	global list2
	list=[]
	widget = event.widget
	selection=widget.curselection()
	for items in selection:
		if(len(list)==4):
			error()
		list.append(widget.get(items))
	
	global button	
	button = Button(root,text="OK",height = 1,width = 7,command = fun)
	button.pack()
	button.place(bordermode=INSIDE, x=1010, y=250)
	list2=list
	#print(list2)

def prop1():
	Lb1.config(state = DISABLED)
	global cond2
	label1 = Label(root,text="Select properties for Second NODE",font = 150,height=1)
	label1.pack()
	label1.place(bordermode=INSIDE, x=960, y=25)
	
	if(var2.get() == 1):
		Lb2.insert(END, "Body")
		Lb2.insert(END, "Title")
		Lb2.insert(END, "Abstract")
		Lb2.insert(END, "Label")
		Lb2.insert(END, "Month")
		Lb2.insert(END, "Year")
		Lb2.insert(END, "Identifier")
		Lb2.pack()
		Lb2.place(bordermode=INSIDE, x=960, y=50)
		Lb2.bind("<ButtonRelease-1>", sender1)
		#sender(Lb1)

	elif(var2.get() == 2):
		Lb2.insert(1, "Identifier")
		Lb2.insert(2, "Name")
		Lb2.insert(3, "Label")
		Lb2.pack()
		Lb2.place(bordermode=INSIDE, x=960, y=50)
		Lb2.bind("<ButtonRelease-1>", sender1)
			
	elif(var2.get() == 3):
		Lb2.insert(1, "Name")
		Lb2.insert(2, "First Name")
		Lb2.insert(3, "Last Name")
		Lb2.insert(4, "Label")
		Lb2.insert(5, "mbox_sha1sum")
		Lb2.insert(6, "Identifier")
		Lb2.pack()
		Lb2.place(bordermode=INSIDE, x=960, y=50)
		Lb2.bind("<ButtonRelease-1>", sender1)

	elif(var2.get() == 4):
		Lb2.insert(1, "Month")
		Lb2.insert(2, "Series")
		Lb2.insert(3, "Book Title")
		Lb2.insert(4, "Identifier")
		Lb2.insert(5, "Year")
		Lb2.pack()
		Lb2.place(bordermode=INSIDE, x=960, y=50)
		Lb2.bind("<ButtonRelease-1>", sender1)
	
	elif(var2.get() == 5):
		Lb2.insert(1, "Identifier")
		Lb2.insert(2, "Text")
		Lb2.pack()
		Lb2.place(bordermode=INSIDE, x=960, y=50)
		Lb2.bind("<ButtonRelease-1>", sender1)
			
	else:
		pass
		
def sender(event):
	global list1
	list=[]
	widget = event.widget
	selection=widget.curselection()
	for items in selection:
		if(len(list)==4):
			error()
		list.append(widget.get(items))
	
	
	
	def check():
		if(out.get()=="Both"):
			prop1()
		else:
			fun()
		button.config(state = DISABLED)
	global button

	button = Button(root,text="OK",height = 1,width = 7,command = check)
	button.pack()
	button.place(bordermode=INSIDE, x=690, y=250)
	list1=list
	#print(list1)
		
def prop():
	global cond1,out
	label1 = Label(root,text="Select properties for First NODE",font = 150,height=1)
	label1.pack()
	label1.place(bordermode=INSIDE, x=640, y=25)

	if(var1.get() == 1):
		Lb1.insert(END, "Body")
		Lb1.insert(END, "Title")
		Lb1.insert(END, "Abstract")
		Lb1.insert(END, "Label")
		Lb1.insert(END, "Month")
		Lb1.insert(END, "Year")
		Lb1.insert(END, "Identifier")
		Lb1.pack()
		Lb1.place(bordermode=INSIDE, x=640, y=50)
		Lb1.bind("<ButtonRelease-1>", sender)

	elif(var1.get() == 2):
		Lb1.insert(1, "Identifier")
		Lb1.insert(2, "Name")
		Lb1.insert(3, "Label")
		Lb1.pack()
		Lb1.place(bordermode=INSIDE, x=640, y=50)
		Lb1.bind("<ButtonRelease-1>", sender)
		
	elif(var1.get() == 3):
		Lb1.insert(1, "Name")
		Lb1.insert(2, "First Name")
		Lb1.insert(3, "Last Name")
		Lb1.insert(4, "Label")
		Lb1.insert(5, "mbox_sha1sum")
		Lb1.insert(6, "Identifier")
		Lb1.pack()
		Lb1.place(bordermode=INSIDE, x=640, y=50)
		Lb1.bind("<ButtonRelease-1>", sender)

	elif(var1.get() == 4):
		Lb1.insert(1, "Month")
		Lb1.insert(2, "Series")
		Lb1.insert(3, "Book Title")
		Lb1.insert(4, "Identifier")
		Lb1.insert(5, "Year")
		Lb1.pack()
		Lb1.place(bordermode=INSIDE, x=640, y=50)
		Lb1.bind("<ButtonRelease-1>", sender)
		
	elif(var1.get() == 5):
		Lb1.insert(1, "Identifier")
		Lb1.insert(2, "Text")
		Lb1.pack()
		Lb1.place(bordermode=INSIDE, x=640, y=50)
		Lb1.bind("<ButtonRelease-1>", sender)
	else:
		prop1()
	
def output():
	R11.config(state = DISABLED)
	R12.config(state = DISABLED)
	R13.config(state = DISABLED)
	R14.config(state = DISABLED)
	R15.config(state = DISABLED)
	label=Label(root,text="Select the Nodes you want at the output",font=200)
	label.pack()
	label.place(bordermode=INSIDE,x=150,y=220)
	out.set("Both")
	global ins1, ins2, cond1, cond2
	def output1(event):
	    
		if(out.get()==ins2):
			prop1()
		else:
			prop()
		option.config(state = DISABLED)

		
	if(var1.get()==1):
		ins1="InProceedings"
		cond1=["Body","Title","Abstract","Label","Month","Year","Identifier"]
	elif(var1.get()==2):
		ins1="Organisation"
		cond1=["Identifier","Name","Label"]
	elif(var1.get()==3):
		ins1="Person"
		cond1=["Identifier","First Name","Last Name","Label","mbox_sha1sum"]
	elif(var1.get()==4):
		ins1="Proceedings"
		cond1=["Identifier","Month","Series","Book Title","Year"]
	elif(var1.get()==5):
		ins1="Reference"
		cond1=["Identifier","Text"]
	
	if(var2.get()==1):
		ins2="InProceedings"
		cond2=["Body","Title","Abstract","Label","Month","Year","Identifier"]
	elif(var2.get()==2):
		ins2="Organisation"
		cond2=["Identifier","Name","Label"]
	elif(var2.get()==3):
		ins2="Person"
		cond2=["Identifier","First Name","Last Name","Label","mbox_sha1sum"]
	elif(var2.get()==4):
		ins2="Proceedings"
		cond2=["Identifier","Month","Series","Book Title","Year"]
	elif(var2.get()==5):
		ins2="Reference"
		cond2=["Identifier","Text"]
	choice=["Both",ins1,ins2]
	global option
	option=OptionMenu(root,out,*choice,command=output1)
	option.pack()
	option.place(bordermode=INSIDE,x=150,y=250)
	
def node2():
	R1.config(state = DISABLED)
	R2.config(state = DISABLED)
	R3.config(state = DISABLED)
	R4.config(state = DISABLED)
	R5.config(state = DISABLED)
	label = Label(root,text="Select Second NODE in RELATION",font = 150,height=1)
	label.pack(side = LEFT)
	label.place(bordermode=INSIDE, x=320, y=25)

	R11.pack()
	R11.place(bordermode=INSIDE, x=320, y=50)
                
	R12.pack()
	R12.place(bordermode=INSIDE, x=320, y=75)

	R13.pack()
	R13.place(bordermode=INSIDE, x=320, y=100)

	R14.pack()
	R14.place(bordermode=INSIDE, x=320, y=125)
	
	R15.pack()
	R15.place(bordermode=INSIDE, x=320, y=150)

label = Label(root,text="Select FIRST NODE in RELATION",font = 150,height=1)
label.pack(side = LEFT)
label.place(bordermode=INSIDE, x=0, y=25)

R1 = Radiobutton(root, text="InProceedings", variable=var1, value=1,font = 100,command=node2)
R1.pack()
R1.place(bordermode=INSIDE, x=0, y=50)

R2 = Radiobutton(root, text="Organisation", variable=var1, value=2,font = 100,command=node2)                  
R2.pack()
R2.place(bordermode=INSIDE, x=0, y=75)

R3 = Radiobutton(root, text="Person", variable=var1, value=3,font = 100,command=node2)
R3.pack()
R3.place(bordermode=INSIDE, x=0, y=100)

R4 = Radiobutton(root, text="Proceedings", variable=var1, value=4,font = 100,command=node2)
R4.pack()
R4.place(bordermode=INSIDE, x=0, y=125)

R5 = Radiobutton(root, text="Reference", variable=var1, value=5,font = 100,command=node2)
R5.pack() 
R5.place(bordermode=INSIDE, x=0, y=150)

R11 = Radiobutton(root, text="InProceedings", variable=var2, value=1,font = 100,command=output)
R12 = Radiobutton(root, text="Organisation", variable=var2, value=2,font = 100,command=output)
R13 = Radiobutton(root, text="Person", variable=var2, value=3,font = 100,command=output)
R14 = Radiobutton(root, text="Proceedings", variable=var2, value=4,font = 100,command=output)
R15 = Radiobutton(root, text="Reference", variable=var2, value=5,font = 100,command=output)

Lb1 = Listbox(root,font = 100,selectmode = MULTIPLE)

Lb2 = Listbox(root,font = 100,selectmode = MULTIPLE)

Rc1 = Radiobutton(root, text="Yes", variable=var3, value=1,font = 100,command=new)
Rc2 = Radiobutton(root, text="No", variable=var3, value=2,font = 100,command=new)
root.attributes('-zoomed', True)
root.mainloop()
