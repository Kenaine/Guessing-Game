import tkinter as tk
import pygame
import tkinter.font as font
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox 
import random


window = tk.Tk()
window.title("Guessing Game")
window.geometry("800x500")
window.resizable(False,False)

#Retro Font
myFont = font.Font(family="Pixeltype")

#Music
pygame.mixer.init()
pygame.mixer.music.load('vitality.mp3')
pygame.mixer.music.play(-1)

def musicMute():
   statusMusic = mutevar.get()
   print(statusMusic)
   if statusMusic ==1:
       pygame.mixer.music.pause()
       buttonMute.config(text="Unmute")
   else:
       pygame.mixer.music.unpause()
       buttonMute.config(text="Mute")
################################################################

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)


Answer = 0
Maxval = 0
Chances = 0

def DifficultySelect():
    global Answer
    global Maxval
    global Chances
    choice = str(difficulties.get())
    if choice == '':
        messagebox.showwarning("Oops!", "Please select a difficulty first!")
    elif choice == 'Easy':
        Answer = random.randint(1, 10)
        Maxval = 10
        Chances = 3
        lbl_details2.config(text=f'1:{Maxval}')
        lbl_details4.config(text=f'{Chances}')
        return Answer, Chances, Maxval
    elif choice == 'Medium':
        Answer = random.randint(1, 25)
        Maxval = 25
        Chances = 5
        lbl_details2.config(text=f'1:{Maxval}')
        lbl_details4.config(text=f'{Chances}')
        return Answer, Chances, Maxval
    elif choice == 'Hard':
        Answer = random.randint(1, 50)
        Maxval = 50
        Chances = 8
        lbl_details2.config(text=f'1:{Maxval}')
        lbl_details4.config(text=f'{Chances}')
        return Answer, Chances, Maxval
    elif choice == 'Very Hard':
        Answer = random.randint(1, 100)
        Maxval = 100
        Chances = 10
        lbl_details2.config(text=f'1:{Maxval}')
        lbl_details4.config(text=f'{Chances}')
        return Answer, Chances, Maxval
    elif choice == 'Challenge':
        Answer = random.randint(1, 500)
        Maxval = 500
        Chances = 12
        lbl_details2.config(text=f'1:{Maxval}')
        lbl_details4.config(text=f'{Chances}')
        return Answer, Chances, Maxval
    elif choice == 'Random':
        Randomrange = random.randint(1, random.randint(1,10000))
        Answer = random.randint(1, Randomrange)
        Maxval = Randomrange
        Chances = 10
        lbl_details2.config(text=f'1:{Maxval}')
        lbl_details4.config(text=f'{Chances}')
        return Answer, Chances, Maxval

    else:
        pass

frame1.pack()

def settings():
    frame1.pack_forget()
    frame2.pack()

def home():
    frame2.pack_forget()
    frame3.pack_forget()
    frame1.pack()


def start():
    frame1.pack_forget()
    frame3.pack()

def forget_diff():
    cb_diff.set('')

def GuessGame():
    if Answer == 0:
        messagebox.showwarning("Oops!", "Please select a difficulty first!")
        frame3.pack_forget()
        frame2.pack()
    else:
        frame3.pack()
        frame2.pack_forget()
        GameInterface =frame3

        lbl_game = ttk.Label(GameInterface, text='Guess the number within the alloted number of chances!', font="Pixeltype 20 bold", background="white")

        # number only in entry
        def validate(attempt):
            return attempt.isdigit()

        valid = GameInterface.register(validate)

        # Guessing
        lbl_guess = ttk.Label(frame3, text='Your Guess:', font="Pixeltype 15 bold", background="white")
        ent_guess = ttk.Entry(frame3, validate='key', validatecommand=(valid, '%S'))
        ent_guess['font']= myFont

        greaterguesses = []
        lessguesses = []

        # Hint Listboxes
        lbl_greaterthan = ttk.Label(frame3, text='Greater Than:', font="Pixeltype 12 bold", background="white")
        lbl_lessthan = ttk.Label(frame3, text='Less Than:', font="Pixeltype 12 bold", background="white")

        # greater than
        greaterthan = tk.Listbox(frame3)
        for item in greaterguesses:
            greaterthan.insert(tk.END, item)

        # less than
        lessthan = tk.Listbox(frame3)
        for item in lessguesses:
            lessthan.insert(tk.END, item)

        # Guess Button
        def Guess():
            Guess = int(ent_guess.get())
            GuessCount = len(greaterguesses) + len(lessguesses)
            if GuessCount == (Chances - 1) and Guess != Answer:
                messagebox.showinfo("Oof!",
                                    f"You didn't guess it in the number of attempts given...\nDo better next time!")
                GameInterface.pack_forget()
                frame1.pack()
            elif Guess < Answer:
                greaterguesses.append(Guess)
                greaterthan.insert(tk.END, Guess)
                ent_guess.delete(0, END)
            elif Guess > Answer:
                lessguesses.append(Guess)
                lessthan.insert(tk.END, Guess)
                ent_guess.delete(0, END)
            else:
                FinalGuessCount = GuessCount + 1
                messagebox.showinfo("Congratulations!",
                                    f"You got it right!\nThe answer is {Answer}!\nIt only took you {FinalGuessCount} guesses!")
                GameInterface.pack_forget()
                frame2.pack()

        btn_guess = tk.Button(frame3, text='Guess', command=Guess)
        btn_guess['font'] = myFont

        lbl_game.place(x=400, y=80, anchor="center")

        lbl_guess.place(x=150, y=150, anchor="center")
        ent_guess.place(x=300, y=150, anchor="center")
        btn_guess.place(x=300, y=200, anchor="center")

        lbl_lessthan.place(x=500, y=250, anchor="center")
        lessthan.place(x=500, y=350, anchor="center")
        lbl_greaterthan.place(x=300, y=250, anchor="center")
        greaterthan.place(x=300, y=350, anchor="center")

        buttonQuit = tk.Button(frame3, text="Quit", command=home)
        buttonQuit['font']= myFont
        buttonQuit.place(x=400, y=200, anchor="center")


#BACKGROUND STUFF
bgFlappy = tk.PhotoImage(file="flappy.png")

canvas = tk.Canvas(frame1, width=800, height=500)
canvas.pack()

canvas.create_image(0,0, image=bgFlappy, anchor=NW)

test_lbl = tk.Label(canvas, image=bgFlappy)
test_lbl.place()

#####
bgFlappy2 = tk.PhotoImage(file="flappy2.png")

canvas2 = tk.Canvas(frame2, width=800, height=500)
canvas2.pack()

canvas2.create_image(0,0, image=bgFlappy2, anchor=NW)

test_lbl2 = tk.Label(canvas2, image=bgFlappy2)
test_lbl2.place()

#####
bgBoard = tk.PhotoImage(file="Board.png")

canvas3 = tk.Canvas(frame3, width=800, height=500)
canvas3.pack()

canvas3.create_image(0,0, image=bgBoard, anchor=NW)

test_lbl3 = tk.Label(canvas3, image=bgBoard)
test_lbl3.place()

################################################################

#MAIN MENU
labelHome = tk.Label(frame1, text="Guessing Game", font="Pixeltype 80 bold", background="#0099CC")
labelHome.place(x=400, y=100, anchor="center")

buttonStart = tk.Button(frame1, text="Start Game", command=settings)
buttonStart['font'] = myFont
buttonStart.place(x=400, y=200, anchor="center")

buttonSettings = tk.Button(frame1, text="Help")
buttonSettings['font'] = myFont
buttonSettings.place(x=400, y=250, anchor="center")

buttonCredits = tk.Button(frame1, text="Credits")
buttonCredits['font'] = myFont
buttonCredits.place(x=400, y=300, anchor="center")

mutevar = tk.IntVar()
buttonMute = tk.Checkbutton(frame1, text="Mute",variable=mutevar, command=musicMute, onvalue=1, offvalue=0)
buttonMute['font'] = myFont
buttonMute.place(x=650, y=450, anchor="center")

################################################################

#DIFFICULTY MENU
labelSettings = tk.Label(frame2, text="Set Difficulty", font="Pixeltype 80 bold", background="#73E0FF")
labelSettings.place(x=470, y=80, anchor="center")

labelDifficulty = tk.Label(frame2, text="Select your Difficulty:", font=myFont, background="#73E0FF")
labelDifficulty.place(x=310, y=150, anchor="center")

difficulties = tk.StringVar()
cb_diff = ttk.Combobox(frame2, textvariable=difficulties)
cb_diff['values'] = ['Easy', 'Medium', 'Hard', 'Very Hard', 'Challenge','Random']
cb_diff['state'] = 'readonly'
cb_diff.set('')
cb_diff['font'] = myFont
cb_diff.place(x=480, y=150, anchor="center")

btn_setdiff = tk.Button(frame2, text='Set Difficulty!', command=DifficultySelect)
btn_setdiff['font'] = myFont
btn_setdiff.place(x=450, y=200, anchor="center")

buttonHome = tk.Button(frame2, text="Play!", command=lambda:[GuessGame(),forget_diff()])
buttonHome['font'] = myFont
buttonHome.place(x=450, y=250, anchor="center")


buttonHome = tk.Button(frame2, text="Home", command=home)
buttonHome['font'] = myFont
buttonHome.place(x=450, y=300, anchor="center")

lbl_details = tk.Label(frame2, text='Range of Numbers:', font=myFont)
lbl_details.place(x=320, y=350, anchor="center")

lbl_details2 = tk.Label(frame2, text='0:0',font=myFont)
lbl_details2.place(x=480, y=350, anchor="center")

lbl_details3 = tk.Label(frame2, font=myFont,text='Number of Attempts:')
lbl_details3.place(x=320, y=400, anchor="center")

lbl_details4 = tk.Label(frame2, font=myFont,text='0')
lbl_details4.place(x=480, y=400, anchor="center")
################################################################
window.mainloop()
