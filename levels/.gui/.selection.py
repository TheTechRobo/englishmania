from tkinter import *
import tkinter as t
from runpy import run_path as r
from sys import exit
selection = t.Tk()
selection.title('Level Selection')

def runOne():
    r(path_name='.1.py')
    selection.destroy()
def runTwo():
    selection.destroy()
    r(path_name='.2.py')
def exitAM():
	exit()

Button(selection, text="Level 1", command=runOne).pack()
Button(selection, text="Level 2", command=runTwo).pack()
Button(selection, text="Cancel", command=exitAM).pack()

Label(selection, text = 'Select a Level ' , font=('Arial' , 17), fg='black', width=11, height=2).pack()


selection.mainloop()
