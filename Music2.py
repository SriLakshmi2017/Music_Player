import tkinter as tk
import fnmatch
import os 
import pygame
from pygame import mixer
from tkinter import *

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
canvas.config(bg='black')

rootpath = "C:\\CodeClause\Playlist"
pattern = "*.mp3"

mixer.init()

main_img = tk.PhotoImage(file ="enjoying-music-music.gif")
prev_img = tk.PhotoImage(file="prev_img.png")
stop_img = tk.PhotoImage(file="stop_img.png")
play_img = tk.PhotoImage(file="play_img.png")
pause_img =tk.PhotoImage(file="pause_img.png")
next_img = tk.PhotoImage(file="next_img.png")

def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0,'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


def pause_song():
    if pauseButton["text"]=="pause":
        mixer.music.pause()
        pauseButton["text"] = "play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"



listBox = tk.Listbox(canvas,fg="cyan",bg="black",width = 100,font = ('poppins',14))  
listBox.pack(padx = 15, pady = 15)

label = tk.Label(canvas,text= '',bg = 'black', fg ='yellow',font = ('poppins', 18))
label.pack(pady = 15)

top = tk.Frame(canvas,bg="black")
top.pack(padx =10,pady =5,anchor = 'center')

# top = tk.Frame(canvas,bg="black")
# top.pack(padx =10,pady =5)

# mainButton = tk.Button(canvas,text = "prev",image= main_img,bg="black",borderwidth=0,command = play_prev)
# mainButton.pack(pady = 10,in_ = top,side = 'left')
 

prevButton = tk.Button(canvas,text = "prev",image= prev_img,bg="black",borderwidth=0,command = play_prev)
prevButton.pack(pady = 15,in_ = top,side = 'left')

StopButton = tk.Button(canvas,text = "Stop",image= stop_img,bg="black",borderwidth=0,command = stop)
StopButton.pack(pady = 15,in_ = top,side = 'left')

playButton = tk.Button(canvas,text = "play",image= play_img,bg="black",borderwidth=0 , command = select)
playButton.pack(pady = 15,in_ = top,side = 'left')

pauseButton = tk.Button(canvas,text = "pause",image= pause_img,bg="black",borderwidth=0,command = pause_song)
pauseButton.pack(pady = 15,in_ = top,side = 'left')

nextButton = tk.Button(canvas,text = "next",image= next_img,bg="black",borderwidth=0,command = play_next)
nextButton.pack(pady = 15,in_ = top,side = 'left')


for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end',filename)
     


canvas.mainloop()
