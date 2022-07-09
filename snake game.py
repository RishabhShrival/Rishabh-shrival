# -*- coding: utf-8 -*-
"""
Created on Wed May  4 22:29:03 2022

@author: Rishabh
"""

from turtle import Turtle,bye,listen,up,setpos,write,mainloop,getscreen,onkey
from random import randrange
from tkinter import Tk,Button


def go():
    global c
    c=-10
    s.clear()
    print('start')
    parent.destroy()
    s.bgcolor('skyblue')
      
    p=Turtle()
    p.up()
    p.shape('square')
    p.color('green')
    p.setpos(-500,-300)
    p.down()
    p.pensize(30)


    k=Turtle()
    k.shape('triangle')
    k.up()
    k.color('red')

    def tar():
        k.setpos(0,0)
        x=randrange(-200,200)
        y=randrange(-200,200)
        k.setpos(x,y)
        t.clear()

    def b():
        t.write('score :',True,font=('Arial',20))
        t.write(c,False,font=('Arial',30))


    t=Turtle()
    t.shape('square')
    t.color('blue')
    t.up()

    def r():
        t.right(90)
    def l():
        t.left(90)
    def q():
        bye()
    
            
    listen()
    onkey(r,'Left')
    onkey(l,'Right')
    onkey(q,'Escape')
    

    while True:
        if t.xcor()//25==k.xcor()//25 and t.ycor()//25==k.ycor()//25:
            tar()
            c+=10
        else:
            t.fd(speed)
            
        if p.xcor()==500:
            b()
            up()
            setpos(-500,300)
            write('do you want play again?',font=('Arial',20))
            playg()
            
            
        else:
            p.fd(2)
            

s=getscreen()
s.setup(1.0,1.0)

def mode():
    global mod
    mod=Tk()
    easy=Button(mod,text='easy',fg='yellow',command=easyf)
    medium=Button(mod,text='medium',fg='orange',command=mediumf)
    hard=Button(mod,text='hard',fg='red',command=hardf)
    easy.pack(side='top')
    medium.pack()
    hard.pack(side='bottom')
def easyf():
    global speed
    speed=5
    mod.destroy()
    playg()
def mediumf():
    global speed
    speed=10
    mod.destroy()
    playg()
def hardf():
    global speed
    speed=15
    mod.destroy()
    playg()

    
def playg():
    global parent
    parent=Tk()
    play=Button(parent,text='play',fg='red',command=go)
    play.pack(side='top')
    mainloop()
    
mode()
