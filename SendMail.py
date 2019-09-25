import tkinter as tk
from tkinter import scrolledtext
import smtplib

class login:
    global email
    global pwd
    def __init__(self,master):
        self.master=master
        master.title('SendMail')
        master.geometry('250x80')

        self.idlbl=tk.Label(master,text='Email ID:')
        self.idlbl.grid(column=0,row=0)
        self.identry=tk.Entry(master,width=30)
        self.identry.grid(column=1,row=0)

        self.pwlbl=tk.Label(master,text='Password:')
        self.pwlbl.grid(column=0,row=1)
        self.pwentry=tk.Entry(master,width=30,show="*")
        self.pwentry.grid(column=1,row=1)

        self.sbmt=tk.Button(master,text='Login with TLS security',command=self.logincmd)
        self.sbmt.grid(columnspan=2,row=2)
        email=self.identry.get()
        pwd=self.pwentry.get()
    def logincmd(self):
        self.newwindow=tk.Toplevel(self.master)
        self.app=compose(self.newwindow)
            

        

class compose():
    global reciever
    global message
    def __init__(self,master):
        
        self.master=master
        self.to=tk.Label(self.master,text='To:')
        self.to.grid(column=0,row=0)

        self.toentry=tk.Entry(self.master,width=56)
        self.toentry.grid(column=1,row=0)

        self.composelbl=tk.Label(self.master,text='Compose:')
        self.composelbl.grid(column=0,row=1)
        
        self.composetext=scrolledtext.ScrolledText(self.master,width=40,height=10)
        self.composetext.grid(column=1,row=1)
        
        self.sendbtn=tk.Button(self.master,text='SendMail :)',width=10,command=self.send)
        self.sendbtn.grid(columnspan=2,row=2)

        self.logoutbtn=tk.Button(self.master,text='Logout',width=10,command=self.logout)
        self.logoutbtn.grid(columnspan=2,row=3)

        self.reciever=self.toentry.get()
        self.message=self.composetext.get("1.0", tk.END)
    def send(self):
        try:
            obj=smtplib.SMTP('smtp.gmail.com',587)
            obj.starttls()
            obj.login(email,pwd)
            obj.sendmail(email,self.reciever,self.message)
        except:
            print('error in sending mail')
    def logout(self):
        self.master.destroy()
def main():
    master=tk.Tk()
    app=login(master)
if __name__=='__main__':
    main()
            

                            
