# !/usr/bin/python
import configparser
from struct import pack
from tkinter import *
from tkinter import ttk
import os


window = Tk()
window.geometry("800x580")
window.title('Ir8 Logiciel')

div1 =  Frame(window,background="grey",height=50,width=213).grid(column=3,row=1)
div2 =  Frame(window,background="black",height=225,width=213).grid(column=3,row=3)
div3 =  Frame(window,background="black",height=245,width=213).grid(column=3,row=5)


box1 = Frame(window,width=150,height=150,bg="#BAB4B4")
titreBox = Label(box1,text='Nouvelle Comande',highlightbackground = "#BAB4B4",bg='#BAB4B4')
btnBox = Button(text = "+",fg='black',highlightbackground = "#BAB4B4",width=8,height=4,bg="#A59999")
btnBox.place(x=273,y=63)
box1.place(x=250,y=25)
titreBox.place(x=300,y=100)

div_1_text1 = Label(div1,text= "Crée un nouveau Clients" ,bg="grey",width=23).grid(column=3,row=0)
div_2_text1 = Label(div2,text= "Clients Récents" ,bg="black",width=23,fg="white").grid(column=3,row=2)
div_2_text1 = Label(div2,text= "Commandes Récentes" ,bg="black",width=23,fg="white").grid(column=3,row=4)

a_input1 = Entry(div1,width=12,highlightbackground = "grey")
a_input1.config(bg='white')
a_input1.place(x=15,y=28)

def newCli():
    res = a_input1.get()
    config = configparser.ConfigParser()
    config[res] = {'name': res,'status':'1','number':'1'}
    with open('configFils.ini', 'w') as configfile:
        config.write(configfile)

btn1 = Button(window,text = "+",width=2,highlightbackground = "grey",command=newCli())
btn1.place(x=150,y=28)

window.mainloop()




