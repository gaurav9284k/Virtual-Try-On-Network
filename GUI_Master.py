# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 15:23:32 2024

@author: admin
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
# import cv2
import sqlite3
import os
# import numpy as np
import time

'''import detection_emotion_practice as validate'''
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="#D15FEE")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Text To Image")


#loading the images
# img=ImageTk.PhotoImage(Image.open("1.png"))

# img2=ImageTk.PhotoImage(Image.open("2.jpg"))

# img3=ImageTk.PhotoImage(Image.open("2.jpg"))


# logo_label=tk.Label()
# logo_label.place(x=0,y=0)

# x=1

image2 = Image.open('2.jpg')
image2 = image2.resize((w,h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)

label_l1 = tk.Label(root, text="Virtual Try on Cloth  ",font=("Times New Roman", 35, 'bold'),
                    background="#eaf2f8", fg="black", width=70, height=2)
label_l1.place(x=0, y=0)
# function to change to next image
# def move():
#     global x
#     if x == 4:
#             x = 1
#     if x == 1:
#         logo_label.config(image=img)
#     elif x == 2:
#         logo_label.config(image=img2)
#     elif x == 3:
#         logo_label.config(image=img3)
#     x = x+1
#     root.after(2000, move)
 
# # calling the function
# move()
canvas=tk.Canvas(root,background="#3D59AB",borderwidth=5)
canvas.place(x=510,y=230,width=440,height=400)
import webbrowser
def open_google():
    webbrowser.open("https://colab.research.google.com/drive/16AWMZAp6bWM5ZstrfZ9bZZuGZhAxdFwg")
label = tk.Label(canvas, text="button", fg="blue", font=('times', 15, ' bold '), bg='pink' ,width=20 ,height=2 )
label.place(x=100,y=250 )
   
    # Bind the label to the function that opens Google when clicked
label.bind("<Button-1>", lambda e: open_google())
 
image2 = Image.open('2.jpg')
image2 = image2.resize((250,200), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(canvas, image=background_image)

background_label.image = background_image

background_label.place(x=100, y=0)  # , relwidth=1, relheight=1)




#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def shift():
#     x1,y1,x2,y2 = canvas.bbox("marquee")
#     if(x2<0 or y1<0): #reset the coordinates
#         x1 = canvas.winfo_width()
#         y1 = canvas.winfo_height()//2
#         canvas.coords("marquee",x1,y1)
#     else:
#         canvas.move("marquee", -2, 0)
#     canvas.after(1000//fps,shift)

# canvas=tk.Canvas(root,bg="green")
# canvas.pack()
# canvas.place(x=0, y=0)
# text_var="Text To Image"
# text=canvas.create_text(0,-2000,text=text_var,font=('Raleway',25,'bold'),fill='black',tags=("marquee",),anchor='w')
# x1,y1,x2,y2 = canvas.bbox("marquee")
# width = 1600
# height = 80
# canvas['width']=width
# canvas['height']=height
# fps=40    #Change the fps to make the animation faster/slower
# shift()   #Function Calling

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


#iframesrc = ("https://assets.pinterest.com/ext/embed.html?id=578853358377785481", height="1167", width="600" , frameborder="0", scrolling="no" )





# def cap_video():
   
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])


   
def window():
  root.destroy()




root.mainloop()