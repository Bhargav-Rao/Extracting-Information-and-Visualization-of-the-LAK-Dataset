import tkinter as tk
import tkinter.tix
class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        canvas = tk.Canvas(self, borderwidth=0)
        table = tk.Frame(canvas)
        table.pack(side="top", fill="both", expand=True)
        fp = open("Intermediate3")
        l = eval(fp.readline())
        l2 = (fp.readline())
        head2 =[]
        if l2:
            l2 = eval(l2)
            data2 = l2[1:]
            head2 = l2[0]    
                
        data = l[1:]
        head = l[0]
        
        vsb = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=vsb.set)

        vsb.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        canvas.create_window((4,4), window=table, anchor="nw", 
                                  tags="self.frame")

        
        
        
        #print (data,head,data2,head2,sep = '\n')
        colval = len(head)+len(head2) -1
        rowval = 0
        tk.Button(table, text="Get PDF",font = 150, command=self.submit).grid(row=rowval, column=colval, sticky="nsew")
        rowval = 1
        #print (head)
        for i in range(len(head)):
            tk.Label(table, text=repr(head[i])[1:-1], justify=tk.LEFT,font = 150, wraplength=500).grid(row=rowval, column=i, sticky="nsew")
        i+=1
        if l2:
            for j in range (len(head2)):
                 tk.Label(table, text=repr(head2[j])[1:-1], justify=tk.LEFT,font = 150, wraplength=500).grid(row=rowval, column=i+j, sticky="nsew")
        
        rowval+=1  
        initrowval = rowval  
        j = 0    
        for i in data:
            for j in range(len(i)):
                tk.Label(table, text=repr(i[j])[1:-1], justify=tk.LEFT,font = 150, wraplength=500).grid(row=rowval, column=j, sticky="nsew")
            rowval+=1
        j+=1
        
        if l2:
            rowval = initrowval
            for i in data2:
                for k in range(len(i)):
                    tk.Label(table, text=repr(i[k])[1:-1], justify=tk.LEFT,font = 150, wraplength=500).grid(row=rowval, column=j+k, sticky="nsew")
                rowval+=1
                
        #tk.Button(table, text="Close", command=self.destroy).grid(row=rowval, column=colval, sticky="nsew")
        
    def submit(self):
         import os
         os.system("python getPDF.py")           
            
if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-zoomed', True)
    Example(root).pack(fill="both", expand=True)
    root.attributes('-alpha', True)  
    
    root.mainloop()
