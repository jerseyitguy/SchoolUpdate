from tkinter import *
from tkinter import messagebox
import os

def MainMenu():

        
    MainMenuWin=Tk()
    MainMenuWin.title("Main Menu")
    MainMenuWin.geometry("200x200")
    
    frame1=Frame(MainMenuWin)
    frame1.pack()
                           
    btn1=Button(frame1,text="Add Teacher",command=AddTeacher)
    btn2=Button(frame1,text="Payroll",command= Payroll)
    
    frame2=Frame(MainMenuWin)
    frame2.pack()

    btn3=Button(frame2,text="Add User",command=AddUser)
    
    frame3=Frame(MainMenuWin)
    frame3.pack()

    btn4=Button(frame3,text="Logout",command=LoginScreen)
    btn5=Button(frame3,text="Exit",command=MainMenuWin.destroy)
            
    btn1.pack()
    btn2.pack()
    btn3.pack()
    btn4.pack(side=LEFT)
    btn5.pack(side=LEFT)
            
def Payroll():
    
    os.system('python Payroll.py')
    
def AddTeacher():

    def SaveTeacher() :

        TeacherIDSave = TeacherIDVar.get()
        TeacherIDSave = TeacherIDSave.ljust(50)
    
        FirstnameSave = FirstnameVar.get()
        FirstnameSave = FirstnameSave.ljust(50)
    
        SurnameSave = SurnameVar.get()
        SurnameSave = SurnameSave.ljust(50)
    
        AddressSave = AddressVar.get()
        AddressSave = AddressSave.ljust(50)
    
        PostCodeSave = PostCodeVar.get()
        PostCodeSave = PostCodeSave.ljust(50)

        QualSave = QualVar.get()
        QualSave = QualSave.ljust(50)
        
    
        fileObject = open("TeacherDetails.txt","a")
        
        fileObject.write(TeacherIDSave + FirstnameSave + SurnameSave + AddressSave + PostCodeSave + QualSave + "\n")
        fileObject.close()
        
        messagebox.showinfo("Confirmation","Teacher details successfully saved")
    
    AddTeacherWin=Tk()
    AddTeacherWin.title("Add Teacher")
    AddTeacherWin.geometry("300x300")
    
    frame1=Frame(AddTeacherWin)
    frame1.pack()

       
    Label(frame1, text="TeacherID").grid(row=3, column=0, sticky=W)
    TeacherIDVar=StringVar()
    TeacherIDVar= Entry(frame1, textvariable=TeacherIDVar)
    TeacherIDVar.grid(row=3,column=1,sticky=W)

    Label(frame1, text="Firstname").grid(row=4, column=0, sticky=W)
    FirstnameVar=StringVar()
    FirstnameVar= Entry(frame1, textvariable=FirstnameVar)
    FirstnameVar.grid(row=4,column=1,sticky=W)
    
    Label(frame1, text="Surname").grid(row=5, column=0, sticky=W)
    SurnameVar=StringVar()
    SurnameVar= Entry(frame1, textvariable=SurnameVar)
    SurnameVar.grid(row=5,column=1,sticky=W)
    
    Label(frame1, text="Address").grid(row=6, column=0, sticky=W)
    AddressVar=StringVar()
    AddressVar= Entry(frame1, textvariable=AddressVar)
    AddressVar.grid(row=6,column=1,sticky=W)
    
    Label(frame1, text="Postcode").grid(row=7, column=0, sticky=W)
    PostCodeVar=StringVar()
    PostCodeVar= Entry(frame1, textvariable=PostCodeVar)
    PostCodeVar.grid(row=7,column=1,sticky=W)

    Label(frame1, text="Qualification").grid(row=8, column=0, sticky=W)
    QualVar=StringVar()
    QualVar= Entry(frame1, textvariable=QualVar)
    QualVar.grid(row=8,column=1,sticky=W)
  

    frame2 = Frame(AddTeacherWin)
    frame2.pack()
    b1= Button(frame2, text=" Back ", command=AddTeacherWin.destroy)
    b2= Button(frame2, text=" Save ", command=SaveTeacher)
    b1.pack(side=LEFT); b2.pack(side=LEFT)



    
    

    
def AddUser():
    
    def SaveUser() :

        UserIDSave = UserIDVar.get()
        UserIDSave = UserIDSave.strip()
    
        PasswordSave = PasswordVar.get()
        PasswordSave = PasswordSave.strip()
    
       
        fileObject = open("data.dat","a")
        
        fileObject.write(UserIDSave + " " + PasswordSave + "\n")
        fileObject.close()
        
        messagebox.showinfo("Confirmation","Password successfully saved")
    
    AddUserWin=Tk()
    AddUserWin.title("Add User")
    AddUserWin.geometry("300x300")
    
    frame1=Frame(AddUserWin)
    frame1.pack()

       
    Label(frame1, text="UserID").grid(row=3, column=0, sticky=W)
    UserIDVar=StringVar()
    UserIDVar= Entry(frame1, textvariable=UserIDVar)
    UserIDVar.grid(row=3,column=1,sticky=W)

    Label(frame1, text="Password").grid(row=4, column=0, sticky=W)
    PasswordVar=StringVar()
    PasswordVar= Entry(frame1, textvariable=PasswordVar)
    PasswordVar.grid(row=4,column=1,sticky=W)
    
     

    frame2 = Frame(AddUserWin)
    frame2.pack()
    b1= Button(frame2, text=" Back ", command=AddUserWin.destroy)
    b2= Button(frame2, text=" Save ", command=SaveUser)
    b1.pack(side=LEFT); b2.pack(side=LEFT)

    
    
def LoginScreen():
    
    def login():
        username=usname.get()
        passwd=password.get()
        flag=TRUE

        if username.strip() == "" and passwd.strip() == "":
            messagebox.showinfo("Error","Blank username and password")
        elif passwd.strip() == "":
            messagebox.showinfo("Error","Blank password")
        elif username.strip()== "":
            messagebox.showinfo("Error","Blank username")
        else:
            
            passwordfile = open("data.dat","r")
            passvar = passwordfile.readline()
                            
            while flag and passvar !="":
                                      
                if passvar.find(username.strip()) >=0 and passvar.find(passwd.strip())>=0:
                    messagebox.showinfo("Authenticated","Correct username and password")
                    flag = FALSE
                                    
                passvar = passwordfile.readline()
                                
                passwordfile.close()
                if flag:
                 messagebox.showinfo("Error","Incorrect username and / or password")
                else:
                    loginwindow.destroy()
                    MainMenu()
                                

        
    loginwindow=Tk()
    loginwindow.title("Log In Screen")
    loginwindow.geometry("300x300")
    lbluname=Label(loginwindow, text="Username")
    usname=Entry(loginwindow)
    lblpass=Label(loginwindow, text="Password")
    password=Entry(loginwindow)

    lbluname.pack()
    usname.pack()
    lblpass.pack()
    password.pack()

    btn=Button(loginwindow,text="Log In",command=login).pack()

    loginwindow.mainloop()


LoginScreen()