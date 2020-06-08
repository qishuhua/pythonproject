#! /usr/bin/python
# coding=utf-8
import tkinter

def showlabel():
    global base
    lb=tkinter.Label(base,text='显示label')
    lb.pack()
base=tkinter.Tk()
base.wm_title('label test')
lb1=tkinter.Label(base,text='python label1')
lb1.pack()
btn=tkinter.Button(base,text='show label',command=showlabel)
btn.pack()
base.mainloop()