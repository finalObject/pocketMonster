from tkinter import *
from PIL import ImageTk,Image
tk =Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack();
rawTree= Image.open('33.png');

img3 = ImageTk.PhotoImage(rawTree)
canvas.create_image(100,100,anchor=NW,image=img3)
