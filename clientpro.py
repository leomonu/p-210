#-----------Bolierplate Code Start -----
from cgitb import text
from distutils.command.upload import upload
from fileinput import filename
from msilib.schema import ListBox
import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from turtle import title
import os
import time
import playsound
from playsound import playsound
import pygame
from pygame import mixer

name=None
listBox=None
textArea=None
labelChat=None
textMsg=None
filePathLabel = None

global song_counter
song_counter=0

# for file in os.listdir('shared_files'):
#     filename=os.fsdecode(file)
#     listBox.insert(song_counter,filename)
#     song_counter=song_counter+1


def musicWindow():

    global name
    global listBox
    global textArea
    global labelChat
    global textMsg
    global filePathLabel
    global infolabel

    

    window=Tk()
    window.title("Music")
    window.geometry("500x350")

    selectlabel = Label(window,text="select song",bg="LightSkyBlue",font=("Calibri",8))
    selectlabel.place(x=2,y=1)

    listbox = Listbox(window,height=10,width=39,activestyle='dotbox',bg="LightSkyBlue",borderwidth=2,font=("Calibri",10))
    listbox.place(x=10,y=18)

    scrollbar1=Scrollbar(listbox)
    scrollbar1.place(relheight=1,relx=1)
    scrollbar1.config(command=listbox.yview)

    PlayButton=Button(window,text="Play",width=10,bd=1,bg='SkyBlue',font=("Calibri",10),command=play)
    PlayButton.place(x=30,y=200)

    stop=Button(window,text="stop",bd=1,width=10,bg='SkyBlue',font=("Calibri",10),command=Stop)
    stop.place(x=200,y=200)

    ResumeButton=Button(window,text="Resume",width=10,bd=1,bg='SkyBlue',font=('Calibri',10),command=resume)
    ResumeButton.place(x=30,y=250)

    PauseButton=Button(window,text="Pause",width=10,bd=1,bg='SkyBlue',font=('Calibri',10),command=pause)
    PauseButton.place(x=30,y=250)

    upload=Button(window,text="Upload",width=10,bd=1,bg="SkyBlue",font=("Calibri",8))
    upload.place(x=200,y=250)

    download=Button(window,text="Download",width=10,bd=1,bg="SkyBlue",font=("Calibri",8))
    download.place(x=200,y=250)

    infolabel = Label(window,text="",bg="blue",font=("Calibri",8))
    infolabel.place(x=6,y=280)


    window.resizable(True,True)

    window.mainloop()


PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096



def play():
    global song_selected
    global infolabel
    song_selected=listBox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infolabel.configure(text="NOW PLAYING: "+song_selected)
    else:
        infolabel.configure(text="")
    
def Stop():
    global song_selected
    pygame
    mixer.int()
    mixer.music.load('shared_flies/' +song_selected)
    mixer.music.pause()
    infolabel.configure(text="")

def resume():
    global song_selected
    mixer.init()
    mixer.music.load('shared_files/'+song_selected)
    mixer.music.play()

def pause():
    global song_selected
    pygame
    mixer.init()
    mixer.music.load('shared_flies/'+song_selected)
    mixer.music.pause()



def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()
setup()


#-----------Bolierplate Code Start -----