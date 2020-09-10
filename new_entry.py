
from tkinter  import*
import sqlite3

con=sqlite3.connect("event.db")
cur=con.cursor()
def entry(at):
    at.destroy()
    col=Tk()
    col.geometry("600x250+400+300")
    col.title("work")

    user_id=StringVar()
    password=StringVar()
    name=StringVar()
    number=StringVar()
    mail=StringVar()

    def n_save():
            try:
                cur.execute("CREATE TABLE IF NOT EXISTS  college_data (user text,password int,c_name text,c_num int,cmail text)")
                cur.execute("INSERT INTO college_data values(?,?,?,?,?)",(user_id.get(),password.get(),name.get(),number.get(),mail.get()))
                con.commit()
            except :
                print("data not saved")



    lbl1=Label(col,text="",font=("ariel",10,"bold"),fg="green")
    lbl1.grid(row=0,column=0)
    user=Label(col,text="User Name :",font=("ariel",10,"italic"),fg="black",bd=8)
    user.grid(row=1,column=1)
    pss=Label(col,text="Password :",font=('ariel',10,"italic"),fg="black",bd=10)
    pss.grid(row=3,column=1)
    c_name=Label(col,text="College Name :",font=('ariel',10,"italic"),fg="black",bd=10)
    c_name.grid(row=4,column=1)
    c_id=Label(col,text="College ID:",font=('ariel',10,"italic"),fg="black",bd=10)
    c_id.grid(row=5,column=1)
    c_mail=Label(col,text="College Email:",font=('ariel',10,"italic"),fg="black",bd=10)
    c_mail.grid(row=6,column=1)

    usere=Entry(col,font=('ariel',10),textvariable=user_id,fg="black",justify="left")
    usere.grid(row=1,column=4)
    psse=Entry(col,font=('ariel',10),textvariable=password,fg="black",justify="left",show="*")
    psse.grid(row=3,column=4)
    c_namee=Entry(col,font=('ariel',10),textvariable=name,fg="black",justify="left")
    c_namee.grid(row=4,column=4)
    c_ide=Entry(col,font=('ariel',10),textvariable=number,fg="black",justify="left")
    c_ide.grid(row=5,column=4)
    c_maile=Entry(col,font=('ariel',10),textvariable=mail,fg="black",justify="left")
    c_maile.grid(row=6,column=4)

    ed_bttn=Button(col,width=10,fg="black",text="Edit",bd=8,command=n_save)
    ed_bttn.grid(row=7,column=2)
    def exit():
        col.destroy()
        #print(password.get())
    bttn=Button(col,width=10,fg="black",text="exit",bd=8,command=exit)
    bttn.grid(row=7,column=4)
    col.mainloop()