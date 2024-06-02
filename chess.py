
# First attempt at making a chess board. I have avoided tutorials that explicitly
# show you how to make a chess board, and instead opted for basic tutorials that didn't
# spoonfeed outright. However alot of this was concepts I knew off the top of my head
# Came up with the loop to draw the board on my own - it wasn't rocket science.

# The main purpose here was to achieve functionality, so I'd imagine that the
# code is spaghetti (I wouldn't know any better at this point), and could still learn more
# on how to organize it properly. I am not happy with the board.bind part of the
# code where lambda is being used, as I don't fully grasp it as a concept yet (this is
# the only thing I essentially copypasted off some forum)

# I will revisit this project and rewrite it as I expand on my knowledge.

from tkinter import *

piecelist = []

board = Tk()
board.geometry("400x400")

canvas = Canvas(board, bg = 'white', width = 400, height = 400)
canvas.pack()


for x in range(0,500,100): # Loop to create the chess board.
    for y in range(0,400,50):
        if y % 100 == 0:
            z = x + 50
        else:
            z = x
        canvas.create_rectangle((z,y,z+50,y+50), fill="navy", width = 0)
        canvas.create_rectangle((z-50,y,z,y+50), fill="grey", width = 0)

# Good find: If you display an image inside a function, then make sure to keep the reference to the image object in your Python program, either by storing it in a global variable or by attaching it to another object.
class piece():
    def __init__(self, x, y):
        self.ogpiece = PhotoImage(file='thex.png')
        self.x = x
        self.y = y 
        self.form = canvas.create_image(x,y, image=self.ogpiece)

class selector():
    def __init__(self,x,y):
        self.selector = PhotoImage(file="selector.png")
        self.x = x
        self.y = y
        self.selectee = True
        self.form = canvas.create_image(x,y, image=self.selector)

class flashbox():
    def __init__(self, x, y):
        self.flasher = PhotoImage(file="flash.png")
        self.x = x
        self.y = y
        self.form = canvas.create_image(x,y,image=self.flasher)

board.bind("<Right>", lambda x: mover(sele, x=50, y=0))
board.bind("<Left>", lambda x: mover(sele, x=-50, y=0))
board.bind("<Up>", lambda x: mover(sele, x=0, y=-50))
board.bind("<Down>", lambda x: mover(sele, x=0, y=50))
board.bind("x", lambda x: fetcher(sele))
board.bind("d", lambda x: pitcher(sele.selectee))

def mover(sele, x, y): # moves the selector
    canvas.move(sele.form, x, y)
    sele.x += x
    sele.y += y
    if sele.x not in range (0,400) or sele.y not in range(0,400):
        canvas.moveto(sele.form, 0, 0)
        sele.x = 25
        sele.y = 25

def fetcher(sele): # selects a peice
    for i in range(0,len(piecelist)):
        if sele.x == piecelist[i].x and sele.y == piecelist[i].y:
            xf = piecelist[i].x
            yf = piecelist[i].y
            sele.selectee = piecelist[i]
            print(xf, ",", yf,"Fetched")
            print(sele.selectee)
            canvas.moveto(flash_obj.form, xf-25, yf-25)

##def pitcher(selectee):
##    obj = selectee
##    obj.x = sele.x
##    obj.y = sele.y
##    canvas.moveto(obj.form, obj.x-25, obj.y-25)
##    canvas.moveto(flash_obj.form, -100, -100)

def pitcher(selectee): # Sends the piece to the desired location
    for i in range(0,len(piecelist)):
        if selectee.x == piecelist[i].x and selectee.y == piecelist[i].y:
            print("Busy")
            break
    obj = selectee
    obj.x = sele.x
    obj.y = sele.y
    canvas.moveto(obj.form, obj.x-25, obj.y-25)
    canvas.moveto(flash_obj.form, -100, -100)
    sele.selectee = True


piece1 = piece(25,25)
piece2 = piece(75,25)
piece3 = piece(125,25)
piece4 = piece(175,25)
piece5 = piece(225,25)
sele = selector(25,25)
flash_obj = flashbox(-100,-100)

piecelist.append(piece1)
piecelist.append(piece2)
piecelist.append(piece3)
piecelist.append(piece4)
piecelist.append(piece5)

##board.bind("<Right>", move_right(sele,selector))
##board.bind("<Left>", move_left)
##board.bind("<Up>", move_up)
##board.bind("<Down>", move_down)

board.mainloop()
