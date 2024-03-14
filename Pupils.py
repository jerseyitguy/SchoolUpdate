from tkinter import *
from tkinter import messagebox
    
AddPupilWin=Tk()
AddPupilWin.title("Add Pupil")
AddPupilWin.geometry("300x300")




def SavePupil() :

    PupilIDSave = PupilIDVar.get()
    if PupilIDSave.strip() == "":
        messagebox.showinfo("Error","Blank username and password")
    else:
       PupilIDSave = PupilIDSave.ljust(50)
   
       FirstnameSave = FirstnameVar.get()
       if any(char.isdigit() for char in FirstnameSave):
            FirstnameSave = FirstnameSave.ljust(50)
            messagebox.showinfo("Error","Number in Pupil Name")
       else:
    
            SurnameSave = SurnameVar.get()
            SurnameSave = SurnameSave.ljust(50)
        
            AddressSave = AddressVar.get()
            AddressSave = AddressSave.ljust(50)
        
            PostCodeSave = PostCodeVar.get()
            PostCodeSave = PostCodeSave.ljust(50)
        
            QualSave = QualVar.get()
            QualSave = QualSave.ljust(50)
            
        
            fileObject = open("PupilDetails.txt","a")
            
            fileObject.write(PupilIDSave + FirstnameSave + SurnameSave + AddressSave + PostCodeSave + QualSave + "\n")
            fileObject.close()
            
            messagebox.showinfo("Confirmation","Pupil details successfully saved")



frame1=Frame(AddPupilWin)
frame1.pack()

   
Label(frame1, text="PupilID").grid(row=3, column=0, sticky=W)
PupilIDVar=StringVar()
PupilIDVar= Entry(frame1, textvariable=PupilIDVar)
PupilIDVar.grid(row=3,column=1,sticky=W)

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


frame2 = Frame(AddPupilWin)
frame2.pack()
b1= Button(frame2, text=" Back ", command=AddPupilWin.destroy)
b2= Button(frame2, text=" Save ", command=SavePupil)
b1.pack(side=LEFT); b2.pack(side=LEFT)


    
AddPupilWin.mainloop()
