import tkinter as tk
import pygame
from tkinter import ttk, messagebox
from tkinter import *
import random

#MAIN WINDOW
window = tk.Tk()
window.title("Numbo Jumbo")
window.geometry("800x500")
window.resizable(False,False)

# MUSIC
pygame.mixer.init()
pygame.mixer.music.load('Sfx\helltaker.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.3)

# SFX
win_sfx = pygame.mixer.Sound('Sfx\win.mp3')
lose_sfx = pygame.mixer.Sound('Sfx\lose.mp3')

#MUTE BUTTON
btn_mute = tk.PhotoImage(file="Pics\mute.png")
btn_unmute = tk.PhotoImage(file="Pics\play.png")

#PLAY MUSIC UPON OPENING
statusmusic = 0

#MUTE THE MUSIC COMMAND
def musicMute():
    global statusmusic
    if statusmusic == 0:
       pygame.mixer.music.pause()
       btn_mute1.config(image=btn_mute)
       btn_mute2.config(image=btn_mute)
       btn_mute3.config(image=btn_mute)
       btn_mute4.config(image=btn_mute)
       statusmusic = 1
    else:
       pygame.mixer.music.unpause()
       btn_mute1.config(image=btn_unmute)
       btn_mute2.config(image=btn_unmute)
       btn_mute3.config(image=btn_unmute)
       btn_mute4.config(image=btn_unmute)
       statusmusic= 0

#cLICK SFX
def click_sound():
    btn_sfx = pygame.mixer.Sound('Sfx\click.mp3')
    btn_sfx.play()

################################################################

# Frames
Main = tk.Frame(window) #MAIN MENU
Settings = tk.Frame(window) #SETTINGS
GameInterface = tk.Frame(window) #MAIN GAME
Credits = tk.Frame(window) #CREDITS

#DEFAULT SCREEN WHEN OPENING GAME
Main.pack()
Answer = 0
Maxval = 0
Chances = 0

#RESET AFTER A GAME
def clear():
    global Maxval
    global Chances
    global Randomrange
    if Maxval > 0:
        Maxval = 0
        Chances = 0
        Randomrange = 0

    cb_diff.set("")
    lbl_maxval.config(text=f'0:0')
    lbl_chances.config(text=f'0')

#SELECT DIFFICULTY
def difficulty_select():
    global Maxval
    global Chances
    global Randomrange
    choice = str(difficulties.get())
    if choice == '':
        messagebox.showwarning("Oops!", "Please select a difficulty first!")
    elif choice == 'Easy':
        Maxval = 10
        Chances = 3
        lbl_maxval.config(text=f'1:{Maxval}')
        lbl_chances.config(text=f'{Chances}')
        return Chances, Maxval
    elif choice == 'Medium':
        Maxval = 25
        Chances = 5
        lbl_maxval.config(text=f'1:{Maxval}')
        lbl_chances.config(text=f'{Chances}')
        return Chances, Maxval
    elif choice == 'Hard':
        Maxval = 50
        Chances = 8
        lbl_maxval.config(text=f'1:{Maxval}')
        lbl_chances.config(text=f'{Chances}')
        return Chances, Maxval
    elif choice == 'Very Hard':
        Maxval = 100
        Chances = 10
        lbl_maxval.config(text=f'1:{Maxval}')
        lbl_chances.config(text=f'{Chances}')
        return Chances, Maxval
    elif choice == 'Challenge':
        Maxval = 500
        Chances = 12
        lbl_maxval.config(text=f'1:{Maxval}')
        lbl_chances.config(text=f'{Chances}')
        return Chances, Maxval
    elif choice == 'Random':
        Maxval = Randomrange
        Chances = 10
        lbl_maxval.config(text=f'1:{Maxval}')
        lbl_chances.config(text=f'{Chances}')
        return Chances, Maxval, Randomrange

#CREATES RANDOMIZED NUMBER WITHIN RANGE
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

#FORGET CURRENT FRAME AND PACK OTHER FRAME
#FOR SETTINGS
def settings():
    Main.pack_forget()
    Settings.pack()

#fOR MAIN MENU
def home():
    Settings.pack_forget()
    GameInterface.pack_forget()
    Credits.pack_forget()
    Main.pack()

#FOR GAME INTERFACE
def start():
    Main.pack_forget()
    GameInterface.pack()

#FOR CREDITS
def credits():
    Main.pack_forget()
    Credits.pack()

#GUESSING GAME CODE
def GuessGame():
    global Chances
    if Maxval == 0:
        #IF NO DIFFICULTIES ARE SELCTED
        messagebox.showwarning("Oops!", "Please select a difficulty first!")
    else:
        GameInterface.pack()
        Settings.pack_forget()

        lbl_game = ttk.Label(GameInterface, text='Guess the number within the alloted number of chances!', font="Pixeltype 25 bold", background="#f2d649")

        # NUMBER ONLY IN ENTRY
        def validate(attempt):
            return attempt.isdigit()
        valid = GameInterface.register(validate)
 
        # GUESSING
        lbl_guess = ttk.Label(GameInterface, text='Your Guess:', font="Pixeltype 20 bold", background="#f2d649")
        ent_guess = ttk.Entry(GameInterface, validate='key', validatecommand=(valid, '%S'))

        # LISTS FOR LISTBOXES
        greater_guesses = []
        less_guesses = []
 
        # HINT LISTBOXES
        lbl_greaterthan = ttk.Label(GameInterface, text='Greater Than:', font="Pixeltype 15 bold", background="#f2d649")
        lbl_lessthan = ttk.Label(GameInterface, text='Less Than:', font="Pixeltype 15 bold", background="#f2d649")
 
        # GREATER THAN
        greaterthan = tk.Listbox(GameInterface)
        greaterthan.config(background="#F2AE1C", justify='center')
        for item in greater_guesses:
            greaterthan.insert(tk.END, item)
 
        # LESS THAN
        lessthan = tk.Listbox(GameInterface)
        lessthan.config(background="#F2AE1C", justify='center')
        for item in less_guesses:
            lessthan.insert(tk.END, item)
 
        # GUESS BUTTON
        def Guess():
            if ent_guess.get() == "":
                #wITHOUT A GUESS
                messagebox.showwarning("Oops!", "Please enter a value first!")
            else:
                global Chances
                Guess = int(ent_guess.get())
                GuessCount = len(greater_guesses) + len(less_guesses)
                if Guess < Answer:
                    greater_guesses.append(Guess)
                    greaterthan.insert(tk.END, Guess)
                    ent_guess.delete(0, END)
                    Chances -= 1
                    lbl_chances.configure(text=f"Chances left: {Chances}")
                    # LOSE
                    if Chances == 0:
                        pygame.mixer.music.pause()
                        lose_sfx.set_volume(0.9)
                        lose_sfx.play(0)
                        messagebox.showinfo("Oof!",
                                            f"You didn't guess it in the number of attempts given...\n\nBetter luck next time!\n\nThe lucky number is {Answer}!")
                        pygame.mixer.music.unpause()
                        GameInterface.pack_forget()
                        clear()
                        Main.pack()
                elif Guess > Answer:
                    less_guesses.append(Guess)
                    lessthan.insert(tk.END, Guess)
                    ent_guess.delete(0, END)
                    Chances -= 1
                    lbl_chances.configure(text=f"Chances left: {Chances}")
                    # LOSE
                    if Chances == 0:
                        pygame.mixer.music.pause()
                        lose_sfx.set_volume(0.9)
                        lose_sfx.play(0)
                        messagebox.showinfo("Oof!",
                                            f"You didn't guess it in the number of attempts given...\n\nBetter luck next time!\n\nThe lucky number is {Answer}!")
                        pygame.mixer.music.unpause()
                        GameInterface.pack_forget()
                        clear()
                        Main.pack()
                else:
                    # WIN
                    pygame.mixer.music.pause()
                    Final_GuessCount = GuessCount + 1
                    win_sfx.set_volume(0.9) #VICTORY THEME
                    win_sfx.play(0)
                    pygame.mixer.music.pause()
                    messagebox.showinfo("Congratulations!",
                                        f"You got it right!\nThe answer is {Answer}!\nIt only took you {Final_GuessCount} guesses!")
                    pygame.mixer.music.unpause()
                    GameInterface.pack_forget() #RETURN TO MAIN MENU
                    clear()
                    Settings.pack()
                    pygame.mixer.music.unpause()

        #DETAILS/HINTS
        btn_guess = tk.Button(GameInterface, text='Guess', font="Pixeltype 20", background="#F2AE1C", activebackground="#F2AE1C", command=lambda: [Guess(), click_sound()])
        lbl_chances = ttk.Label(GameInterface, text=f"Chances left: {Chances}", font="Pixeltype 20 bold", background="#f2d649")
        lbl_range = tk.Label(GameInterface, text=f'Range of Numbers: 1:{Maxval}', font="Pixeltype 20 bold", background="#f2d649")

        lbl_range.place(x=240, y=130, anchor="center")
        lbl_game.place(x=400, y=80, anchor="center")
        lbl_chances.place(x=560, y=130, anchor="center")

        lbl_guess.place(x=190, y=170, anchor="center")
        ent_guess.place(x=320, y=170, anchor="center")
        btn_guess.place(x=520, y=170, anchor="center")

        lbl_lessthan.place(x=500, y=250, anchor="center")
        lessthan.place(x=500, y=350, anchor="center")
        lbl_greaterthan.place(x=300, y=250, anchor="center")
        greaterthan.place(x=300, y=350, anchor="center")

        btn_quit = tk.Button(GameInterface, text="Quit", font="Pixeltype 20", width=6, background="#F2AE1C", activebackground="#F2AE1C", command=lambda: [home(), clear(), click_sound()])
        btn_quit.place(x=600, y=170, anchor="center")

################################################################

# Background Wallpaper
bg_home = tk.PhotoImage(file="Pics\home.png")
bg_credits = tk.PhotoImage(file="Pics\Credits.png")
bg_settings = tk.PhotoImage(file="Pics\Settings.png")
bg_guess = tk.PhotoImage(file="Pics\Guess.png")

# Canvas for Home Page
canvas = tk.Canvas(Main, width=800, height=500,)
canvas.pack()
canvas.create_image(0, 0, image=bg_home, anchor=NW, )

# Canvas for Select Difficulty
canvas2 = tk.Canvas(Settings, width=800, height=500)
canvas2.pack()
canvas2.create_image(0, 0, image=bg_settings, anchor=NW)

# Canvas for the Actual Guessing Platform
canvas3 = tk.Canvas(GameInterface, width=800, height=500)
canvas3.pack()
canvas3.create_image(0, 0, image=bg_guess, anchor=NW)

# Canvas for Credits
canvas4 = tk.Canvas(Credits, width=800, height=500)
canvas4.pack()
canvas4.create_image(0, 0, image=bg_credits, anchor=NW)

################################################################

# Main Menu
btn_start = tk.Button(Main, text="Start Game", font="Pixeltype 20", background="#F2AE1C", activebackground="#F2AE1C", command=lambda:[click_sound(), settings(), ])
btn_start.place(x=400, y=200, anchor="center")

btn_credits = tk.Button(Main, text="Credits", font="Pixeltype 20", height=1, width=10, background="#F2AE1C", activebackground="#F2AE1C", command=lambda:[click_sound(), credits()])
btn_credits.place(x=400, y=250, anchor="center")

btn_mute1 = tk.Button(Main, image=btn_unmute, background="#F2AE1C", activebackground="#F2AE1C", command=musicMute)
btn_mute1.place(x=400, y=450, anchor="center")

################################################################

# Difficulty Menu
lbl_settings = tk.Label(Settings, text="Set Difficulty", font="Pixeltype 50 bold", background="#fcce4e")
lbl_settings.place(x=410, y=80, anchor="center")

# COMBOBOX OF DIFFICULTIES
difficulties = tk.StringVar()
Settings.option_add('*TCombobox*Listbox.font', 'Pixeltype')
cb_diff = ttk.Combobox(Settings, textvariable=difficulties, font="Pixeltype 20", width = 15)
cb_diff['values'] = ['Easy', 'Medium', 'Hard', 'Very Hard', 'Challenge','Random']
cb_diff['state'] = 'readonly'
cb_diff.set('')
cb_diff.place(x=380, y=150, anchor="center")

#SET DIFFICULTY BUTTON
btn_setdiff = tk.Button(Settings, text='Set', font="Pixeltype 20", background="#F2AE1C", activebackground="#F2AE1C", command=lambda:[randomizer(), difficulty_select(), click_sound()])
btn_setdiff.place(x=490, y=150, anchor="center")

#PLAY BUTTON
btn_play = tk.Button(Settings, text="Play!", font="Pixeltype 20", width=12, background="#F2AE1C", activebackground="#F2AE1C", command=lambda: [click_sound(), GuessGame()])
btn_play.place(x=400, y=220, anchor="center")

#HOME BUTTON
btn_home = tk.Button(Settings, text="Home", font="Pixeltype 20", width=12, background="#F2AE1C", activebackground="#F2AE1C", command=lambda: [click_sound(), home(), clear()])
btn_home.place(x=400, y=270, anchor="center")

# RANGE LABEL
lbl_range = ttk.Label(Settings, text='Range of Numbers:', font="Pixeltype 20", background="#fcce4e")
lbl_range.place(x=320, y=350, anchor="center")

# RANGE VALUES
lbl_maxval = ttk.Label(Settings, text='0:0', font="Pixeltype 20", background="#fcce4e")
lbl_maxval.place(x=480, y=350, anchor="center")

# CHANCES LABEL
lbl_attempts = ttk.Label(Settings, font="Pixeltype 20", text='Number of Attempts:', background="#fcce4e")
lbl_attempts.place(x=320, y=400, anchor="center")

# CHANCES COUNT
lbl_chances = ttk.Label(Settings, font="Pixeltype 20", text='0', background="#fcce4e")
lbl_chances.place(x=480, y=400, anchor="center")

# MUTE BUTTON
btn_mute2 = tk.Button(Settings, image=btn_unmute, background="#F2AE1C", activebackground="#F2AE1C", command=musicMute)
btn_mute2.place(x=600, y=450, anchor="center")

# MUTE BUTTON
btn_mute3 = tk.Button(GameInterface, image=btn_unmute, background="#F2AE1C", activebackground="#F2AE1C", command=musicMute)
btn_mute3.place(x=650, y=410, anchor="center")

################################################################

# Credit Screen
btn_CreditsHome = tk.Button(Credits, text="Home", font="Pixeltype 20", width=12, background="#F2AE1C", activebackground="#F2AE1C", command=lambda: [home(), click_sound()])
btn_CreditsHome.place(x=360, y=400, anchor="center")

# MUTE BUTTON
btn_mute4 = tk.Button(Credits, image=btn_unmute, background="#F2AE1C", activebackground="#F2AE1C", command=musicMute)
btn_mute4.place(x=455, y=400, anchor="center")

# END CODE
window.mainloop()
