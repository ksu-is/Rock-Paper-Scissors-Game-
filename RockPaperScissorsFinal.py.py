from tkinter import *
from tkinter import messagebox
import sys, random
import tkinter.messagebox

rps = ['rock', 'paper', 'scissors']
res = 'PLAY'

root = Tk()
root.geometry('800x400')
root.title('ROCK-PAPER-SCISSORS GAME')

frame_text = Frame(root)    
frame_text.place(width=250, height=100, x=260, y=300)

text = Label(frame_text, text=res, fg='red', font=('Times New Roman', 40))
text.pack()

def instructions ():
   tkinter.messagebox.askokcancel('Instructions', '''HOW TO PLAY ROCK PAPER SCISSORS

    START by clicking one of the buttons, EITHER 'Rock", 'Paper', OR 'Scissors'
    You will be playing against a computer that will be choosing against you randomly.

    RULES OF THE GAME:
    -----------------
    - ROCK WINS AGAINST SCISSORS
    - SCISSORS WINS AGAINST PAPER
    - PAPER WINS AGAINST ROCK''')

def close():
    root.destroy()
    sys.exit()

menu = Menu()
menu.add_command(label='Instructions', command=instructions)
menu.add_separator()
menu.add_command(label='Quit', command=close)

filemenu = Menu(menu, tearoff=0)
filemenu.add_command(label='Hello')
filemenu.add_command(label='Nice Game')
menu.add_cascade(label='Options',menu=filemenu)

root.configure(menu=menu) #maybe messup

def res_text(res):
    text.config(text=res)

def play_rock(Event):
    x = random.choice(rps)
    if x=='rock':
        res = 'TIE'
        res_text(res)
    elif x=='paper':
        res = 'LOSE'
        res_text(res)
    elif x=='scissors':
        res = 'WIN'
        res_text(res)

def play_paper(Event):
    x = random.choice(rps)
    if x=='rock':
        res = 'TIE'
        res_text(res)
    elif x=='paper':
        res = 'LOSE'
        res_text(res)
    elif x=='scissors':
        res = 'WIN'
        res_text(res)

def play_scissors(Event):
    x = random.choice(rps)
    if x=='rock':
        res = 'TIE'
        res_text(res)
    elif x=='paper':
        res = 'LOSE'
        res_text(res)
    elif x=='scissors':
        res = 'WIN'
        res_text(res)

start_text = Label(root, text='Choose Rock, Paper, or Scissors', font=('Times New Roman', 20))
start_text.pack()

rock_button = Button(root, text='Rock', width=10)
rock_button.bind('<Button-1>', play_rock)
rock_button.place(x=250, y=100)

paper_button = Button(root, text='Paper', width=10)
paper_button.bind('<Button-1>', play_paper)
paper_button.place(x=350, y=100)

scissors_button = Button(root, text='Scissors', width=10)
scissors_button.bind('<Button-1>', play_scissors)
scissors_button.place(x=450, y=100)


root.mainloop()
