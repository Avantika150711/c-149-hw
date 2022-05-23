# -*- coding: utf-8 -*-
"""
Created on Sat May 21 18:15:11 2022

@author: zoya sharma
"""

from tkinter import*
 import random

root=Tk()
root.title("RANDOM WORD GENERATOR")
root.geometry("500x500")
root.configure(background='yellow')

label1=Label(root)

def random_word():
    alpha_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    random1=random.randint(1,26)
    random2=random.randint(1,26)
    random3=random.randint(1,26)
    random4=random.randint(1,26)
    random5=random.randint(1,26)
    
    label1["text"]=random1+random2+random3+random4+random5

btn=Button(root,text="genrator random word",command=random_word,bg="black",fg="white")
btn.place(relx=0.5,rely=0.4,ancher=CENTER)
btn.place(relx=0.5,rely=0.5,ancher=CENTER)
root.mainloop()
