# Python project on rock paper scissors
import random
# we have to import some packages to perform this program

import tkinter as tk

root = tk.Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('DataFlare_Rock,Paper,Scissors')
root.config(bg='seashell3')
# Tk() use to initialized Tkinter to create window
# geometry() sets the window width and height
# resizable(0,0) by this command we can fix the size of the window
# title() used to set the title of the window
# bg = ‘’ use to set the color of the background

label = tk.Label(root, text='Rock, Paper, Scissors', font='arial 20 bold', bg='seashell2')  # Removed .pack()
label.pack()

user_Input = tk.StringVar()
tk.Label(root, text='choose any one:-Rock,Paper,Scissors', font='arial 20 bold', bg='seashell2').place(x=20, y=70)
user_entry = tk.Entry(root, font='arial 15 ', textvariable=user_Input, bg='antiquewhite2')
user_entry.place(x=90, y=130)  # Removed duplicate .place() call

comp_pick = random.choice(['rock', 'paper', 'scissors'])  # Used random.choice()

Result = tk.StringVar()  # Renamed from tk.Result to Result
def play():
    user_input = user_Input.get()  # Renamed from tk.user_take to user_Input
    if user_input == comp_pick:
        Result.set('Tie,You both selected the same')
    elif user_input == 'rock' and  comp_pick == 'Paper':
        Result.set('You loose, computer selected paper')
    elif user_input == 'paper' and comp_pick == 'rock':
        Result.set('You win, computer selected rock')
    elif user_input == 'scissors' and comp_pick == 'paper':
        Result.set('You win, computer selected paper')
    elif user_input == 'paper' and comp_pick == 'scissors':
        Result.set('you loose, computer selected scissors')
    elif user_input == 'scissors' and comp_pick == 'rock':
        Result.set('you losse, computer selected rock')
    elif user_input == 'rock' and comp_pick == 'scissors':
        Result.set('you win, computer selected scissors')
    else:
        Result.set('invalid:- choose any one -- rock,paper,scissors')


def reset():  # Renamed from tk.Reset to reset
    Result.set(" ")
    user_Input.set(" ")

def exit_game():  # Renamed from Exit to exit_game
    root.destroy()

result_label = tk.Label(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50)
result_label.place(x=25, y=250)
play_button = tk.Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='seashell4', command=play)
play_button.place(x=150, y=190)
reset_button = tk.Button(root, font='arial 13 bold', text='RESET', padx=5, bg='seashell4', command=reset)
reset_button.place(x=70, y=310)
exit_button = tk.Button(root, font='arial 13 bold', text='EXIT', padx=5, bg='seashell4', command=exit_game)
exit_button.place(x=230, y=310)

# Button() widget used when we want to display a button.
# command called the specific function when the button will be clicked.
# root.mainloop() method executes when we run our program.

root.mainloop()
