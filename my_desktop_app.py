try:
    from Tkinter import *
    from Tkinter import ttk
    #code for importing Tkinter in Python 2
    
except:
    import time
    from tkinter import *
    from tkinter import ttk
    #code for importing Tkinter in Python 3

import os
import csv
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email import encoders

count,c = 0,0

details = 'tempfile.temp'
#this sets the login details to 'tempfile.temp'

def mail():
    def attach():
        count += 1
        master.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

        file = Label(master, text = master.filename)
        file.grid(row = 1, column = 0, sticky = W)

    def Pass():
        pass

    def Sendmail():

        sender = 'edidiongumoh84@gmail.com'
        password = 'Iniedymimieky04'

        message = MIMEMultipart()
        message['From'] = 'edidiongumoh84@gmail.com'
        message['To'] = to_email_entry.get()
        message['Subject'] = subject_entry.get()

        body = email_content.get("1.0","end")
        message.attach(MIMEText(body, 'plain'))

        if count > 0:
            #open the file to be sent
            filename = master.filename
            attachment = open(fname, 'rb')
            app = MIMEBase('application', 'octet-stream')
            app.set_payload((attachment).read())
            encoders.encode_base64(app)
            app.add_header('Content-Disposition', 'attachment; filename = "%s"' % os.path.basename(attach))
            message.attach(app)

        else:
            pass
        text = message.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(sender, password)

        try:
            server.sendmail(sender, message['To'], text)
            c += 1
            print('Email has been successfully sent')

        except:
            print('The message could not be sent')

        server.quit()
        master.destroy()

        if c >= 1:

            r = Tk()
            r.geometry('250 x 100')
            rLabel = Label(r, text = 'Email Sent Successfully')
            rLabel.pack()
            r.mainloop()

        else:

            r = Tk()
            r.geometry('250 x 100')
            rLabel = Label(r, text = 'Message not sent')
            rLabel.pack()
            r.mainloop()        
            

    master = Tk()
    master.title("Mail Message")
        
    myfont = ('arial', 12, 'bold')
    my_font = ('Times New Roman', 12, 'bold')
    
    #create the first button on the first row
    send = Button(master, font = myfont, text = 'Send Mail', bg = 'red', fg = 'white', command = Sendmail)
    send.grid(row = 0, column = 0, sticky = W)

    #create the 'Attach' label on the first row
    attach = Button(master, font = myfont, text = 'Attach', bg = 'grey', fg = 'white', command = attach)
    attach.grid(row = 0, column = 1, sticky = W)
              
    #create the 'To:' label on the second row
    to_email = Label(master, font = myfont, text = 'To: ')
    to_email.grid(row = 1, column = 0, pady = 5, padx = 5, sticky = W)
    to_email_entry = Entry(master, font = my_font, bd = 10, width = 70)
    to_email_entry.grid(row = 1, column = 1, pady = 5, padx = 5, sticky = W)
    
    #create the 'Subject' label on the third row
    subject = Label(master, font = myfont, text = 'Subject: ')
    subject.grid(row = 2, column = 0, pady = 5, padx = 5, sticky = W)
    subject_entry = Entry(master, font = my_font, bd = 10, width = 70)
    subject_entry.grid(row = 2, column = 1, pady = 5, padx = 5, sticky = W)
    
    #create the text box to contain the main letter of the email
    email_content = Text(master, font = ('Times New Roman', 12), width = 100, height = 22)
    email_content.grid(row = 3, column = 1, columnspan = 2, pady = 5, padx = 5, sticky = E)

    master.geometry("1000x700")
    master.mainloop()

def send():
    
    root = Tk()
    root.title('Send New Email')
    root.geometry('300 x 150')
    new_email = Button(root, text = 'New Email', command = mail)
    new_email.grid(row = 1, column = 0, sticky = N)

    quit_email = Button(root, text = 'Log Out', command = logout)
    quit_email.grid(row = 1, column = 1, sticky = N)

    root.mainloop()

def logout():
    root.destroy()
    window = Tk()
    window.title('Quit')
    window.geometry('200 x 100')

    quit_label = Label(window, text = 'Successfully Logged Out.')
    quit_label.pack()
    window.mainloop()
    login()

def Signup():
    global master
    global usernameEL
    global p_wordEL
    
    master = Tk()
    master.title('Email SignUp')
    register = Label(master, text = 'Register New Credentials\n')
    register.grid(row = 0, column = 0, sticky = E)

    usernameL = Label(master, text = 'Enter New Username: ')
    usernameL.grid(row = 1, column = 0, sticky = W)
    usernameEL = Entry(master)
    usernameEL.grid(row = 1, column = 1)

    p_wordL = Label(master, text = 'Enter Your Password: ')
    p_wordL.grid(row = 2, column = 0, sticky = W)
    p_wordEL = Entry(master, show = '*')
    p_wordEL.grid(row = 2, column = 1)

    SUButton = Button(master, text = 'Please Signup', command = EmailSignUp)
    SUButton.grid(columnspan = 2, sticky = W)
    master.mainloop()

def EmailSignUp():
    
    with open(details, 'w') as file:
        file.write(usernameEL.get())
        file.write('\n')
        file.write(p_wordEL.get())
        file.close()

    master.destroy()
    Login()

def Login():
    global nameEL
    global passwordEL

    r = Tk()
    r.title('Login')

    login = Label(r, text = 'Please Login')
    

    nameL = Label(r, text = 'Username: ')
    nameL.grid(row = 1, sticky = W)
    nameEL = Entry(r)
    nameEL.grid(row = 1, column = 1)

    passwordL = Label(r, text = 'Password: ')
    passwordL.grid(row = 2, sticky = W)
    passwordEL = Entry(r, show = '*')
    passwordEL.grid(row = 2, column = 1)

    loginB = Button(r, text = 'Login', command = SignIn)
    loginB.grid(columnspan = 2, sticky = W)

    delete_user = Button(r, text = 'Delete User', fg = 'red', command = DeleteUser)
    delete_user.grid(columnspan = 2, sticky =W)
    r.mainloop()

def SignIn():
    with open(details) as f:
        info = f.readlines()
        u_name = info[0].rstrip()
        p_word = info[1].rstrip()

    if nameEL.get() == u_name and passwordEL.get() == p_word:
        w = Tk()
        w.geometry('150x50')
        wLabel = Label(w, text = 'Log In Successful')
        wLabel.pack()
        w.mainloop()

    else:
        w = Tk()
        w.geometry('150x50')
        wLabel = Label(w, text = 'Invalid Login Details')
        wLabel.pack()
        w.mainloop()


def DeleteUser():
    os.remove(details)
    r.destroy()
    Signup()

if os.path.isfile(details):
    Login()

else:
    Signup()




