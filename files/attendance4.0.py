#import module from tkinter for UI
from tkinter import *
#from playsound import playsound
import os
from datetime import datetime;
#import main2
import main2 as m
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")
entryglo = ""
def function1():
    m.recognize()
    #os.system("py dataset_capture.py")
    
def function2():
    newwin = Toplevel(root)
    display = Label(newwin, text="Enter your name")
    display.pack()
    entry = Entry(newwin)
    entry.pack()
    #entryglo=entry.get()
    button = Button(newwin, text="ok",command= lambda: functiona(entry,newwin))
    button.pack()
    print(entry)
    #os.system("py training_dataset.py")
        #playsound('sound.mp3')
def functiona(entry,newwin):
    a=entry.get()
    print(a)
    newwin.destroy()
    m.register(a)
    
def function5():    
   os.startfile(os.getcwd()+"/developers/diet1frame1first.html");
   
def function6():

    root.destroy()

def attend():
    os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')

#stting title for the window
root.title("WELCOME TO ATTENDANCE 4.0")

#creating a text label
Label(root, text="WELCOME TO ATTENDANCE 4.0",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Recognize",font=("times new roman",20),bg="#0D47A1",fg='white',command=function1).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Register",font=("times new roman",20),bg="#0D47A1",fg='white',command=function2).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#0D47A1",fg="white",command=attend).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Developers",font=('times new roman',20),bg="#0D47A1",fg="white",command=function5).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=function6).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
