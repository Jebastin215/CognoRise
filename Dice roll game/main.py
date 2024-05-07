import tkinter as tk
from PIL import Image,ImageTk
import random

window=tk.Tk()
window.geometry("650x500")
window.title("Dice Game")



dice=["1.png","2.png","3.png","4.png","5.png","6.png"]
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1=tk.Label(window,image=image1)
label2=tk.Label(window,image=image2)

label1.image=image1
label2.image=image2

label1.place(x=40,y=100)
label2.place(x=350,y=100)

def dice_roll():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image=image1)
    label1.image = image1  

    image2=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image=image2)
    label2.image=image2



button=tk.Button(window,text="Roll",fg="red",font="Times 20 bold",command=dice_roll)
button.place(x=290,y=400)
window.mainloop()