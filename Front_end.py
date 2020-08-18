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
            self.root.wm_iconbitmap("images/icon.png")
        except:
            pass
        #set windows size
        root.geometry('600x500')
        #set title
        root.title("Piano Flex 1.0")
        #make window unresizable
        root.resizable(False, False)
 
        root.configure(bg = 'Green')
 
        #hover button effects
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
 
#set background image
filename = 'images/mainmenu_bg.png'
 
canvas = tk.Canvas(root, width = 600, height = 500)
canvas.pack()
tk_img = PhotoImage(file = filename)
canvas.create_image(110, 250, image = tk_img)
 
#apply hover effects on buttons
Button1 = TK_UI(root, text = "PLAY THE PIANO", font = ('algerian', 20, 'bold', 'underline'),bg = 'blue', foreground = 'red', activebackground = 'gold', highlightbackground = "#bce8f1", highlightthickness = 1, relief = tk.SOLID, borderwidth = "4", command = None)
Button1win = canvas.create_window(187, 70, anchor = 'nw', window = Button1)
 
Button2 = TK_UI(root, text = "ABOUT AND CREDITS",font = ('algerian', 20, 'bold', 'underline'),bg = 'blue', foreground = 'red', activebackground = 'gold',highlightbackground = "#bce8f1", highlightthickness = 1, relief = tk.SOLID, borderwidth = "4", command = ShowAbout)
Button2win = canvas.create_window(160, 185, anchor = 'nw', window = Button2)
 
Button3 = TK_UI(root, text = "QUIT !",font = ('algerian', 20, 'bold', 'underline'), bg = 'blue', foreground = 'red', activebackground = 'gold', highlightbackground = "#bce8f1", highlightthickness = 1, relief = tk.SOLID, borderwidth = "4", command = quitApplication)
Button3win = canvas.create_window(250, 300, anchor = 'nw', window = Button3)
 
root.mainloop()
