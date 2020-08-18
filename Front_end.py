"""Piano Flex, developed by PRAISE JAMES copyright @ 2020, simple basic piano with GUI"""
#imports
import pygame
import back_end
import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
 
root = Tk()
class TK_UI(tk.Button):
    def __init__(self, master, **kw):
          #-set icon-
        try:
            self.root.wm_iconbitmap("icon.png")
        except:
            pass
        #set windows size
        root.geometry('600x500')
        #set title
        root.title("Piano Flex 1.0")
        #make window unresizable
        root.resizable(False, False)
 
        #hover button effects
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
 
        #set background image
        img = PhotoImage(file = "mainmenu_bg.png")
        img = img.subsample(1, 1)
        background = Label(root, image = img, bd = 0)
        background.grid()
        background.image = img
 
        
    def on_enter(self, e):
        self['background'] = self['activebackground']
 
    def on_leave(self, e):
        self['background'] = self.defaultBackground
 
 
def ShowAbout():
    showinfo ("Piano Flex 1.0", "made by Praise James for sake of coding practice,\n Good to have fun with music some times :) \n although not all the resources used in this project were all made by the developer\n in this accord, the developer would like to give credit to \n where is due:\n BACKGROUND IMAGES: http://www.wallpaperscraft.com\n ")
 
def quitApplication():
    root.destroy()
    #exit
 
#apply hover effects on buttons
Button1 = TK_UI(root, text = "PLAY THE PIANO", font = ('algerian', 20, 'bold', 'underline'),bg = 'blue', foreground = 'red', activebackground = 'gold', highlightbackground = "#bce8f1", highlightthickness = 1, relief = tk.SOLID, borderwidth = "4", command = None)
Button1.grid(row = 1, column = 5, padx = 100, pady = 25)
 
Button2 = TK_UI(root, text = "ABOUT AND CREDITS",font = ('algerian', 20, 'bold', 'underline'),bg = 'blue', foreground = 'red', activebackground = 'gold',highlightbackground = "#bce8f1", highlightthickness = 1, relief = tk.SOLID, borderwidth = "4", command = ShowAbout)
Button2.grid(row = 5, column = 5, padx = 100, pady = 25)
 
Button3 = TK_UI(root, text = "QUIT !",font = ('algerian', 20, 'bold', 'underline'), bg = 'blue', foreground = 'red', activebackground = 'gold', highlightbackground = "#bce8f1", highlightthickness = 1, relief = tk.SOLID, borderwidth = "4", command = quitApplication)
Button3.grid(row = 7, column = 5, padx = 100, pady = 25)
 
root.mainloop()
