from tkinter import *
import random

window = Tk()

window.title("Lucky Friend Wheel")
window.geometry("500x500")
window.config(background="light blue")

friends_list = ["Dev", "lavish","Tushar", "Khyati", "shital", "Rishit", "Bhavesh", "Anhad", "Aryan", "Ayush","Arjav"]

def lucky_friends():
    x = random.randint(0,10)
    print("You lucky friend is :"+ friends_list[x])




btn = Button(window ,text = "Who is your lucky friend" , command=lucky_friends)
btn.place(relx = 0.5, rely = 0.5 , anchor= CENTER)
window.mainloop()
