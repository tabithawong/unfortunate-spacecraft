###################################
# Title: "Space BONK!"            #
# Programmer: Tabitha Wong        #
# Last modified:  March 27, 2019  #
# P.S. I know things don't "fall" #
# like that in space, but use     #
# your imagination please!        #
###################################

from tkinter import *
from random import *
from time import *
myInterface = Tk()
screen = Canvas(myInterface, width=800, height=800, background="black")
screen.pack()

#STARS
for hi in range(500):
    r = randint(1,3)
    rx1 = randint(1,800)
    ry1 = randint(1,800)
    rx2 = rx1 + r
    ry2 = ry1 + r
    screen.create_oval (rx1,ry1, rx2, ry2, fill = "white", outline = "white")

#MOON
screen.create_oval(550,250,850,550, fill = "grey55", outline = "grey25", width = 5)
screen.create_oval(725,300,775,350, outline = "grey25", width = 3)
screen.create_oval(590,350,690,450, outline = "grey25", width = 3)
screen.create_oval(625,300,650,325, outline = "grey25", width = 3)
screen.create_oval(700,475,760,535, outline = "grey25", width = 3)

#ROCKET AND ANIMATION

#initial values
x1 = -100
xNose = 87
y1 = 288
xSpeed = 8

#animation loop
for f in range(150):
    w1 = screen.create_polygon(x1,y1,x1+12,y1-13,x1+37,y1+12,x1+24,y1+25, fill = "red")
    w2 = screen.create_polygon(x1,y1+100,x1+24,y1+75,x1+37,y1+87,x1+12,y1+112, fill = "red")
    w3 = screen.create_polygon(x1-24,y1-13,x1+12,y1-13,x1,y1,fill = "red")
    w4 = screen.create_polygon(x1-24,y1+112,x1,y1+100,x1+12,y1+112, fill = "red")
    thicc = screen.create_oval(x1,y1+2,xNose,y1+97, fill = "white")
    w5 = screen.create_oval(x1+102,y1+26,x1+149,y1+73, fill = "red")
    w6 = screen.create_oval(x1+112,y1+36,x1+139,y1+63, fill = "black")
    w7 = screen.create_rectangle(x1-24,y1+37,x1+37,y1+62, fill = "red")

    screen.update()
    sleep(0.03)
    screen.delete(w1,w2,w3,w4,thicc,w5,w6,w7)
    
    x1 = x1 + xSpeed
    xNose = x1 + 187

    if xNose >= 555:
        x1 = 368
        xNose = 555
        y1 = y1 + 20
        screen.create_text(400,150, text = "UH OH!", fill = "red", font = "fixedsys 75")

    else:
        y1 = 288
        
