from tkinter import *
from PIL import Image, ImageTk
from random import randint

root = Tk()
root.geometry("1500x800")
root.title("Rock, Paper, Scissors Game")
root.configure(background="yellow")

rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

user_label = Label(root, image=scissors_img, bg="green")
comp_label = Label(root, image=scissors_img_comp, bg="green")
comp_label.grid(row=2, column=0)
user_label.grid(row=2, column=5)

playerScore = Label(root, text=0, font=100, bg="black", fg="white")
computerScore = Label(root, text=0, font=100, bg="black", fg="white")
computerScore.grid(row=2, column=1)
playerScore.grid(row=2, column=3)

# indicators
user_indicator = Label(root, font=70, bg="red", fg="white", text="USER").grid(row=0, column=3)
comp_indicator = Label(root, font=70, bg="red", fg="white", text="COMPUTER").grid(row=0, column=1)

# message
msg_label = Label(root, font=50, bg="red", fg="white")
msg_label.grid(row=5, column=2)

def updateMessage(x):
    msg_label.config(text=x)

def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

def checkWin(player, computer):
    if player == computer:
        updateMessage("It's a tie!!!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        updateMessage("You Win!!")
        updateUserScore()
    else:
        updateMessage("You Loose")
        updateCompScore()

choices = ["rock", "paper", "scissors"]

def updateChoice(x):
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.config(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.config(image=paper_img_comp)
    else:
        comp_label.config(image=scissors_img_comp)

    if x == "rock":
        user_label.config(image=rock_img)
    elif x == "paper":
        user_label.config(image=paper_img)
    else:
        user_label.config(image=scissors_img)
    checkWin(x, compChoice)

rock = Button(root, width=10, height=3, font="7", text="Rock", bg="#808080", fg="white", command=lambda: updateChoice("rock")).grid(row=7, column=1)
paper = Button(root, width=10, height=3, font="7", text="Paper", bg="#00FF00", fg="white", command=lambda: updateChoice("paper")).grid(row=7, column=2)
scissors = Button(root, width=10, height=3, font="7", text="Scissors", bg="#800000", fg="white", command=lambda: updateChoice("scissors")).grid(row=7, column=3)

root.mainloop()