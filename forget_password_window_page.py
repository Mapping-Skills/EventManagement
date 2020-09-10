import sqlite3
from tkinter import *
import send_mail
from tkinter import messagebox


def check_email_id(email):
    conn = sqlite3.connect('event.db')
    c = conn.cursor()
    c.execute("SELECT email,password,user_id from stu_reg WHERE email = ? ", (email, ))
    data = c.fetchall()

    if len(data) == 0:
        messagebox.showinfo("Invalid Details", "Please Enter Valid Email")
    else:
        if data[0][0] == email:
            password = data[0][1]
            username = data[0][2]
            send_mail.send(email, password, username)
        else:
            messagebox.showinfo("Invalid Details", "Please Enter Valid Email")

    c.close()
    conn.close()


def forget_password_window():

    def request_password():
        check_email_id(email_entry.get())

    forget = Tk()
    forget.title("Forget Password")
    forget.iconbitmap('favicon.ico')

    header_frame = Frame(forget, bg="#72F107")
    header_frame.grid(row=0, column=1)

    email_label = Label(header_frame, text="Enter Register Email ID", relief="groove", padx="2", pady="5", borderwidth=2)
    email_label.grid(row=0, column=0, padx=10, pady=10)

    email_entry = Entry(header_frame, relief="sunken", borderwidth=2)
    email_entry.grid(row=0, column=1, padx=10)

    forget_password_button = Button(header_frame, text="Forget Password", bg="#0867FA", fg="#CEDBEF",
                                    font=("Arial", 10, "bold"),
                                    padx="0",
                                    pady="5",
                                    borderwidth="2", relief="sunken", command=request_password)
    forget_password_button.grid(row=2, column=1,)

    forget.mainloop()
