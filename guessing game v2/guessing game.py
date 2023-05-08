import tkinter as tk
import pygame
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import random


window = tk.Tk()
window.title("Guessing Game")
window.geometry("800x500")
window.resizable(False,False)

#Music
pygame.mixer.init()
pygame.mixer.music.load('vitality.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

muteButton = tk.PhotoImage(file="mute.png")
playButton = tk.PhotoImage(file="play.png")

status = 0
def musicMute():
    global status
    if status==0:
       pygame.mixer.music.pause()
       buttonMute.config(image=muteButton)
       buttonMute2.config(image=muteButton)
       buttonMute3.config(image=muteButton)
       buttonMute4.config(image=muteButton)
       status = 1
    else:
       pygame.mixer.music.unpause()
       buttonMute.config(image=playButton)
       buttonMute2.config(image=playButton)
       buttonMute3.config(image=playButton)
       buttonMute4.config(image=playButton)
       status= 0

def click_sound():
    sfx_button = pygame.mixer.Sound('click.mp3')
    sfx_button.play()
################################################################

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)

frame1.pack()
Answer = 0
Maxval = 0
Chances = 0


def clear():
    global Maxval
    global Chances
    global Randomrange
    if Maxval > 0:
        Maxval = 0
        Chances = 0
        Randomrange = 0

    cb_diff.set("")
    lbl_details2.config(text=f'0:0')
    lbl_details4.config(text=f'0')


def DifficultySelect():
    global Maxval
    global Chances
    global Randomrange
    choice = str(difficulties.get())
    if choice == '':
        messagebox.showwarning("Oops!", "Please select a difficulty first!")
    elif choice == 'Easy':
        Maxval = 10
        Chances = 3
        lbl_details2.config(text=f'1:{Maxval}')
        lbl_details4.config(text=f'{Chances}')
        return Chances, Maxval
    elif choice == 'Medium':
        Maxval = 25
        Chances = 5
        lbl_details2.config(text=f'1:{Maxval}')
        lbl_details4.config(text=f'{Chances}')
        return Chances, Maxval
    elif choice == 'Hard':
        Maxval = 50
        Chances = 8
        lbl_details2.config(text=f'1:{Maxval}')
        lbl_details4.config(text=f'{Chances}')
        return Chances, Maxval
    elif choice == 'Very Hard':
        Maxval = 100
        Chances = 10
        lbl_details2.config(text=f'1:{Maxval}')
        lbl_details4.config(text=f'{Chances}')
        return Chances, Maxval
    elif choice == 'Challenge':
        Maxval = 500
        Chances = 12
        lbl_details2.config(text=f'1:{Maxval}')
        lbl_details4.config(text=f'{Chances}')
        return Chances, Maxval
    elif choice == 'Random':
        Maxval = Randomrange
        Chances = 10
        lbl_details2.config(text=f'1:{Maxval}')
        lbl_details4.config(text=f'{Chances}')
        return Chances, Maxval, Randomrange


def randomizer():
    global Answer
    global Randomrange
    choice = str(difficulties.get())
    if choice == 'Easy':
        Answer = random.randint(1, 10)
        return Answer
    elif choice == 'Medium':
        Answer = random.randint(1, 25)
        return Answer
    elif choice == 'Hard':
        Answer = random.randint(1, 50)
        return Answer
    elif choice == 'Very Hard':
        Answer = random.randint(1, 100)
        return Answer
    elif choice == 'Challenge':
        Answer = random.randint(1, 500)
        return Answer
    elif choice == 'Random':
        Randomrange = random.randint(1, random.randint(1, 10000))
        Answer = random.randint(1, Randomrange)
        return Answer
print(Answer)



def settings():
    frame1.pack_forget()
    frame2.pack()

def home():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame1.pack()

def start():
    frame1.pack_forget()
    frame3.pack()

def credits():
    frame1.pack_forget()
    frame4.pack()


def GuessGame():
    if Maxval == 0:
        messagebox.showwarning("Oops!", "Please select a difficulty first!")
    else:
        print(Answer)
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
                                    f"You didn't guess it in the number of attempts given...\n\nBetter luck next time!\n\nThe lucky number is {Answer}!")
                GameInterface.pack_forget()
                clear()
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
                clear()
                frame2.pack()

        btn_guess = tk.Button(frame3, text='Guess',font="Pixeltype 20", command=lambda: [Guess(), click_sound()])

        lbl_game.place(x=400, y=80, anchor="center")

        lbl_guess.place(x=150, y=150, anchor="center")
        ent_guess.place(x=300, y=150, anchor="center")
        btn_guess.place(x=300, y=200, anchor="center")

        lbl_lessthan.place(x=500, y=250, anchor="center")
        lessthan.place(x=500, y=350, anchor="center")
        lbl_greaterthan.place(x=300, y=250, anchor="center")
        greaterthan.place(x=300, y=350, anchor="center")

        buttonQuit = tk.Button(frame3, text="Quit", font="Pixeltype 20", command=lambda: [home(), clear(), click_sound()])
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
#####

canvas4 = tk.Canvas(frame4, width=800, height=500)
canvas4.pack()

canvas4.create_image(0,0, image=bgFlappy, anchor=NW)

test_lbl4 = tk.Label(canvas4, image=bgFlappy2)
test_lbl4.place()
################################################################

#MAIN MENU
labelHome = tk.Label(frame1, text="Guessing Game", font="Pixeltype 80 bold", background="#0099CC")
labelHome.place(x=400, y=100, anchor="center")

buttonStart = tk.Button(frame1, text="Start Game",font="Pixeltype 20",command=lambda:[click_sound(),settings(),])
buttonStart.place(x=400, y=200, anchor="center")

buttonCredits = tk.Button(frame1, text="Credits",font="Pixeltype 20", height=1, width=10, command=lambda:[click_sound(),credits()])
buttonCredits.place(x=400, y=250, anchor="center")

buttonMute = tk.Button(frame1,image=playButton, command=musicMute)
buttonMute.place(x=650, y=450, anchor="center")

################################################################

#DIFFICULTY MENU
labelSettings = tk.Label(frame2, text="Set Difficulty", font="Pixeltype 50 bold", background="#73E0FF")
labelSettings.place(x=410, y=80, anchor="center")

labelDifficulty = tk.Label(frame2, text="Select your Difficulty:", font="Pixeltype 20", background="#73E0FF")
labelDifficulty.place(x=300, y=150, anchor="center")

difficulties = tk.StringVar()
frame2.option_add('*TCombobox*Listbox.font', 'Pixeltype')
cb_diff = ttk.Combobox(frame2, textvariable=difficulties, font="Pixeltype 20", width = 15)
cb_diff['values'] = ['Easy', 'Medium', 'Hard', 'Very Hard', 'Challenge','Random']
cb_diff['state'] = 'readonly'
cb_diff.set('')
cb_diff.place(x=480, y=150, anchor="center")

btn_setdiff = tk.Button(frame2, text='Set Difficulty!',font="Pixeltype 20", command=lambda:[randomizer(),DifficultySelect(),click_sound()])
btn_setdiff.place(x=450, y=200, anchor="center")

buttonPlay = tk.Button(frame2, text="Play!", font="Pixeltype 20",width=12,command=lambda: [click_sound(), GuessGame()])
buttonPlay.place(x=450, y=250, anchor="center")

buttonHome = tk.Button(frame2, text="Home",font="Pixeltype 20",width=12 ,command=lambda: [click_sound(), home(), clear()])
buttonHome.place(x=450, y=300, anchor="center")

lbl_details = tk.Label(frame2, text='Range of Numbers:', font="Pixeltype 20")
lbl_details.place(x=320, y=350, anchor="center")

lbl_details2 = tk.Label(frame2, text='0:0',font="Pixeltype 20")
lbl_details2.place(x=480, y=350, anchor="center")

lbl_details3 = tk.Label(frame2, font="Pixeltype 20",text='Number of Attempts:')
lbl_details3.place(x=320, y=400, anchor="center")

lbl_details4 = tk.Label(frame2, font="Pixeltype 20",text='0')
lbl_details4.place(x=480, y=400, anchor="center")

buttonMute2 = tk.Button(frame2,image=playButton, command=musicMute)
buttonMute2.place(x=650, y=450, anchor="center")

buttonMute3 = tk.Button(frame3,image=playButton, command=musicMute)
buttonMute3.place(x=650, y=410, anchor="center")
################################################################

#Creditscreen
labelCredits = tk.Label(frame4, text="Credits", font="Pixeltype 80 bold", background="#0099CC")
labelCredits.place(x=400, y=100, anchor="center")

buttonCreditsHome = tk.Button(frame4, text="Home",font="Pixeltype 20",width=12 ,command=lambda: [home(),click_sound()])
buttonCreditsHome.place(x=400, y=400, anchor="center")

buttonMute4 = tk.Button(frame4,image=playButton, command=musicMute)
buttonMute4.place(x=400, y=450, anchor="center")

window.mainloop()
