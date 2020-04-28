# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter.ttk import *
from tkinter import ttk
from Tl_class_frame import *
import os
import time
from tkinter.filedialog import askopenfilename
from pic9 import *
from PIL import Image, ImageTk

class PiMain(object):
    #设计UI 界面
    def setupUI(self):
        v = View(self.root, kind='日', orient=tk.VERTICAL)
        v.v1['width'] = 120

        # #增加按钮,用来 OS
        vButton = tk.Button(v.v1,text='待扩展1',width=11)
        vButton.place(anchor=tk.W,relx=0.1,rely=0.2)

        vButton = tk.Button(v.v1, text='待扩展2', width=11)
        vButton.place(anchor=tk.W, relx=0.1, rely=0.3)

        vButton = tk.Button(v.v1, text='待扩展3', width=11)
        vButton.place(anchor=tk.W, relx=0.1, rely=0.4)

        v_right = View(v.v2, bg='blue',kind='日', orient=tk.HORIZONTAL)
        v_right.v1['height'] = 100

        # #增加Label,用来
        tk.Label(v_right.v1,text='图片文件路径:').pack(side=tk.LEFT)
        self.file1=tk.StringVar()        
        tk.Entry(v_right.v1,width=50,textvariable=self.file1).pack(side=tk.LEFT)
        vButton = tk.Button(v_right.v1, text='...', width=3,command=self.getfile)
        vButton.pack(side=tk.LEFT)
        vButton = tk.Button(v_right.v1, text='分割成九宫格', width=20,command=self.split_pic)
        vButton.pack(side=tk.LEFT)
        vButton = tk.Button(v_right.v1, text='Show', width=10,command=self.show_pic)
        vButton.pack(side=tk.LEFT)
        
        width1=150
        height1=150
        img = Image.open('21.gif')  # 打开图片
        img_png2 = ImageTk.PhotoImage(image=img)   
        # img_png2 = tk.PhotoImage(file='22.GIF')
        button_img2 = tk.Button(v_right.v2, text="WIFI", image=img_png2,width=width1,height=height1)
        button_img2.pack()

        # img = Image.open('E:/py_proj/xiaohong02/21.gif')  # 打开图片
        # img_png1 = ImageTk.PhotoImage(image=img)        
        # label_img1 = tk.Label(v_right.v2, image = img_png1)
        # # label_img1 = tk.Label(v_right.v2, text='sssssss')
        # # label_img1.pack()
        # label_img1.grid(row=0,column=0,padx=5, pady=5)

        # label_img1 = tk.Label(v_right.v2, text='sssssss')
        # label_img1.pack()
        # img_png2 = tk.PhotoImage(file='21.GIF')
        # label_img2 = tk.Label(v_right.v2,text="WIFI", image = img_png2)
        # label_img2.pack()

        # img_png3 = tk.PhotoImage(file = 'E:/py_proj/xiaohong02/3.png')
        # label_img3 = tk.Label(v_right.v2, image = img_png3)
        # label_img3.grid(row=0,column=2,padx=5, pady=5)

    def split_pic(self):
        yy=self.file1.get()
        print(yy)
        Start_split(yy)
    
    def show_pic(self):
        print('xx')

    def getfile(self):
        xx = tk.filedialog.askopenfilename()
        self.file1.set(xx)

    def setCenter(self,root, w, h):
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = int((ws / 2) - (w / 2))
        y = int((hs / 2) - (h / 2))
        root.geometry('{}x{}+{}+{}'.format(w, h, x, y))

    #类的运行主体
    def __init__(self):
        self.root = tk.Tk()
        self.root.title(string='图片分割成九宫格')
        self.setCenter(self.root, 700, 300)
        self.setupUI()
        self.root.mainloop()

if __name__=='__main__':
    PiMain()
