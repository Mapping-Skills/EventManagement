#!/usr/bin/env python
# coding: utf-8

# In[54]:


from tkinter  import*
import sqlite3
#------------------methods-------------------------

def std():
    con=sqlite3.connect("event.db")
    cur=con.cursor()

    root=Tk()
    root.geometry("150x150+400+300")
    root.title("Student corner")

    def up_eve():
            cur.execute("select* from my_data")
            c1=cur.fetchall()
            root1 = Tk()
            root1.geometry("200x150+400+300")
            root1.title("Basic")
            lbl1=Label(root1,text="Event Name",font=("ariel",10,"bold"),fg="green")
            lbl1.grid(row=0,column=1)
            lble1=Label(root1,text=c1[0][0],font=("ariel",10,"bold"),fg="black")
            lble1.grid(row=0,column=2)
            lbl2=Label(root1,text="Event Date",font=("ariel",10,"bold"),fg="green")
            lbl2.grid(row=2,column=1)
            lble2=Label(root1,text=c1[0][1],font=("ariel",10,"bold"),fg="black")
            lble2.grid(row=2,column=2)
            lbl3=Label(root1,text="Event Details",font=("ariel",10,"bold"),fg="green")
            lbl3.grid(row=3,column=1)
            lble3=Label(root1,text=c1[0][2],font=("ariel",10,"bold"),fg="black")
            lble3.grid(row=3,column=2)
            root1.mainloop()

    def list_eve():
            #std.destroy()
            cur.execute("select* from my_data")
            c1=cur.fetchall()
            root1 = Tk()
            root1.title("Basic")
            root1.geometry("300x150+400+300")
            sc= Scrollbar(root1)
            sc.pack( side = RIGHT, fill =Y )
            mylist = Listbox(root1, yscrollcommand = sc.set )
            for line in c1:
                mylist.insert(END,line)
            mylist.pack(fill = BOTH )
            sc.config( command = mylist.yview )

            mainloop()

    lbl=Label(root,text="Event Dashboard",font=("ariel",10,"bold"),fg="green")
    lbl.grid(row=0,column=1)

    m_bttn=Button(root,fg="black",text="Upcoming Event",command=up_eve)
    m_bttn.grid(row=2,column=1,padx=30,pady=20)

    v_bttn=Button(root,fg="black",text="Event List",command=list_eve)
    v_bttn.grid(row=3,column=1,padx=20,pady=10)

    root.mainloop()
