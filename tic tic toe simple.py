#############
#Tic-Tac-Toe#
#############


import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("+600+200")


# variables for buttons
var1 = tk.StringVar()
var1.set("-")

var2 = tk.StringVar()
var2.set("-")

var3 = tk.StringVar()
var3.set("-")

var4 = tk.StringVar()
var4.set("-")

var5 = tk.StringVar()
var5.set("-")

var6 = tk.StringVar()
var6.set("-")

var7 = tk.StringVar()
var7.set("-")

var8 = tk.StringVar()
var8.set("-")

var9 = tk.StringVar()
var9.set("-")

var = tk.StringVar()
var.set("-")

count = 0

play_turn = tk.StringVar()
play_turn.set("Player 1's turn")


# graphics for buttons (row, column)    
button_00 = tk.Button(root, width = 10, height = 10, textvariable = var1, command = lambda: click(var1))
button_01 = tk.Button(root, width = 10, height = 10, textvariable = var2, command = lambda: click(var2))
button_02 = tk.Button(root, width = 10, height = 10, textvariable = var3, command = lambda: click(var3))
button_10 = tk.Button(root, width = 10, height = 10, textvariable = var4, command = lambda: click(var4))
button_11 = tk.Button(root, width = 10, height = 10, textvariable = var5, command = lambda: click(var5))
button_12 = tk.Button(root, width = 10, height = 10, textvariable = var6, command = lambda: click(var6))
button_20 = tk.Button(root, width = 10, height = 10, textvariable = var7, command = lambda: click(var7))
button_21 = tk.Button(root, width = 10, height = 10, textvariable = var8, command = lambda: click(var8))
button_22 = tk.Button(root, width = 10, height = 10, textvariable = var9, command = lambda: click(var9))

button_00.grid(row = 0, column = 0)
button_01.grid(row = 0, column = 1)
button_02.grid(row = 0, column = 2)
button_10.grid(row = 1, column = 0)
button_11.grid(row = 1, column = 1)
button_12.grid(row = 1, column = 2)
button_20.grid(row = 2, column = 0)
button_21.grid(row = 2, column = 1)
button_22.grid(row = 2, column = 2)


# checks vertically, horizontally, and diagonally for win
def check_win():
    # if player 1 wins ask to play again
    if (button_00["text"] == "X" and button_01["text"] == "X" and button_02["text"] == "X" or
        button_10["text"] == "X" and button_11["text"] == "X" and button_12["text"] == "X" or
        button_20["text"] == "X" and button_21["text"] == "X" and button_22["text"] == "X" or
        button_00["text"] == "X" and button_11["text"] == "X" and button_22["text"] == "X" or
        button_20["text"] == "X" and button_11["text"] == "X" and button_02["text"] == "X" or
        button_00["text"] == "X" and button_10["text"] == "X" and button_20["text"] == "X" or
        button_01["text"] == "X" and button_11["text"] == "X" and button_21["text"] == "X" or
        button_02["text"] == "X" and button_12["text"] == "X" and button_22["text"] == "X"):

        response = messagebox.askquestion("Winner", "X Wins!\nPlay Again?")

        if response == "no":
            root.destroy()

        # resets board if the user wants to play again
        elif response =="yes":
            global count
            
            turn.config(bg = "lightblue")
            play_turn.set("Player 1's turn")
            count = 0
            
            var1.set("-")
            var2.set("-")
            var3.set("-")
            var4.set("-")
            var5.set("-")
            var6.set("-")
            var7.set("-")
            var8.set("-")
            var9.set("-")

    # if player 2 wins ask to play again
    elif(button_00["text"] == "O" and button_01["text"] == "O" and button_02["text"] == "O" or
         button_10["text"] == "O" and button_11["text"] == "O" and button_12["text"] == "O" or
         button_20["text"] == "O" and button_21["text"] == "O" and button_22["text"] == "O" or
         button_00["text"] == "O" and button_11["text"] == "O" and button_22["text"] == "O" or
         button_20["text"] == "O" and button_11["text"] == "O" and button_02["text"] == "O" or
         button_00["text"] == "O" and button_10["text"] == "O" and button_20["text"] == "O" or
         button_01["text"] == "O" and button_11["text"] == "O" and button_21["text"] == "O" or
         button_02["text"] == "O" and button_12["text"] == "O" and button_22["text"] == "O"):

        response = messagebox.askquestion("Winner", "O Wins!\nPlay Again?")

        if response == "no":
            root.destroy()

        # resets board if user wants to play again
        elif response =="yes":
            turn.config(bg = "lightblue", text = "Player 1's turn")
            play_turn.set("Player 1's turn")
            count = 0
            
            var1.set("-")
            var2.set("-")
            var3.set("-")
            var4.set("-")
            var5.set("-")
            var6.set("-")
            var7.set("-")
            var8.set("-")
            var9.set("-")

    # if it's a tie ask to playa gain
    elif count == 8:
        response = messagebox.askquestion("Winner", "Match ends in a draw!\nPlay Again?")

        if response == "no":
            root.destroy()

        # resets board if user wants to play again
        elif response =="yes":
            turn.config(bg = "lightblue")
            play_turn.set("Player 1's turn")
            count = 0
            
            var1.set("-")
            var2.set("-")
            var3.set("-")
            var4.set("-")
            var5.set("-")
            var6.set("-")
            var7.set("-")
            var8.set("-")
            var9.set("-")


# main game loop when each button is clicked
def click(var):
    global count
    
    if count % 2 == 0 and var.get() == "-":
        var.set("X")
        count += 1
        player_turn("p2")
        check_win()
    
    elif count % 2 ==1 and var.get() == "-":
        var.set("O")
        count += 1
        player_turn("p1")
        check_win()

# sets turn label with appropriate text and color depending on who's turn it is
def player_turn(player):
    
    if player == "p1":
        play_turn.set("Player 1's turn")
        turn.config(bg = "lightblue")
    
    elif player == "p2":
        play_turn.set("Player 2's turn")
        turn.config(bg = "orange")
    
# turn label graphics
turn = tk.Label(root, textvariable = play_turn, bg = "lightblue", padx = 82)
turn.grid(row = 4, column = 0, columnspan = 3)

root.mainloop()