from tkinter import *
import login_button_function
import forget_password_window_page
import event_managment
import reg_form

def home_page_window():
    def login():
        login_button_function.login(username_entry.get(), password_entry.get())

    def register():
        reg_form.student_shadow(root)

    def forget():
        forget_password_window_page.forget_password_window()

    def admin():
        event_managment.admin_shadow(root)

    # Frame1
    details_frame = Frame(root, bg="#4C93EA", borderwidth=1, relief="flat", height=100, width=200)
    details_frame.grid(row=2, column=1, padx=150)

    username_label = Label(details_frame, text="Username", font=("Arial", 15, "bold"), relief="groove", padx="2",
                           pady="5", borderwidth=2)
    username_label.grid(row=1, column=0, padx=5, pady=10)

    password_label = Label(details_frame, text="Password", font=("Arial", 15, "bold"), relief="groove", padx="2",
                           pady="5", borderwidth=2)
    password_label.grid(row=2, column=0, padx=5, pady=10)

    username_entry = Entry(details_frame, relief="sunken", font=("Arial", 15, "bold"), borderwidth=2)
    username_entry.grid(row=1, column=2, padx=5)

    password_entry = Entry(details_frame, relief="sunken", font=("Arial", 15, "bold"), borderwidth=2)
    password_entry.grid(row=2, column=2, padx=5)

    # Frame 2
    details_frame_in = Frame(root, bg="#E0E6F0", borderwidth=1, relief="flat")
    details_frame_in.grid(row=3, column=1)

    login_button = Button(details_frame_in, text="Login", bg="#0867FA", fg="#CEDBEF", font=("Arial", 10, "bold"), padx="1", pady="0",
                          borderwidth="2", relief="sunken", command=login)
    login_button.grid(row=3, column=2, sticky=E + W + S + N, pady=10, padx=50)

    register_button = Button(details_frame_in, text="Registration", bg="#0867FA", fg="#CEDBEF", font=("Arial", 10, "bold"), padx="0",
                             pady="5",
                             borderwidth="2", relief="sunken", command=register)
    register_button.grid(row=4, column=2, sticky=E + W + S + N, pady=10, padx=50)

    forget_password_button = Button(details_frame_in, text="Forget Password", bg="#0867FA", fg="#CEDBEF", font=("Arial", 10, "bold"),
                                    padx="0",
                                    pady="5",
                                    borderwidth="2", relief="sunken", command=forget)
    forget_password_button.grid(row=5, column=2, sticky=E + W + S + N, pady=10, padx=50)

    admin_panel_button = Button(details_frame_in, text="Admin Panel", bg="#0867FA", fg="#CEDBEF", font=("Arial", 10, "bold"),
                                padx="2", pady="0",
                                borderwidth="2", relief="sunken", command=admin)
    admin_panel_button.grid(row=6, column=2, sticky=E + W + S + N, pady=10, padx=50)


root = Tk()
root.title("Home Page")
root.configure(bg='#2D75E4')

root.iconbitmap('favicon.ico')


header_frame = Frame(root, bg="#72F107")
header_frame.grid(row=0, column=1)

title_label = Label(header_frame, text="Event Management System", font=("Arial", 15, "bold"))
title_label.grid(padx=195, pady=30)


home_page_window()

root.mainloop()

