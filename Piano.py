"""Piano Flex, developed by PRAISE JAMES @ 2020, simple basic piano GUI"""
import pygame, winsound, sys
from pygame.locals import *
from tkinter import *
from tkinter.messagebox import *

root = Tk()
class TK_UI(Button):
    def __init__(self, master, **kw):
        root.geometry('600x500')
        root.title("Piano Flex 1.0")
        root.resizable(False, False)

        Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):self['background'] = self['activebackground']
    def on_leave(self, e):self['background'] = self.defaultBackground

def ShowAbout():showinfo ("Piano Flex 1.0", "made by Praise James for sake of coding practice,\n Good to have fun with music some times :) \n although not all the resources used in this project were all made by the developer\n in this accord, the developer would like to give credit to \n where is due:\n BACKGROUND IMAGES: http://www.wallpaperscraft.com\n ")
def quitApplication():root.destroy()

def KeyBoard():
    global WHITE, BLACK, GREEN, screen, bg
    root.destroy()
    pygame.init()
    screen = pygame.display.set_mode((747, 700), 0, 32)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)
    light_shade = (170, 170, 170)
    dark_shade = (100, 100, 100)
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render('BACK', True, WHITE)
    pygame.display.set_caption('Piano Flex 1.0')
    try:
        bg = pygame.image.load('piano_bg.jpg')
        screen.blit(bg, (0, 80))
    except: pass
    draw()
    run()

def draw():
    screen.blit(bg, (0, 80))
    x = 20
    for i in range(16):
        pygame.draw.rect(screen, WHITE, (x, 150, 40, 230))
        x += 43
    #come back to automating this
    """x = 45
    for i in range(4):
        for i in range(2):
            pygame.draw.rect(screen, BLACK, (x, 150, 30, 120))
            x += 44
        x+=80
    x1 = 174
    for i in range(2):
        pygame.draw.rect(screen, BLACK, (x1, 150, 30, 120))
        x1 += 332
    """#-Black keys-
    key17 = pygame.draw.rect(screen, BLACK, (45, 150, 30, 120))
    key18 = pygame.draw.rect(screen, BLACK, (89, 150, 30, 120))
    key19 = pygame.draw.rect(screen, BLACK, (174, 150, 30, 120))
    key20 = pygame.draw.rect(screen, BLACK, (218, 150, 30, 120))
    key21 = pygame.draw.rect(screen, BLACK, (262, 150, 30, 120))
    key22 = pygame.draw.rect(screen, BLACK, (347, 150, 30, 120))
    key23 = pygame.draw.rect(screen, BLACK, (391, 150, 30, 120))
    key24 = pygame.draw.rect(screen, BLACK, (476, 150, 30, 120))
    key25 = pygame.draw.rect(screen, BLACK, (520, 150, 30, 120))
    key26 = pygame.draw.rect(screen, BLACK, (564, 150, 30, 120))
    key27 = pygame.draw.rect(screen, BLACK, (649, 150, 30, 120))

    #button variables
    light_shade = (170, 170, 170)
    dark_shade = (100, 100, 100)
    smallfont = pygame.font.SysFont('Corbel', 35)
    text = smallfont.render('BACK', True, WHITE)

#===================SOUND METHODS REGION==============================
def lowcnote():
    Freq = 180
    Dur = 400
    winsound.Beep(Freq, Dur)

def cnote():
    Freq = 1046
    Dur = 200
    winsound.Beep(Freq, Dur)

def dnote():
    Freq = 1174
    Dur = 200
    winsound.Beep(Freq, Dur)

def enote():
    Freq = 1318
    Dur = 200
    winsound.Beep(Freq, Dur)

def fnote():
    Freq = 1397
    Dur = 200
    winsound.Beep(Freq, Dur)

def gnote():
    Freq = 1568
    Dur = 200
    winsound.Beep(Freq, Dur)

def anote():
    Freq = 1760
    Dur = 200
    winsound.Beep(Freq, Dur)

def bflatnote():
    Freq = 1864
    Dur = 200
    winsound.Beep(Freq, Dur)

def bnote():
    Freq = 1975
    Dur = 200
    winsound.Beep(Freq, Dur)

def hcnote():
    Freq = 2093
    Dur = 200
    winsound.Beep(Freq, Dur)
# Second Octive up for regular duration

def hcnote():
    Freq = 2093
    Dur = 200
    winsound.Beep(Freq, Dur)

def hdnote():
    Freq = 2349
    Dur = 200
    winsound.Beep(Freq, Dur)

def henote():
    Freq = 2637
    Dur = 200
    winsound.Beep(Freq, Dur)

def hfnote():
    Freq = 2793
    Dur = 200
    winsound.Beep(Freq, Dur)

def hgnote():
    Freq = 3135
    Dur = 200
    winsound.Beep(Freq, Dur)

def hanote():
    Freq = 3520
    Dur = 200
    winsound.Beep(Freq, Dur)

def hbnote():
    Freq = 3951
    Dur = 200
    winsound.Beep(Freq, Dur)

# Long time length for these notes
def lcnote():
    Freq = 1046
    Dur = 200
    winsound.Beep(Freq, Dur)

def ldnote():
    Freq = 1174
    Dur = 200
    winsound.Beep(Freq, Dur)

def lenote():
    Freq = 1318
    Dur = 200
    winsound.Beep(Freq, Dur)

def lfnote():
    Freq = 1397
    Dur = 200
    winsound.Beep(Freq, Dur)

def lgnote():
    Freq = 1568
    Dur = 200
    winsound.Beep(Freq, Dur)

def lanote():
    Freq = 1760
    Dur = 200
    winsound.Beep(Freq, Dur)

def lbflatnote():
    Freq = 1864
    Dur = 200
    winsound.Beep(Freq, Dur)

def lbnote():
    Freq = 1975
    Dur = 200
    winsound.Beep(Freq, Dur)

# Second Octive up for long duration
def lhcnote():
    Freq = 2093
    Dur = 800
    winsound.Beep(Freq, Dur)

def lhdnote():
    Freq = 2349
    Dur = 800
    winsound.Beep(Freq, Dur)

def lhenote():
    Freq = 2637
    Dur = 800
    winsound.Beep(Freq, Dur)

def lhfnote():
    Freq = 2793
    Dur = 800
    winsound.Beep(Freq, Dur)

def lhgnote():
    Freq = 3135
    Dur = 800
    winsound.Beep(Freq, Dur)

def lhanote():
    Freq = 3520
    Dur = 800
    winsound.Beep(Freq, Dur)

def lhbnote():
    Freq = 3951
    Dur = 800
    winsound.Beep(Freq, Dur)

# Short time length for these notes
def scnote():
    Freq = 1046
    Dur = 200
    winsound.Beep(Freq, Dur)

def sdnote():
    Freq = 1174
    Dur = 200
    winsound.Beep(Freq, Dur)

def senote():
    Freq = 1318
    Dur = 200
    winsound.Beep(Freq, Dur)

def sfnote():
    Freq = 1397
    Dur = 200
    winsound.Beep(Freq, Dur)

def sgnote():
    Freq = 1568
    Dur = 200
    winsound.Beep(Freq, Dur)

def sanote():
    Freq = 1760
    Dur = 200
    winsound.Beep(Freq, Dur)

def sbflatnote():
    Freq = 1864
    Dur = 200
    winsound.Beep(Freq, Dur)

def sbnote():
    Freq = 1975
    Dur = 200
    winsound.Beep(Freq, Dur)
# Second Octive up for short duration
def shcnote():
    Freq = 2093
    Dur = 200
    winsound.Beep(Freq, Dur)

def shdnote():
    Freq = 2349
    Dur = 200
    winsound.Beep(Freq, Dur)

def shenote():
    Freq = 2637
    Dur = 200
    winsound.Beep(Freq, Dur)

def shfnote():
    Freq = 2793
    Dur = 200
    winsound.Beep(Freq, Dur)

def shgnote():
    Freq = 3135
    Dur = 200
    winsound.Beep(Freq, Dur)

def shanote():
    Freq = 3520
    Dur = 200
    winsound.Beep(Freq, Dur)

def shbnote():
    Freq = 3951
    Dur = 200
    winsound.Beep(Freq, Dur)

def shfsharpnote():
    Freq = 2959
    Dur = 200
    winsound.Beep(Freq, Dur)

def shdsharpnote():
    Freq = 2489
    Dur = 200
    winsound.Beep(Freq, Dur)

def sgsharpnote():
    Freq = 1661
    Dur = 200
    winsound.Beep(Freq, Dur)

def hhcnote():
    Freq = 4186
    Dur = 400
    winsound.Beep(Freq, Dur)

def shhcnote():
    Freq = 4186
    Dur = 200
    winsound.Beep(Freq, Dur)

#==========================END OF SOUND REGION=========================

def run():
    #--event log--
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_a:
                     key1 = pygame.draw.rect(screen, GREEN, (20, 150, 40, 230))
                     key17 = pygame.draw.rect(screen, BLACK, (45, 150, 30, 120))
                     cnote()
                if event.key == K_s:
                    key2 = pygame.draw.rect(screen, GREEN, (63, 150, 40, 230))
                    key17 = pygame.draw.rect(screen, BLACK, (45, 150, 30, 120))
                    key18 = pygame.draw.rect(screen, BLACK, (89, 150, 30, 120))
                    dnote()
                if event.key == K_d:
                    key3 = pygame.draw.rect(screen, GREEN, (106, 150, 40, 230))
                    key18 = pygame.draw.rect(screen, BLACK, (89, 150, 30, 120))
                    enote()
                if event.key == K_f:
                    key4 = pygame.draw.rect(screen, GREEN, (149, 150, 40, 230))
                    key19 = pygame.draw.rect(screen, BLACK, (174, 150, 30, 120))
                    fnote()
                if event.key == K_g:
                    key5 = pygame.draw.rect(screen, GREEN, (192, 150, 40, 230))
                    key19 = pygame.draw.rect(screen, BLACK, (174, 150, 30, 120))
                    key20 = pygame.draw.rect(screen, BLACK, (218, 150, 30, 120))
                    gnote()
                if event.key == K_h:
                    key6 = pygame.draw.rect(screen, GREEN, (235, 150, 40, 230))
                    key20 = pygame.draw.rect(screen, BLACK, (218, 150, 30, 120))
                    key21 = pygame.draw.rect(screen, BLACK, (262, 150, 30, 120))
                    anote()
                if event.key == K_j:
                    key7 = pygame.draw.rect(screen, GREEN, (278, 150, 40, 230))
                    key21 = pygame.draw.rect(screen, BLACK, (262, 150, 30, 120))
                    bflatnote()
                if event.key == K_k:
                    key8 = pygame.draw.rect(screen, GREEN, (321, 150, 40, 230))
                    key22 = pygame.draw.rect(screen, BLACK, (347, 150, 30, 120))
                    bnote()
                if event.key == K_l:
                    key9 = pygame.draw.rect(screen, GREEN, (364, 150, 40, 230))
                    key22 = pygame.draw.rect(screen, BLACK, (347, 150, 30, 120))
                    key23 = pygame.draw.rect(screen, BLACK, (391, 150, 30, 120))
                    hcnote()
                if event.key == K_q:
                    key10 = pygame.draw.rect(screen, GREEN, (407, 150, 40, 230))
                    key23 = pygame.draw.rect(screen, BLACK, (391, 150, 30, 120))
                    hdnote()
                if event.key == K_w:
                    key11 = pygame.draw.rect(screen, GREEN, (450, 150, 40, 230))
                    key24 = pygame.draw.rect(screen, BLACK, (476, 150, 30, 120))
                    henote()
                if event.key == K_e:
                    key12 = pygame.draw.rect(screen, GREEN, (493, 150, 40, 230))
                    key24 = pygame.draw.rect(screen, BLACK, (476, 150, 30, 120))
                    key25 = pygame.draw.rect(screen, BLACK, (520, 150, 30, 120))
                    hfnote()
                if event.key == K_p:
                    key13 = pygame.draw.rect(screen, GREEN, (536, 150, 40, 230))
                    key25 = pygame.draw.rect(screen, BLACK, (520, 150, 30, 120))
                    key26 = pygame.draw.rect(screen, BLACK, (564, 150, 30, 120))
                    hgnote()
                if event.key == K_o:
                    key14 = pygame.draw.rect(screen, GREEN, (579, 150, 40, 230))
                    key26 = pygame.draw.rect(screen, BLACK, (564, 150, 30, 120))
                    hanote()
                if event.key == K_i:
                    key15 = pygame.draw.rect(screen, GREEN, (622, 150, 40, 230))
                    key27 = pygame.draw.rect(screen, BLACK, (649, 150, 30, 120))
                    hbnote()
                if event.key == K_u:
                    key16 = pygame.draw.rect(screen, GREEN, (665, 150, 40, 230))
                    key27 = pygame.draw.rect(screen, BLACK, (649, 150, 30, 120))
                    #lowcnote()
                    
            if event.type == KEYUP:
                if event.key == K_a:
                    key1 == pygame.draw.rect(screen, WHITE, (20, 150, 40, 230))
                    key17 = pygame.draw.rect(screen, BLACK, (45, 150, 30, 120))
                    key18 = pygame.draw.rect(screen, BLACK, (89, 150, 30, 120))
                if event.key == K_s:
                    key2 = pygame.draw.rect(screen, WHITE, (63, 150, 40, 230))
                    key17 = pygame.draw.rect(screen, BLACK, (45, 150, 30, 120))
                    key18 = pygame.draw.rect(screen, BLACK, (89, 150, 30, 120))
                if event.key == K_d:
                    key3 = pygame.draw.rect(screen, WHITE, (106, 150, 40, 230))
                    key18 = pygame.draw.rect(screen, BLACK, (89, 150, 30, 120))
                if event.key == K_f:
                    key4 = pygame.draw.rect(screen, WHITE, (149, 150, 40, 230))
                    key19 = pygame.draw.rect(screen, BLACK, (174, 150, 30, 120))
                if event.key == K_g:
                    key5 = pygame.draw.rect(screen, WHITE, (192, 150, 40, 230))
                    key19 = pygame.draw.rect(screen, BLACK, (174, 150, 30, 120))
                    key20 = pygame.draw.rect(screen, BLACK, (218, 150, 30, 120))
                if event.key == K_h:
                    key6 = pygame.draw.rect(screen, WHITE, (235, 150, 40, 230))
                    key20 = pygame.draw.rect(screen, BLACK, (218, 150, 30, 120))
                    key21 = pygame.draw.rect(screen, BLACK, (262, 150, 30, 120))
                if event.key == K_j:
                    key7 = pygame.draw.rect(screen, WHITE, (278, 150, 40, 230))
                    key21 = pygame.draw.rect(screen, BLACK, (262, 150, 30, 120))
                if event.key == K_k:
                    key8 = pygame.draw.rect(screen, WHITE, (321, 150, 40, 230))
                    key22 = pygame.draw.rect(screen, BLACK, (347, 150, 30, 120))
                if event.key == K_l:
                    key9 = pygame.draw.rect(screen, WHITE, (364, 150, 40, 230))
                    key22 = pygame.draw.rect(screen, BLACK, (347, 150, 30, 120))
                    key23 = pygame.draw.rect(screen, BLACK, (391, 150, 30, 120))
                if event.key == K_q:
                    key10 = pygame.draw.rect(screen, WHITE, (407, 150, 40, 230))
                    key23 = pygame.draw.rect(screen, BLACK, (391, 150, 30, 120))
                if event.key == K_w:
                    key11 = pygame.draw.rect(screen, WHITE, (450, 150, 40, 230))
                    key24 = pygame.draw.rect(screen, BLACK, (476, 150, 30, 120))
                if event.key == K_e:
                    key12 = pygame.draw.rect(screen, WHITE, (493, 150, 40, 230))
                    key24 = pygame.draw.rect(screen, BLACK, (476, 150, 30, 120))
                    key25 = pygame.draw.rect(screen, BLACK, (520, 150, 30, 120))
                if event.key == K_p:
                    key13 = pygame.draw.rect(screen, WHITE, (536, 150, 40, 230))
                    key25 = pygame.draw.rect(screen, BLACK, (520, 150, 30, 120))
                    key26 = pygame.draw.rect(screen, BLACK, (564, 150, 30, 120))
                if event.key == K_o:
                    key14 = pygame.draw.rect(screen, WHITE, (579, 150, 40, 230))
                    key26 = pygame.draw.rect(screen, BLACK, (564, 150, 30, 120))
                if event.key == K_i:
                    key15 = pygame.draw.rect(screen, WHITE, (622, 150, 40, 230))
                    key27 = pygame.draw.rect(screen, BLACK, (649, 150, 30, 120))
                if event.key == K_u:
                    key16 = pygame.draw.rect(screen, WHITE, (665, 150, 40, 230))
                    key27 = pygame.draw.rect(screen, BLACK, (649, 150, 30, 120))
        pygame.display.update()

#set background image
filename = 'mainmenu_bg.png'
canvas = Canvas(root, width = 600, height = 500)
canvas.pack()
try:
    tk_img = PhotoImage(file = filename)
    canvas.create_image(110, 250, image = tk_img)
except: pass
#apply hover effects on buttons
Button1 = TK_UI(root, text = "PLAY THE PIANO", font = ('algerian', 20, 'bold', 'underline'),bg = 'blue', foreground = 'red', activebackground = 'gold', highlightbackground = "#bce8f1", highlightthickness = 1, relief = SOLID, borderwidth = "4", command = KeyBoard)
Button1win = canvas.create_window(187, 70, anchor = 'nw', window = Button1)

Button2 = TK_UI(root, text = "ABOUT AND CREDITS",font = ('algerian', 20, 'bold', 'underline'),bg = 'blue', foreground = 'red', activebackground = 'gold',highlightbackground = "#bce8f1", highlightthickness = 1, relief = SOLID, borderwidth = "4", command = ShowAbout)
Button2win = canvas.create_window(160, 185, anchor = 'nw', window = Button2)

Button3 = TK_UI(root, text = "QUIT !",font = ('algerian', 20, 'bold', 'underline'), bg = 'blue', foreground = 'red', activebackground = 'gold', highlightbackground = "#bce8f1", highlightthickness = 1, relief = SOLID, borderwidth = "4", command = quitApplication)
Button3win = canvas.create_window(250, 300, anchor = 'nw', window = Button3)

root.mainloop()
