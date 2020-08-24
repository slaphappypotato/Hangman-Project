from tkinter import *
from tkinter import ttk
import random
from tkinter import messagebox
#WINDOW
window=Tk()
window.title("Hangman")
window.geometry("700x500")
window.resizable(0,0)
window["background"]="#b19cd9"

#CONTENTS
img1=PhotoImage(file="1.png")
#Choosing the word
label1=Label(window,image=img1,borderwidth=0,bg="#b19cd9",fg="#b19cd9")
label1.pack(pady=15)
file1=open("words.txt","r")
words=file1.read()
words=words.split("\n")
length=len(words)
r_int=random.randint(0,length-1)
word=words[r_int].upper()
length=len(word)
#Printing underscores
space="_"
space*=length
space=list(space)
label2=ttk.Label(window,text=space,borderwidth=0,background="#b19cd9",foreground="#ffd700",font=("Karmatic Arcade",35))
label2.pack()
label3=Label(window,text="Enter one letter per guess!",bg="#b19cd9",font=(10))
label3.pack()
#Guess input/entry
var=StringVar()
entry=ttk.Entry(window,width=2,font=("Karmatic Arcade",20),textvariable=var)
entry.pack()
#Wrong guesses label
wrong_guess=6
str_wg=str(wrong_guess)
label4=ttk.Label(window,text="Wrong Guesses left:"+str_wg,background="#b19cd9",font=("Arial",10))
label4.pack(pady=5)
guesses=0
#Command Function
def play():
    global guesses
    global wrong_guess
    global length
    global word
    global var
    global str_wg
    guess=(var.get()).upper()
    guess=guess[0]
    entry.delete(0,"end")
    if guess in word:
        for a in range(0,length):
            if guess==word[a]:
                space[a]=guess
                guesses+=1
    elif guess not in word:
        wrong_guess-=1
        str_wg=str(wrong_guess)
    label2.configure(text=space)
    label4.configure(text="Wrong Guesses left:"+str_wg)
    if wrong_guess<=0 or guesses==length:
        return win()
def win():
    global wrong_guess
    global guesses
    global length
    global word
    if wrong_guess>=1 and guesses==length:
        messagebox.showinfo("Correct","Your guesses were correct!\nYou win!")
    elif wrong_guess==0:
       messagebox.showinfo("Wrong","Your guesses were incorrect!\nYou lose!\nThe word was:"+word)
#Button-In Play
button1=ttk.Button(window,text="Enter Guess!",command=play)
button1.pack(pady=5)

window.mainloop()
