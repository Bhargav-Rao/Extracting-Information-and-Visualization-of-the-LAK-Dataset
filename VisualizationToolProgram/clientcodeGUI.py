from tkinter import *
mapping = { "Month": "month","Series":"series", "Book Title":"booktitle", "Identifier":"identifier", "Year":"year", "Name":"name", "First Name":"firstName", "Last Name":"lastName", "Label": "label","mbox_sha1sum":"mbox_sha1sum" ,"Body":"body", "Title":"title" ,"Abstract":"abstract"}
limitvalue = 0
target = False
def main():
           
    root = Tk()
    root.attributes('-zoomed', True)  
    
    welcome_label = Label(root,text = "Extraction of data and Visualization of LAK Dataset",font = 200)
    welcome_label.pack()
    
    label = Label(root,text="1.Select the type of request",font = 150,height=1)
    label.pack(side = LEFT)
    label.place(bordermode=INSIDE, x=0, y=25)
    
    var2 = IntVar()
    global value
    value=[]
    def set_query():
       R21.config(state = DISABLED)
       R22.config(state = DISABLED)
       
       query = "MATCH (a:"+nodelabel+") "
       conditions = []
       for i in value:
         ##print (i)
       	 if i[1]:
          conditions.append("a."+i[0]+" = \"" +i[1]+'"')
       if conditions:
          query+= "WHERE " + " and ".join(conditions)
       query+=" RETURN a"
       limitvalue = limitvar.get()
       if limitvalue != '0':
           query+=" LIMIT "+limitvalue
       
       
       f = open("Intermediate2","w")
       f.write(query)
       f.close()  
       
       f = open("Intermediate1","w")
       #print ("wrkjsb")
       global lst
       lst = [mapping[i] for i in lst]
       f.write(str(lst))
       f.close()            
       root.destroy()
       
    def error():
    	root1=Tk()
    	root1.geometry("300x125")
    	label = Label(root1,text="Maximum no. of columns in the table is 4",font=200)
    	label.pack()
    	label.place(bordermode=INSIDE,x=0,y=25)
    	button = Button(root1,text="OK",height = 1,width = 7,command = root1.destroy,bg="red")
    	button.pack()
    	button.place(bordermode=INSIDE, x=125, y=80)
    	root1.mainloop()    
    
    def condition_setter(event):
    	list1 = []
    	widget = event.widget
    	selection=widget.curselection()
    	for items in selection:
    		list1.append(widget.get(items))
    
    	def condition_setter_inner():
    		i1=iter(list1)
    		Lb1.config(state = DISABLED)
    		root2=Tk()
    		global button3
    		button3.config(state=DISABLED)
    		root2.geometry("400x500")
    		label1=Label(root2,text="Enter the values for node",font=200)
    		label1.pack()
    		label1.place(bordermode=INSIDE,x=0,y=30)
    		try:
    			l1=Label(root2,text=next(i1)+':',font=200)
    			l1.pack()
    			l1.place(bordermode=INSIDE,x=0,y=70)
    			t1=Entry(master=root2)
    			t1.pack()
    			t1.place(bordermode=INSIDE,x=100,y=70)
    			l2=Label(root2,text=next(i1)+':',font=200)
    			l2.pack()
    			l2.place(bordermode=INSIDE,x=0,y=100)
    			t2=Entry(master=root2)
    			t2.pack()
    			t2.place(bordermode=INSIDE,x=100,y=100)
    			l3=Label(root2,text=next(i1)+':',font=200)
    			l3.pack()
    			l3.place(bordermode=INSIDE,x=0,y=130)
    			t3=Entry(master=root2)
    			t3.pack()
    			t3.place(bordermode=INSIDE,x=100,y=130)
    			l4=Label(root2,text=next(i1)+':',font=200)
    			l4.pack()
    			l4.place(bordermode=INSIDE,x=0,y=160)
    			t4=Entry(master=root2)
    			t4.pack()
    			t4.place(bordermode=INSIDE,x=100,y=160)
    			l5=Label(root2,text=next(i1)+':',font=200)
    			l5.pack()
    			l5.place(bordermode=INSIDE,x=0,y=190)
    			t5=Entry(master=root2)
    			t5.pack()
    			t5.place(bordermode=INSIDE,x=100,y=190)
    			l6=Label(root2,text=next(i1)+':',font=200)
    			l6.pack()
    			l6.place(bordermode=INSIDE,x=0,y=220)
    			t6=Entry(master=root2)
    			t6.pack()
    			t6.place(bordermode=INSIDE,x=100,y=220)
    			l7=Label(root2,text=next(i1)+':',font=200)
    			l7.pack()
    			l7.place(bordermode=INSIDE,x=0,y=250)
    			t7=Entry(master=root2)
    			t7.pack()
    			t7.place(bordermode=INSIDE,x=100,y=250)
    		except StopIteration:
    			pass
    	
    		def get():
    			i1=iter(list1)
    			
    			global value
    			try:
    				next(i1)
    				value.append([mapping[l1.cget("text")[:-1]],t1.get()])
    				next(i1)
    				value.append([mapping[l2.cget("text")[:-1]],t2.get()])
    				next(i1)
    				value.append([mapping[l3.cget("text")[:-1]],t3.get()])
    				next(i1)
    				value.append([mapping[l4.cget("text")[:-1]],t4.get()])
    				next(i1)
    				value.append([mapping[l5.cget("text")[:-1]],t5.get()])
    				next(i1)
    				value.append([mapping[l6.cget("text")[:-1]],t6.get()])
    				next(i1)
    				value.append([mapping[l7.cget("text")[:-1]],t7.get()])
    			except StopIteration:
    				pass
    			##print(value)
    			root2.destroy()
    			set_query()
    		button2 = Button(root2,text="SUBMIT",height = 2,width = 10,command = get)
    		button2.pack()
    		button2.place(bordermode=INSIDE, x=200, y=300)
    		root2.mainloop()
    		
    	global button3
    	button3 = Button(root,text="Ok",height = 2,width = 10,command = condition_setter_inner)
    	#button.pack()
    	button3.place(bordermode=INSIDE, x=350, y=500)
    

       
    
    def condition():
       
       label = Label(root,text="5.Select the properties on which the conditions should be applied",font = 150,height=1)
       label.pack(side = LEFT)
       label.place(bordermode=INSIDE, x=310, y=250)
       global limitvalue
       limitvalue = limitvar.get()
       limiter.config(state = DISABLED)
       R21.config(state = DISABLED)
       R22.config(state = DISABLED)       
       global Lb1
       
    
       Lb1 = Listbox(root,font = 100,selectmode = MULTIPLE)
    
       if(var1.get() == 1):
          Lb1.insert(END, "Body")
          Lb1.insert(END, "Title")
          Lb1.insert(END, "Abstract")
          Lb1.insert(END, "Label")
          Lb1.insert(END, "Month")
          Lb1.insert(END, "Year")
          Lb1.insert(END, "Identifier")
          Lb1.pack()
          Lb1.place(bordermode=INSIDE, x=310, y=275)
          Lb1.bind("<ButtonRelease-1>",condition_setter )
          #sender(Lb1)
    
       elif(var1.get() == 2):
          
          Lb1.insert(1, "Identifier")
          Lb1.insert(2, "Name")
          Lb1.insert(3, "Label")
          Lb1.pack()
          Lb1.place(bordermode=INSIDE, x=310, y=275)
          Lb1.bind("<ButtonRelease-1>",condition_setter )
    
       elif(var1.get() == 3):
          
          Lb1.insert(1, "Name")
          Lb1.insert(2, "First Name")
          Lb1.insert(3, "Last Name")
          Lb1.insert(4, "Label")
          Lb1.insert(5, "mbox_sha1sum")
          Lb1.insert(6, "Identifier")
          Lb1.pack()
          Lb1.place(bordermode=INSIDE, x=310, y=275)
          Lb1.bind("<ButtonRelease-1>", condition_setter)
    
       elif(var1.get() == 4): 
          
          Lb1.insert(1, "Month")
          Lb1.insert(2, "Series")
          Lb1.insert(3, "Book Title")
          Lb1.insert(4, "Identifier")
          Lb1.insert(5, "Year")
          Lb1.pack()
          Lb1.place(bordermode=INSIDE, x=310, y=275)
          Lb1.bind("<ButtonRelease-1>",condition_setter )
    
       else:
          pass
       
    
    def sender(event):
       global lst
       #print ("sender called")
       lst = []
       #print ("lst",lst)
       widget = event.widget
       selection=widget.curselection()
       for items in selection:
          lst.append(widget.get(items))
          if len(lst) > 4:
              error()
       
    
       
       def sender2():
          ##print(lst)
          Lb1.config(state = DISABLED)
          button.place_forget()
          button.place()
          label = Label(root,text="4.Specify the limit for output",font = 150,height=1)
          label.pack(side = LEFT)
          label.place(bordermode=INSIDE, x=900, y=25)
          label1 = Label(root,text="select 0 for no upper bound",font = 150,height=1)
          label1.pack(side = LEFT)
          label1.place(bordermode=INSIDE, x=900, y=45)
          global limiter
          global limitvar
          limitvar = StringVar()
       
          limiter = Spinbox(root, values=(0,5,10,15,20,25,50,100), textvariable = limitvar)
          limiter.pack()
          limiter.place(bordermode=INSIDE, x=920, y=75)
    
          label = Label(root,text="5.Do you want to add a condition?",font = 150,height=1)
          label.pack(side = LEFT)
          label.place(bordermode=INSIDE, x=0, y=250)
          global R21,R22
    
          R21 = Radiobutton(root, text="Yes", variable=var2, value=1,font = 100,
                      command=condition)
          R21.pack( anchor = W,side = LEFT )
          R21.place(bordermode=INSIDE, x=0, y=275)
    
          R22 = Radiobutton(root, text="No", variable=var2, value=2,font = 100,
                      command=set_query)
          R22.pack( anchor = W,side = LEFT )
          R22.place(bordermode=INSIDE, x=0, y=300)

    
       
    
       button = Button(root,text="Ok",height = 2,width = 10,command = sender2)
       button.pack()
       button.place(bordermode=INSIDE, x=650, y=280)
       
    
    
    def caller():
       R1.config(state=DISABLED)
       R2.config(state=DISABLED)
       R3.config(state=DISABLED)
       R4.config(state=DISABLED)
       
       label1 = Label(root,text="3.Select the properties",font = 150,height=1)
       label1.pack()
       label1.place(bordermode=INSIDE, x=600, y=25)
       global Lb1
       global nodelabel
       nodes = ["InProceedings","Organisation","Person","Proceedings"]
       nodelabel = nodes[var1.get()-1]
      
       Lb1 = Listbox(root,font = 100,selectmode = MULTIPLE)
       
       if(var1.get() == 1):
          Lb1.insert(END, "Body")
          Lb1.insert(END, "Title")
          Lb1.insert(END, "Abstract")
          Lb1.insert(END, "Label")
          Lb1.insert(END, "Month")
          Lb1.insert(END, "Year")
          Lb1.insert(END, "Identifier")
          Lb1.pack()
          Lb1.place(bordermode=INSIDE, x=610, y=50)
          Lb1.bind("<ButtonRelease-1>", sender)
          #sender(Lb1)
    
       elif(var1.get() == 2):
          
          Lb1.insert(1, "Identifier")
          Lb1.insert(2, "Name")
          Lb1.insert(3, "Label")
          Lb1.pack()
          Lb1.place(bordermode=INSIDE, x=610, y=50)
          Lb1.bind("<ButtonRelease-1>", sender)
    
       elif(var1.get() == 3):
          
          Lb1.insert(1, "Name")
          Lb1.insert(2, "First Name")
          Lb1.insert(3, "Last Name")
          Lb1.insert(4, "Label")
          Lb1.insert(5, "mbox_sha1sum")
          Lb1.insert(6, "Identifier")
          Lb1.pack()
          Lb1.place(bordermode=INSIDE, x=610, y=50)
          Lb1.bind("<ButtonRelease-1>", sender)
    
       elif(var1.get() == 4):
          
          Lb1.insert(1, "Month")
          Lb1.insert(2, "Series")
          Lb1.insert(3, "Book Title")
          Lb1.insert(4, "Identifier")
          Lb1.insert(5, "Year")
          Lb1.pack()
          Lb1.place(bordermode=INSIDE, x=610, y=50)
          Lb1.bind("<ButtonRelease-1>", sender)
    
       else:
          pass
       
    var1 = IntVar()
    
    def callrelation():
        import os;
        root.destroy()
        os.system("python3 relationgui.py ")
        #import relationgui --- for windows users
    def select_node():
       label = Label(root,text="2.Select a node",font = 150,height=1)
       label.pack()
       target = True
       #print ("target is",target)
       label.place(bordermode=INSIDE, x=310, y=25)
       global R1,R2,R3,R4
       R01.config(state=DISABLED)
       R02.config(state=DISABLED)
       R1 = Radiobutton(root, text="InProceedings", variable=var1, value=1,font = 100,
                      command=caller)
       R1.pack()#anchor = W,side = LEFT )
       R1.place(bordermode=INSIDE, x=310, y=50)
    
       R2 = Radiobutton(root, text="Organisation", variable=var1, value=2,font = 100,
                      command=caller)
       R2.pack()#anchor = W,side = LEFT )
       R2.place(bordermode=INSIDE, x=310, y=75)
    
       R3 = Radiobutton(root, text="Person", variable=var1, value=3,font = 100,
                      command=caller)
       R3.pack()# anchor = W,side = LEFT )
       R3.place(bordermode=INSIDE, x=310, y=100)
    
       R4 = Radiobutton(root, text="Proceedings", variable=var1, value=4,font = 100,
                      command=caller)
       R4.pack() #anchor = W,side = LEFT )
       R4.place(bordermode=INSIDE, x=310, y=125)
    
    
    var = IntVar()
    R01 = Radiobutton(root, text="Node", variable=var, value=1,font = 100,
                      command=select_node)
    R01.pack( anchor = W,side = LEFT )
    R01.place(bordermode=INSIDE, x=0, y=50)
    
    R02 = Radiobutton(root, text="Relation", variable=var, value=2,font = 100,
                      command=callrelation)
    R02.pack( anchor = W,side = LEFT )
    R02.place(bordermode=INSIDE, x=0, y=75)
    
    root.mainloop()
main()

