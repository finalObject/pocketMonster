#-*-coding:utf-8-*-
import os,sys
from PIL import Image,ImageTk
import hashlib
import Tkinter as tk
os.chdir(os.path.split(os.path.abspath(sys.argv[0]))[0])
root=tk.Tk()
im=Image.open(r'.\ERR\err.jpg')
im=im.resize((376,250))
for x in range(1,4):
    
    #这一段代码放在循环之外和放在循环之内的区别#################
    photo=ImageTk.PhotoImage(im)
    im.close()
    ############################################################
    
    locals()['x'+str(x)]=tk.LabelFrame(root).grid(row=x,column=0)
    tk.Label(locals()['x'+str(x)],image=photo).grid(row=x,column=0)
root.mainloop()
