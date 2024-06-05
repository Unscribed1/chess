from tkinter import *

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
    def __init__(self, x, y, team, ttype):
        self.pathlist= []
        self.ogpiece = True
        self.firstmove = 1
        self.x = x
        self.y = y
        self.team = team
        self.ttype = ttype
        self.form = True

class coordinates():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class path_box():
    def __init__(self,x,y):
        self.pathimg = PhotoImage(file="pathway.png")
        self.x = x
        self.y = y
        self.form = canvas.create_image(x,y,image=self.pathimg)

class selector():
    def __init__(self,x,y):
        self.selector = PhotoImage(file="selector.png")
        self.waiter = PhotoImage(file="selector2.png")
        self.current_player = "white"
        self.waiting_player = "black"
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

def piece_initialiser(obj):
    if obj.team == "black":
        if obj.ttype == "pawn":
            obj.ogpiece = PhotoImage(file="black_pawn.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
        if obj.ttype == "rook":
            obj.ogpiece = PhotoImage(file="thex.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
    if obj.team == "white":
        if obj.ttype == "pawn":
            obj.ogpiece = PhotoImage(file="white_pawn.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
        if obj.ttype == "rook":
            obj.ogpiece = PhotoImage(file="thex.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
            
def mover(sele, x, y): # moves the selector
    canvas.move(sele.form, x, y)
    sele.x += x
    sele.y += y
    if sele.x not in range (0,400) or sele.y not in range(0,400):
        canvas.moveto(sele.form, 0, 0)
        sele.x = 25
        sele.y = 25

def fetcher(sele): # selects a piece
    pathway_cleaner()
    for i in range(0,len(piecelist)):
        if sele.x == piecelist[i].x and sele.y == piecelist[i].y:
            if sele.current_player == piecelist[i].team:
                print("got here")
                pathways(piecelist[i])
                xf = piecelist[i].x
                yf = piecelist[i].y
                sele.selectee = piecelist[i]
                print(xf, ",", yf,"Fetched")
                print(sele.selectee)
                canvas.moveto(flash_obj.form, xf-25, yf-25)

def pitcher(selectee,pathlist): # Sends the piece to the desired location
    occupied_by_friendly = False
    occupied_by_enemy = False
    matchfound = 0
    for i in range(0,len(piecelist)):
        if sele.x == piecelist[i].x and sele.y == piecelist[i].y:
            if selectee.team == piecelist[i].team:
                occupied_by_friendly = True
                print("Square occupied by friendly")
            if selectee.team != piecelist[i].team:
                print("Square occupied by enemy team")
                occupied_by_enemy = True
                enemy = piecelist[i]
    
    if occupied_by_friendly == False :
        for i in range(0,len(pathlist)):
            print(sele.x)
            print(sele.y)
            print(pathlist[i].x)
            print(pathlist[i].y)
            print("newloop")
            if sele.x == pathlist_used[i].x and sele.y == pathlist_used[i].y:
                matchfound = 1
                obj = selectee
                obj.x = sele.x
                obj.y = sele.y
                obj.firstmove = 2
                canvas.moveto(obj.form, obj.x-25, obj.y-25)
                canvas.moveto(flash_obj.form, -100, -100)
                canvas.delete(sele.form)
                sele.current_player, sele.waiting_player = sele.waiting_player, sele.current_player
                sele.selector, sele.waiter = sele.waiter, sele.selector
                sele.form = canvas.create_image(sele.x,sele.y, image=sele.selector)
                break
        pathway_cleaner()

    if occupied_by_enemy == True and matchfound == 1:
        enemy.x = -100
        enemy.y = -100
        canvas.moveto(enemy.form, -100,-100)

pathlist_used = []
pathlist = [path_box(-100,-100) for i in range(20)]

def pathway_cleaner(): # organizes the path lists
    x = 0
    print("\n",len(pathlist_used),pathlist_used,"\n")
    while len(pathlist_used) > 0:
        print(pathlist_used[0], "ELEMENT")
        pathlist_used[0].x = -100
        pathlist_used[0].y = -100
        canvas.moveto(pathlist_used[0].form, -100, -100)
        pathlist.append(pathlist_used[0])
        pathlist_used.pop(0)
        x += 1
        print("USED PATH MOVED TO PATHLIST")

##def direction_checker_front(obj):
##    if obj.team == "black":
##        z = 100
##    else:
##        z = 0
####    forward_x = obj.x ## We're working with the y dimension here, x not needed
##    forward_y = obj.y-50+z
##    for i in range(0,len(piecelist)):
##        if piecelist[i].x == obj.x and forward_y == piecelist[i].y:
##            print("SPACE OCCUPIED")
##            return 1
##            break
##    else:
##        return 0

def crossref(ylist, xpos):
    pass

def direction_checker_north(obj):
    northlist = []
    for i in range(obj.y-50,-25,-50):
        a = coordinates(obj.x, i)
        northlist.append(a)
    return northlist

def direction_checker_south(obj):
    southlist = []
    for i in range(obj.y+50,375,50):
        pass
    return southlist
        

def pathways_checker_pawn(obj):
    x = obj.x
    y = obj.y
    if obj.team == "white":
        northlist = direction_checker_north(obj)
        if northlist[0] == False:
            pathlist_used.append(pathlist[0])
            pathlist.pop(0)
            canvas.moveto(pathlist_used[0].form, x-25,y-75)
            pathlist_used[0].x = x
            pathlist_used[0].y = y-50
            print("PATH APPENDED TO PATHLIST_USED")
            if obj.firstmove == 1 and northlist[1] == False:
                pathlist_used.append(pathlist[1])
                pathlist.pop(1)
                canvas.moveto(pathlist_used[1].form, x-25,y-125)
                pathlist_used[1].x = x
                pathlist_used[1].y = y-100
                print("PATH APPENDED TO PATHLIST_USED")
    if obj.team == "black":
        pathlist_used.append(pathlist[0])
        pathlist.pop(0)
        canvas.moveto(pathlist_used[0].form, x-25,y+25)
        pathlist_used[0].x = x
        pathlist_used[0].y = y+50
        if obj.firstmove == 1:
            pathlist_used.append(pathlist[1])
            pathlist.pop(1)
            canvas.moveto(pathlist_used[1].form, x-25,y+75)
            pathlist_used[1].x = x
            pathlist_used[1].y = y+100
    if obj.team == "black":
        z = 100
    else:
        z = 0
    upper_x = [x-50, x+50]
    upper_y = y-50+z
    print("loop should start here")
    for i in range(0,len(piecelist)): # DIAGONALS
        if (piecelist[i].x in upper_x) and upper_y == piecelist[i].y:
             if obj.team != piecelist[i].team:
                 print("ENEMY FOUND")
                 newpath = pathlist[0]
                 pathlist_used.append(newpath)
                 pathlist.pop(0)
                 canvas.moveto(newpath.form, piecelist[i].x-25, piecelist[i].y-25)
                 newpath.x = piecelist[i].x
                 newpath.y = piecelist[i].y
    

def pathways(obj):
    x = obj.x
    y = obj.y
    if obj.ttype == "pawn":
        pathways_checker_pawn(obj)

piecelist = []

piece1 = piece(25,75,"black", "pawn")
piece2 = piece(75,75,"black", "pawn")
piece3 = piece(125,75,"black", "pawn")
piece4 = piece(175,75,"black", "pawn")
piece5 = piece(225,75,"black", "pawn")
piece6 = piece(275,75,"black", "pawn")
piece7 = piece(325,75,"black", "pawn")
piece8 = piece(375,75,"black", "pawn")

piece9 = piece(25,325,"white", "pawn")
piece10 = piece(75,325,"white", "pawn")
piece11 = piece(125,325,"white", "pawn")
piece12 = piece(175,325,"white", "pawn")
piece13 = piece(225,325,"white", "pawn")
piece14 = piece(275,325,"white", "pawn")
piece15 = piece(325,325,"white", "pawn")
piece16 = piece(375,325,"white", "pawn")

piece17 = piece(25,375,"white","rook")

sele = selector(25,25)
flash_obj = flashbox(-100,-100)

piecelist.append(piece1)
piecelist.append(piece2)
piecelist.append(piece3)
piecelist.append(piece4)
piecelist.append(piece5)
piecelist.append(piece6)
piecelist.append(piece7)
piecelist.append(piece8)

piecelist.append(piece9)
piecelist.append(piece10)
piecelist.append(piece11)
piecelist.append(piece12)
piecelist.append(piece13)
piecelist.append(piece14)
piecelist.append(piece15)
piecelist.append(piece16)
piecelist.append(piece17)

board.bind("<Right>", lambda x: mover(sele, x=50, y=0))
board.bind("<Left>", lambda x: mover(sele, x=-50, y=0))
board.bind("<Up>", lambda x: mover(sele, x=0, y=-50))
board.bind("<Down>", lambda x: mover(sele, x=0, y=50))
board.bind("x", lambda x: fetcher(sele))
board.bind("d", lambda x: pitcher(sele.selectee,pathlist))

#Places the graphical representation of the pieces on the board
for i in range(0,len(piecelist)):
    piece_initialiser(piecelist[i])
    
board.mainloop()