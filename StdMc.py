from tkinter import*

root=Tk()
T=Label(root,text="Enter a Student Name").grid(row=0,column=0)
A=Label(root,text="Enter a Student RollNo").grid(row=1,column=0)
B=Label(root,text="Enter a Student Mark1").grid(row=2,column=0)
C=Label(root,text="Enter a Student Mark2").grid(row=3,column=0)
D=Label(root,text="Enter a Student Mark3").grid(row=4,column=0)
D=Label(root,text="Average").grid(row=5,column=0)
#T.pack(side=LEFT, fill=X, padx=5, pady=5)
e1=Entry(root).grid(row=0,column=1)
e2=Entry(root).grid(row=1,column=1)
e3=Entry(root).grid(row=2,column=1)
e4=Entry(root).grid(row=3,column=1)
e5=Entry(root).grid(row=4,column=1)
e6=Entry(root).grid(row=5,column=1)
#e1.pack(side=LEFT)
#e2.pack(side=LEFT)
#e3.pack(side=LEFT)
def calc():
    #name=e1.get()
    #rollno=e2.get()
    m1=e3.get()
    m2=e4.get()
    m3=e5.get()
    m4=float(m1)
    m5=float(m2)
    m6=float(m3)
    avg=(m4+m5+m6)/3
    #E=Entry(root,text=avg).grid(row=5,column=1)
    
    
B=Button(root, text='Calculate',command=calc).grid(row=6,column=0)
mainloop()
      
