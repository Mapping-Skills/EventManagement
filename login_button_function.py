from tkinter import messagebox
import sqlite3
import student_window

def login_successful():
    # put after login fuction @nupur
    print("Login")


def login(username, password):

    conn = sqlite3.connect('event.db')
    c = conn.cursor()
    c.execute("SELECT user_id,password from stu_reg WHERE user_id = ? ", (username,))
    data = c.fetchall()

    if len(data) != 0:
        if data[0][0] == username and data[0][1] == password:
            student_window.std()
        else:
            messagebox.showinfo("Invalid Details", "Username Or Password Wrong")

    else:
        messagebox.showinfo("Invalid Details", "Username Or Password Wrong")

    c.close()
    conn.close()
