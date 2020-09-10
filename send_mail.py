import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox



def send(email, password, username):
    # Header --> from, to, subject

    from_mail = "pakpakpakya302@gmail.com"

    to_mail = email

    subject = "Your Login Details"

    msg = MIMEMultipart()
    msg["From"] = from_mail
    msg["To"] = to_mail
    msg["Subject"] = subject

    # Body

    body = "Your Username Is: " + username + "\nYour Password Is: " + password
    msg.attach(MIMEText(body, "plain"))

    # attaching attachments

    #     my_file = open(filename, "rb")

    #     part = MIMEBase("application", "octet-stream")

    #     part.set_payload(my_file.read())

    #     encoders.encode_base64(part)

    #     part.add_header("Content-Disposition", "attachment; filename=" + filename)
    #     msg.attach(part)

    # converting message as string

    message = msg.as_string()

    # Creating server

    server = smtplib.SMTP("smtp.gmail.com", 587)

    # For Secure connection

    server.starttls()

    # Login

    server.login(from_mail, "ghhdppyhtgpferpe")

    # Sending mail

    server.sendmail(from_mail, to_mail, message)

    server.quit()
    messagebox.showinfo("Successful", "Login Details Sent To: " + to_mail)
