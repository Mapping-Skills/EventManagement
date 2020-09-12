from tkinter import *
def about(root):
    root.destroy()
    top=Tk()

    top.title("about")
    top.configure(bg='#CDDEF9')

    top.maxsize()

    header_frame = Frame(top, bg="#72F107")
    header_frame.pack()
    v0 = (" Feroze Gandhi Institute of Professional Studies")
    l0 = Label(header_frame, font=("Courier New", 28, "bold"), text=v0, fg="black", bg="red")
    l0.pack()


    v1=("* Feroze Gandhi Institute of Professional Studies is a premier institute, established with a vision to develop worldclass technical\n professionals.")
    v2=("* FGIPS having a spectacular campus of 22.5 acre with several conspicuous features.")
    v3=("* It Offers an amiable, verdant and eco-friendly atmosphere to the students and fosters them to be more meditative,\n veracious and focused.")
    v4=("* Feroze Gandhi Institute of Professional Studies is a premier institute, established with a vision to produce the best technical \nprofessionals.")
    v5=("* FGIPS has a spectacular campus of 22.5 acre with several conspicuous features.")
    v6=("* It offers an amiable, verdant and eco-friendly atmosphere to students in order to make them more meditative, veracious and\n focused.")
    v7=("* Besides state-of-the-art Library and Computer Centre FGIPS also offers best residential facility for its students.")
    v8=("* The spacious campus includes recreation room, indoor-outdoor game facility, round the clock electric power supply and \nround the clock available reading facilities.")
    v9=("Founded:-2017\nSpecialties:-BBA and BCA \nAddress:- Ratapur, Rae Bareli, Uttar Pradesh")

    header_frame_in = Frame(top, bg='#CDDEF9')
    header_frame_in.pack(side="left")

    l1=Label(header_frame_in,font=("Comic Sans Ms",15,"bold"),text=v1,fg="black",bg="#CDDEF9")
    l1.pack()
    l2=Label(header_frame_in,font=("Comic Sans Ms",15,"bold"),text=v2,fg="black",bg="#CDDEF9")
    l2.pack()
    l3=Label(header_frame_in,font=("Comic Sans Ms",15,"bold"),text=v3,fg="black",bg="#CDDEF9")
    l3.pack()
    l4=Label(header_frame_in,font=("Comic Sans Ms",15,"bold"),text=v4,fg="black",bg="#CDDEF9")
    l4.pack()
    l5=Label(header_frame_in,font=("Comic Sans Ms",15,"bold"),text=v5,fg="black",bg="#CDDEF9")
    l5.pack()
    l6=Label(header_frame_in,font=("Comic Sans Ms",15,"bold"),text=v6,fg="black",bg="#CDDEF9")
    l6.pack()
    l7=Label(header_frame_in,font=("Comic Sans Ms",15,"bold"),text=v7,fg="black",bg="#CDDEF9")
    l7.pack()
    l8=Label(header_frame_in,font=("Comic Sans Ms",15,"bold"),text=v8,fg="black",bg="#CDDEF9")
    l8.pack()
    l9=Label(header_frame_in,font=("Comic Sans Ms",15,"bold"),text=v9,fg="red",bg="yellow")
    l9.pack()
    top.mainloop()