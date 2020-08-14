"""Piano Flex, developeds by PRAISE JAMES copyright @ 2020, simple basic piano with GUI"""
#imports
import pygame
import back_end
import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
 
root = Tk()
class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
 
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
Button1 = HoverButton(root, text = "PLAY THE PIANO", font = ('algerian', 20, 'bold', 'underline'),bg = 'blue', foreground = 'red', activebackground = 'gold', highlightbackground = "#bce8f1", highlightthickness = 1, relief = tk.SOLID, borderwidth = "4", command = None)
Button1.grid(row = 1, column = 3, padx = 10, pady = 10)
 
Button2 = HoverButton(root, text = "ABOUT AND CREDITS",font = ('algerian', 20, 'bold', 'underline'),bg = 'blue', foreground = 'red', activebackground = 'gold',highlightbackground = "#bce8f1", highlightthickness = 1, relief = tk.SOLID, borderwidth = "4", command = None)
Button2.grid(row = 3, column = 3, padx = 10, pady = 10)
 
Button3 =HoverButton(root, text = "QUIT !",font = ('algerian', 20, 'bold', 'underline'), bg = 'blue', foreground = 'red', activebackground = 'gold', highlightbackground = "#bce8f1", highlightthickness = 1, relief = tk.SOLID, borderwidth = "4", command = None)
Button3.grid(row = 5, column = 3, padx = 10, pady = 10)
 
root.mainloop()
