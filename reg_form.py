from tkinter import *
import sqlite3
from tkinter import messagebox
connec = sqlite3.connect('event.db')


def insert():
    try:
        if (user_id.get() == "" or password.get() == "" or first_name.get() == "" or last_name.get() == "" or email.get() == "" or var.get() == "" or reg_type.get() == "" or con_num.get()==''):
            messagebox.showinfo("Invalid Details", "FILL ALL DETAILS")

        else:
            if str(var.get()) == '1':
                gender = 'Male'
            else:
                gender = "Female"


            cur = connec.cursor()

            cur.execute(
                '''CREATE TABLE IF NOT EXISTS stu_reg(first_name text  , last_name text , user_id text , password text , gender text , contact_number text ,reg_type text , email text ,UNIQUE(user_id))''')

            try:
                cur.execute("select email from stu_reg where email= ?", (email.get(),))
                if (cur.fetchone() is None):

                    cur.execute('''INSERT INTO stu_reg VALUES(?,?,?,?,?,?,?,?)''', (
                    first_name.get(), last_name.get(), user_id.get(), password.get(), gender, con_num.get(),
                    reg_type.get(),email.get()))
                    connec.commit()
                    connec.close()

                    messagebox.showinfo("Details", " Registration Successfull ")

                else:
                    messagebox.showinfo("Invalid Details", "This Email Already Exist")
            except:
                messagebox.showinfo("Invalid Details", "Username Already Exist")

            # cur.execute(
            #     '''CREATE TABLE IF NOT EXISTS stu_reg(first_name text  , last_name text , user_id text , password text , gender text , contact_number text ,reg_type text , email text ,UNIQUE(user_id))''')
            # cur.execute('''INSERT INTO stu_reg VALUES(?,?,?,?,?,?,?)''', (first_name.get(),last_name.get(),user_id.get(),password.get(),gender,con_num.get(),reg_type.get()))

    except Exception as e:
        messagebox.showinfo("Details", e)

def student_shadow(root):
    root.destroy()
    student_reg()




def student_reg():

    try:
        global  first_name, last_name, user_id, password, var , con_num, reg_type, email
        root = Tk()
        root.geometry("500x580")
        root.title("Student Registration form")

        label_0 = Label(root, text="Student Registration form", width=20, font=("bold", 20))
        label_0.place(x=90, y=53)

        # first name
        label_1 = Label(root, text="First name", width=20, font=("bold", 10))
        label_1.place(x=80, y=130)
        first_name = Entry(root)
        first_name.place(x=240, y=130)

        # last name
        label_2 = Label(root, text="Last name", width=20, font=("bold", 10))
        label_2.place(x=68, y=180)
        last_name = Entry(root)
        last_name.place(x=240, y=180)

        # user name
        label_3 = Label(root, text="User id", width=20, font=("bold", 10))
        label_3.place(x=68, y=230)
        user_id = Entry(root)
        user_id.place(x=240, y=230)

        # password
        label_4 = Label(root, text="password", width=20, font=("bold", 10))
        label_4.place(x=68, y=280)
        password = Entry(root)
        password.place(x=240, y=280)

        # gender
        label_5 = Label(root, text="Gender", width=20, font=("bold", 10))
        label_5.place(x=70, y=330)
        var = IntVar()
        Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=330)
        Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=330)

        # contact no.
        label_6 = Label(root, text="Contact Number", width=20, font=("bold", 10))
        label_6.place(x=68, y=380)
        con_num = Entry(root)
        con_num.place(x=240, y=380)

        # reg_type
        label_7 = Label(root, text="Reg_type", width=20, font=("bold", 10))
        label_7.place(x=68, y=430)
        reg_type = Entry(root)
        reg_type.place(x=240, y=430)

        # email
        label_8 = Label(root, text="Email", width=20, font=("bold", 10))
        label_8.place(x=68, y=480)
        email = Entry(root)
        email.place(x=240, y=480)

        Button(root, text='Submit', width=20, bg='brown', fg='white', command=insert).place(x=180, y=530)
        # it is use for display the registration form on the window
        root.mainloop()

    except Exception as e:
        print("Error :", e)
        messageVar = Message(root, text=e)
        messageVar.config(bg='lightgreen')
        messageVar.pack()
        root.mainloop()
