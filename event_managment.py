#!/usr/bin/env python
# coding: utf-8

# In[13]:


import new_entry
from tkinter import *
import sqlite3

# ------------------methods-------------------------
con = sqlite3.connect("event.db")
cur = con.cursor()


# -------------------modify-function-----------------
def c_data(log):
    log.destroy()

    def edit():
        root1.destroy()
        dat = Tk()
        dat.geometry("600x270+400+300")
        dat.title("work")

        user_id = StringVar()
        password = StringVar()
        name = StringVar()
        number = StringVar()
        mail = StringVar()

        def c_save():
            try:
                cur.execute(
                    "CREATE TABLE IF NOT EXISTS  college_data (user text,password int,c_name text,c_num int,cmail text)")
                cur.execute("UPDATE college_data SET user = (?) where c_name = (?)", (user_id.get(), name.get()))
                cur.execute("UPDATE college_data SET c_num = (?) where c_name = (?)", (number.get(), name.get()))
                cur.execute("UPDATE college_data SET cmail = (?) where c_name = (?)", (mail.get(), name.get()))
                con.commit()
            except:
                print("data not saved")

        try:
            cur.execute("select* from college_data")
            c1 = cur.fetchall()

            user_id.set(c1[0][0])
            password.set(c1[0][1])
            name.set(c1[0][2])
            number.set(c1[0][3])
            mail.set(c1[0][4])

            lbl1 = Label(dat, text="", font=("ariel", 10, "bold"), fg="green")
            lbl1.grid(row=0, column=0)
            user = Label(dat, text="User Name :", font=("ariel", 10, "italic"), fg="black", bd=8)
            user.grid(row=1, column=1)
            pss = Label(dat, text="Password :", font=('ariel', 10, "italic"), fg="black", bd=10)
            pss.grid(row=3, column=1)
            c_name = Label(dat, text="College Name :", font=('ariel', 10, "italic"), fg="black", bd=10)
            c_name.grid(row=4, column=1)
            c_id = Label(dat, text="College ID:", font=('ariel', 10, "italic"), fg="black", bd=10)
            c_id.grid(row=5, column=1)
            c_mail = Label(dat, text="College Email:", font=('ariel', 10, "italic"), fg="black", bd=10)
            c_mail.grid(row=6, column=1)

            usere = Entry(dat, font=('ariel', 10), textvariable=user_id, fg="black", justify="left")
            usere.grid(row=1, column=4)
            psse = Entry(dat, font=('ariel', 10), textvariable=password, fg="black", justify="left", show="*")
            psse.grid(row=3, column=4)
            c_namee = Entry(dat, font=('ariel', 10), textvariable=name, fg="black", justify="left")
            c_namee.grid(row=4, column=4)
            c_ide = Entry(dat, font=('ariel', 10), textvariable=number, fg="black", justify="left")
            c_ide.grid(row=5, column=4)
            c_maile = Entry(dat, font=('ariel', 10), textvariable=mail, fg="black", justify="left")
            c_maile.grid(row=6, column=4)

            ed_bttn = Button(dat, width=10, fg="black", text="Edit", bd=8, command=c_save)
            ed_bttn.grid(row=7, column=2)
        except:
            lbl1 = Label(dat, text="No Data Available , please Insert data", font=("ariel", 10, "bold"), fg="green")
            lbl1.grid(row=0, column=0)
            lbl = Label(dat, text="Click below to add details", font=('ariel', 10, "italic"), fg="black", bd=10)
            lbl.grid(row=7, column=0)

        def exit1():
            c_data(dat)

        bttn = Button(dat, width=10, fg="black", text="exit", bd=8, command=exit1)
        bttn.grid(row=7, column=4)

        def new(dat):
            dat.destroy()

            at = Tk()
            at.geometry("200x120+400+300")
            at.title("new")

            var = StringVar()
            c_mail = Label(at, text="Want to Update College !", font=('ariel', 10, "italic"), fg="black", bd=10)
            c_mail.grid(row=1, column=2)

            def ne():
                cur.execute('Delete from college_data')
                con.commit()
                new_entry.entry(at)

            bttn = Button(at, fg="black", text="Yes", bd=8, command=ne)
            bttn.grid(row=2, column=2)
            ex = Label(at, text="It will delete your previous data", font=('ariel', 10, "italic"), fg="black", bd=10)
            ex.grid(row=3, column=2)

        lbl_4 = Label(dat, text="  Update College  ", font=("ariel", 8, "bold"), fg="black")
        lbl_4.grid(row=8, column=0)
        lbl_4.bind("<Button>", lambda e: new(dat))

        dat.mainloop()

    cur.execute("CREATE TABLE IF NOT EXISTS  college_data (user text,password int,c_name text,c_num int,cmail text)")
    cur.execute("select* from college_data")
    c1 = cur.fetchall()
    root1 = Tk()
    root1.geometry("250x250+400+300")
    root1.title("Basic")
    try:
        data = Label(root1, text="User Name :", font=('ariel', 10, "italic"), fg="black", bd=10)
        data.grid(row=1, column=1)
        datau = Label(root1, text=c1[0][0], font=('ariel', 10, "italic"), fg="black", bd=10)
        datau.grid(row=1, column=2)
        datn = Label(root1, text="College Name :", font=('ariel', 10, "italic"), fg="black", bd=10)
        datn.grid(row=2, column=1)
        datan = Label(root1, text=c1[0][2], font=('ariel', 10, "italic"), fg="black", bd=10)
        datan.grid(row=2, column=2)
        da = Label(root1, text="Number :", font=('ariel', 10, "italic"), fg="black", bd=10)
        da.grid(row=3, column=1)
        dataN = Label(root1, text=c1[0][3], font=('ariel', 10, "italic"), fg="black", bd=10)
        dataN.grid(row=3, column=2)
        dam = Label(root1, text="Mail :", font=('ariel', 10, "italic"), fg="black", bd=10)
        dam.grid(row=4, column=1)
        datam = Label(root1, text=c1[0][4], font=('ariel', 10, "italic"), fg="black", bd=10)
        datam.grid(row=4, column=2)
    except:
        data = Label(root1, text="No data avialble", font=('ariel', 10, "italic"), fg="black", bd=10)
        data.grid(row=1, column=1)

    ed_bttn = Button(root1, width=10, fg="black", text="Edit", bd=8, command=edit)
    ed_bttn.grid(padx=20, pady=30, row=5, column=1)

    def wwe():
        root1.destroy()

    bttn = Button(root1, width=10, fg="black", text="Exit", bd=8, command=wwe)
    bttn.grid(padx=20, pady=30, row=5, column=2)

    root1.mainloop()


def work(log):
    log.destroy()
    wrk = Tk()
    wrk.geometry("600x200+400+300")
    wrk.title("work")

    def add(wrk):
        wrk.destroy()
        ad = Tk()
        ename = StringVar()
        edate = StringVar()
        edetails = StringVar()
        ad.geometry("600x300+400+300")
        ad.title("DATA")

        def save():
            try:
                cur.execute("CREATE TABLE IF NOT EXISTS  my_data (Ename text,Edate int,Edetails text)")
                cur.execute("INSERT INTO my_data values(?,?,?)", (ename.get(), edate.get(), edetails.get()))
                con.commit()
                ename.set("")
                edate.set("")
                edetails.set("")
            except:
                print("data not saved")

        def ww():
            work(ad)

        lbl = Label(ad, text="", font=("ariel", 10, "bold"), fg="green", bd=8)
        lbl.grid(row=0, column=0)

        name_lbl = Label(ad, text="Event Name :", font=("ariel", 20), fg="black", bd=8)
        name_lbl.grid(row=1, column=2)
        name_e = Entry(ad, font=("ariel", 20), fg="black", textvariable=ename)
        name_e.grid(row=1, column=3)

        num_lbl = Label(ad, text="Event date :", font=("ariel", 20), fg="black", bd=8)
        num_lbl.grid(row=2, column=2)
        num_e = Entry(ad, font=("ariel", 20), fg="black", textvariable=edate)
        num_e.grid(row=2, column=3)

        add_lbl = Label(ad, text="Event Description :", font=("ariel", 20), fg="black", bd=8)
        add_lbl.grid(row=3, column=2)
        add_e = Entry(ad, font=("ariel", 20), fg="black", textvariable=edetails)
        add_e.grid(row=3, column=3)

        ad_bttn = Button(ad, width=10, fg="black", text="ADD", bd=8, command=save)
        ad_bttn.grid(padx=20, pady=30, row=4, column=2)

        bttn = Button(ad, width=10, fg="black", text="Exit", bd=8, command=ww)
        bttn.grid(padx=20, pady=30, row=4, column=3)

        ad.mainloop()

    def view_data(wrk):
        wrk.destroy()
        cur.execute("select* from my_data")
        c1 = cur.fetchall()
        root1 = Tk()
        root1.title("Basic")
        # root.geometry("890x580+0+0")
        sc = Scrollbar(root1)
        sc.pack(side=RIGHT, fill=Y)
        mylist = Listbox(root1, yscrollcommand=sc.set)
        for line in c1:
            mylist.insert(END, line)
        mylist.pack(fill=BOTH)
        sc.config(command=mylist.yview)

        def ww1():
            work(root1)

        bttn = Button(root1, width=10, fg="black", text="Exit", bd=8, command=ww1).pack(side="top")
        # bttn.grid(padx=20,pady=30,row=0,column=0)
        mainloop()

    def update(wrk):
        wrk.destroy()
        ad = Tk()
        ename = StringVar()
        edate = StringVar()
        edetails = StringVar()
        ad.geometry("650x300+400+300")
        ad.title("DATA")

        def ss():
            cur.execute("select * from my_data where ename =(?)", (ename.get(),))
            emp2 = cur.fetchall()
            edate.set(emp2[0][1])
            edetails.set(emp2[0][2])
            con.commit()

        name_lbl = Label(ad, text="Enter Event name  :", font=("ariel", 15), fg="black", bd=8)
        name_lbl.grid(row=1, column=2)
        name_e = Entry(ad, font=("ariel", 15), fg="black", textvariable=ename)
        name_e.grid(row=1, column=3)
        bttn = Button(ad, width=10, fg="black", text="Submit", bd=8, command=ss)
        bttn.grid(padx=20, pady=30, row=1, column=7)

        num_lbl = Label(ad, text="Date :", font=("ariel", 20), fg="black", bd=8)
        num_lbl.grid(row=2, column=2)
        num_e = Entry(ad, font=("ariel", 20), fg="black", textvariable=edate)
        num_e.grid(row=2, column=3)

        add_lbl = Label(ad, text="Description :", font=("ariel", 20), fg="black", bd=8)
        add_lbl.grid(row=3, column=2)
        add_e = Entry(ad, font=("ariel", 20), fg="black", textvariable=edetails)
        add_e.grid(row=3, column=3)

        def uv():
            cur.execute("UPDATE my_data SET Edate = (?) where Ename = (?)", (edate.get(), ename.get()))
            cur.execute("UPDATE my_data SET edetails = (?) where Ename =(?)", (edetails.get(), ename.get()))
            con.commit()

        ad_bttn = Button(ad, width=10, fg="black", text="Update", bd=8, command=uv)
        ad_bttn.grid(padx=20, pady=30, row=4, column=2)

        def wwu():
            work(ad)

        bttn = Button(ad, width=10, fg="black", text="Exit", bd=8, command=wwu)
        bttn.grid(padx=20, pady=30, row=4, column=3)
        ad.mainloop()

    """def search(wrk):
        wrk.destroy()
        ad=Tk()
        name=StringVar()
        number=StringVar()
        address=StringVar()
        ad.geometry("600x300+400+300")
        ad.title("DATA")
        def ss():
            cur.execute("select * from my_data where Number =(?)",(number.get(),))
            emp2 = cur.fetchall()
            name.set(emp2[0][0])
            address.set(emp2[0][2])
            con.commit()
        name_lbl=Label(ad,text="Enter number  :",font=("ariel",15),fg="black",bd=8)
        name_lbl.grid(row=1,column=2)
        name_e=Entry(ad,font=("ariel",15),fg="black",textvariable=number)
        name_e.grid(row=1,column=3)
        bttn=Button(ad,width=10,fg="black",text="Submit",bd=8,command=ss)
        bttn.grid(padx=20,pady=30,row=1,column=7)
        num_lbl=Label(ad,text="Name :",font=("ariel",20),fg="black",bd=8)
        num_lbl.grid(row=2,column=2)
        num_e=Entry(ad,font=("ariel",20),fg="black",textvariable=name)
        num_e.grid(row=2,column=3)
        add_lbl=Label(ad,text="address :",font=("ariel",20),fg="black",bd=8)
        add_lbl.grid(row=3,column=2)
        add_e=Entry(ad,font=("ariel",20),fg="black",textvariable=address)
        add_e.grid(row=3,column=3)
        def wwu():
            work(ad)
        bttn=Button(ad,width=10,fg="black",text="Exit",bd=8,command=wwu)
        bttn.grid(padx=20,pady=30,row=4,column=3)
        ad.mainloop()"""

    def delete(wrk):
        wrk.destroy()
        ad = Tk()
        ename = StringVar()
        ad.geometry("600x300+400+300")
        ad.title("DATA")

        def dd():
            try:
                cur.execute('''DELETE from my_data where Ename = (?)''', (ename.get(),))
                con.commit()
                ssd = Label(ad, text="data deleted", font=("ariel", 15), fg="green", bd=8)
                ssd.grid(row=3, column=2)
            except:
                ssd = Label(ad, text="Invalid event name", font=("ariel", 15), fg="green", bd=8)
                ssd.grid(row=3, column=2)

        name_lbl = Label(ad, text="Enter Event name  :", font=("ariel", 15), fg="black", bd=8)
        name_lbl.grid(row=1, column=2)
        num_e = Entry(ad, font=("ariel", 15), fg="black", textvariable=ename)
        num_e.grid(row=1, column=3)
        bttn = Button(ad, width=10, fg="black", text="Delete", bd=8, command=dd)
        bttn.grid(padx=20, pady=30, row=1, column=7)

        def wwu():
            work(ad)

        bttn = Button(ad, width=10, fg="black", text="Exit", bd=8, command=wwu)
        bttn.grid(padx=20, pady=30, row=4, column=3)
        ad.mainloop()

    def a():
        add(wrk)

    def v():
        view_data(wrk)

    def u():
        update(wrk)

    """ def s():
        search(wrk)"""

    def d():
        delete(wrk)

    a_bttn = Button(wrk, width=10, fg="black", text="ADD", bd=8, command=a)
    a_bttn.grid(padx=20, pady=30, row=2, column=1)
    up_bttn = Button(wrk, width=10, fg="black", text="UPDATE", bd=8, command=u)
    up_bttn.grid(padx=40, pady=30, row=2, column=2)
    up_bttn = Button(wrk, width=10, fg="black", text="DELETE", bd=8, command=d)
    up_bttn.grid(padx=60, pady=30, row=2, column=3)
    # s_bttn=Button(wrk,width=10,fg="black",text="search",bd=8,command=s)
    # s_bttn.grid(padx=30,pady=30,row=3,column=1)
    v_bttn = Button(wrk, width=10, fg="black", text="VIEW", bd=8, command=v)
    v_bttn.grid(padx=70, pady=30, row=3, column=2)

    def q():
        print("Thanks for visit")
        wrk.destroy()

    e_bttn = Button(wrk, width=10, fg="black", text="Exit", bd=8, command=q)
    e_bttn.grid(padx=60, pady=30, row=3, column=3)
    wrk.mainloop()

def admin_shadow(root):
    root.destroy()
    admin()

def admin():
    log = Tk()
    username = StringVar()
    password = StringVar()
    username.set("")
    password.set("")
    log.geometry("450x170+400+300")
    log.title("MODIFY")

    try:
        cur.execute("select* from college_data")
        c1 = cur.fetchall()
        user1 = c1[0][0]
        pss1 = c1[0][1]
        u = 0
        p = 0
    except:
        lbl_0 = Label(log, text="Please insert college details ", font=("ariel", 8, "bold"), fg="black")
        lbl_0.grid(row=5, column=3)

    lbl = Label(log, text="", font=("ariel", 10, "bold"), fg="green")
    lbl.grid(row=0, column=0)
    user = Label(log, text="User Name :", font=("ariel", 10, "italic"), fg="black", bd=8)
    user.grid(row=1, column=1)
    pss = Label(log, text="Password :", font=('ariel', 10, "italic"), fg="black", bd=10)
    pss.grid(row=3, column=1)

    usere = Entry(log, font=('ariel', 10), textvariable=username, fg="black", justify="left")
    usere.grid(row=1, column=4)
    psse = Entry(log, font=('ariel', 10), textvariable=password, fg="black", justify="left")
    psse.grid(row=3, column=4)

    def w():
        if username.get() == user1 and password.get() == pss1:
            work(log)
        else:
            print("wrong id password")

    u_bttn = Button(log, width=10, fg="black", text="Login", command=w)
    u_bttn.grid(row=4, column=3)

    lbl_1 = Label(log, text="", font=("ariel", 8, "bold"), fg="green")
    lbl_1.grid(row=4, column=2)
    lbl_3 = Label(log, text="college details", font=("ariel", 8, "bold"), fg="green")
    lbl_3.grid(row=6, column=3)
    lbl_3.bind("<Button>", lambda e: c_data(log))
    log.mainloop()
