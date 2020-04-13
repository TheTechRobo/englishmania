import tkinter as t
from tkinter import messagebox as tkMB
from tkinter import *
from runpy import run_path as r

top = t.Tk()
intro = top
top.title('Englishmania!:Start')

def helloCallback():
   #create child window
   whatIs = Toplevel()
   whatIs.title("What is Englishmania!?")
   #display message
   Label(whatIs, text="Englishmania! is a spelling/grammar game about English.").pack()
   Label(whatIs, text="It is based off of gui-app.")
   Button(whatIs, text="OK", command=whatIs.destroy).pack()
def aboutCallback():
   #create child window
   about = Toplevel()
   about.title("About Englishmania!")
   #display message
   Label(about, text='''Englishmania!
   
   CREDITS: (NOT AFFILIATED WITH ANY OF THESE SITES)
   
   Thanks to tiny.cc/tkinterguide for providing a guide.
   Thanks also to shields.io for the README.md badges.
   Thanks also to pythonprogramming.net/tkinter-adding-text-images/ for a nice article (can't remember what it taught me though)
   Thanks so much to the Python Software Foundation and TkInter -- without you this wouldn't exist!
   Thanks to smallguysit.com/index.php/2017/03/10/tkinter-create-window/ for `from Tkinter import *'
   Thanks to tiny.cc/childwindow for the guide on child windows -- it helped with this window!")
   Thanks to the book Python for Kids that helped me learn Python.
   
   Thanks to all!
   
   Englishmania! is licensed under the DBAD license. You should have received a copy; else go to http://tiny.cc/dbad.'''
   #quit child window and return to root window
   #the button is optional here, simply use the corner x of the child window
   Button(about, text='OK', command=about.destroy).pack()
def badaCallback():
   print("Loading..")
   top.destroy()
   r(path_name=".gui/.selection.py")
def notCodedCallback():
   tkMB.showerror("Sorry", "Not coded yet")
def showMoreCallback():
   BBada.pack()
def badaCB():
   BAbt.pack()
   Button(top, text='Exit', command=top.destroy).pack()
   Button(top, command=easterEggCallback).pack()
def messageWindow():
    #create child window
    newWindow = Toplevel()
    #display message
    message = "This is the child window"
    Label(newWindow, text=message).pack()
    #quit child window and return to root window
    #the button is optional here, simply use the corner x of the child window
    Button(newWindow, text='OK', command=newWindow.destroy).pack()
def exitCallback():
	print("Okay, bye :(")
	exit()

BWhatIs = t.Button(top, text ="What is Englishmania!?", command = helloCallback)
BAbt = t.Button(top, text ="About...", command=aboutCallback).pack()
BSt = t.Button(top, text ="START!", command= badaCallback)
BExit = t.Button(top, text="Exit :(", command=exitCallback)

Label(top, text="Welcome to Englishmania!").pack()

BWhatIs.pack()
BSt.pack()

tkMB.showinfo("Willkomen!", "Welcome to Englishmania!!")


top.mainloop()
