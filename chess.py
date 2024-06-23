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
        self.team = "na"
        self.put = "na"
        
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
        
        ############ RECURSIONS
# def tri_recursion(k):
  # if(k>0):
    # result = k+tri_recursion(k-1)
    # print(result)
  # else:
    # result = 0
  # return result
def north_recursion(obj, arg, list):
    print("north recursion")
    arg -= 1
    obj.y -= 50
    for i in range(len(piecelist)):
        if (obj.x and obj.y) == (piecelist[i].x and piecelist[i].y)
    coords = coordinates(a,b)
    list.append(coords)
    if arg != 0:
        recursion(obj.x, obj.y, arg, list)
    else:
        return   


def piece_initialiser(obj):
    if obj.team == "black":
        if obj.ttype == "pawn":
            obj.ogpiece = PhotoImage(file="black_pawn.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
        if obj.ttype == "rook":
            obj.ogpiece = PhotoImage(file="black_rook.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
        if obj.ttype == "bishop":
            obj.ogpiece = PhotoImage(file="black_bishop.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
        if obj.ttype == "queen":
            obj.ogpiece = PhotoImage(file="black_queen.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
        if obj.ttype == "knight":
            obj.ogpiece = PhotoImage(file="black_knight.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
        if obj.ttype == "king":
            obj.ogpiece = PhotoImage(file="black_king.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
    if obj.team == "white":
        if obj.ttype == "pawn":
            obj.ogpiece = PhotoImage(file="white_pawn.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
        if obj.ttype == "rook":
            obj.ogpiece = PhotoImage(file="white_rook.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
        if obj.ttype == "bishop":
            obj.ogpiece = PhotoImage(file="white_bishop.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
        if obj.ttype == "queen":
            obj.ogpiece = PhotoImage(file="white_queen.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
        if obj.ttype == "knight":
            obj.ogpiece = PhotoImage(file="white_knight.png")
            obj.form = canvas.create_image(obj.x,obj.y, image=obj.ogpiece)
        if obj.ttype == "king":
            obj.ogpiece = PhotoImage(file="white_king.png")
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
    for i in range(0,len(piecelist)):
        if sele.x == piecelist[i].x and sele.y == piecelist[i].y:
            if sele.current_player == piecelist[i].team:
                pathways(piecelist[i])
                xf = piecelist[i].x
                yf = piecelist[i].y
                sele.selectee = piecelist[i]
                canvas.moveto(flash_obj.form, xf-25, yf-25)

# There's an error when I press D outside of the paths. I've lingered too much on how to fix it,
# and since it doesn't seem to affect functionality, I'll leave it for later.

def pitcher(selectee,pathlist): # Sends the piece to the desired location
    occupied_by_friendly = False
    occupied_by_enemy = False
    occupied_by_king = False
    matchfound = 0
    for i in range(0,len(piecelist)):
        if sele.x == piecelist[i].x and sele.y == piecelist[i].y:
            if selectee.team == piecelist[i].team:
                occupied_by_friendly = True
            if selectee.team != piecelist[i].team:
                occupied_by_enemy = True
                if piecelist[i].ttype == "king":
                    occupied_by_king = True
                    
                enemy = piecelist[i]
    
    if occupied_by_friendly == False :
        for i in range(0,len(pathlist_used)):
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
        if occupied_by_king == True:
            print("GAME OVER")

pathlist_used = []
pathlist = [path_box(-100,-100) for i in range(50)]
    

def pathways(obj):
    plist = []
    if obj.ttype == "pawn":
        if obj.team == "white":
            north_recursion(obj, plist)
    if obj.ttype == "rook":
        pathways_checker_rook(obj)
    if obj.ttype == "bishop":
        pathways_checker_bishop(obj)
    if obj.ttype == "queen":
        pathways_checker_bishop(obj)
        pathways_checker_rook(obj)
    if obj.ttype == "knight":
        pathways_checker_knight(obj)
    if obj.ttype == "king":
        pathways_checker_king(obj)

piecelist = []

piece1 = piece(25,75,"black", "pawn")
piece2 = piece(75,75,"black", "pawn")
piece3 = piece(125,75,"black", "pawn")
piece4 = piece(175,75,"black", "pawn")
piece5 = piece(225,75,"black", "pawn")
piece6 = piece(275,75,"black", "pawn")
piece7 = piece(325,75,"black", "pawn")
piece8 = piece(375,75,"black", "pawn")

piece10 = piece(75,325,"white", "pawn")
piece11 = piece(125,325,"white", "pawn")
piece12 = piece(175,325,"white", "pawn")
piece13 = piece(225,325,"white", "pawn")
piece14 = piece(275,325,"white", "pawn")
piece15 = piece(325,325,"white", "pawn")
piece16 = piece(375,325,"white", "pawn")
piece23 = piece(25,325,"white", "pawn")

piece17 = piece(25,375,"white","rook")
piece18 = piece(375,375,"white", "rook")

piece19 = piece(25,25,"black", "rook")
piece20 = piece(375,25,"black", "rook")
piece24 = piece(125, 25,"black", "bishop")
piece25 = piece(275, 25,"black", "bishop")


piece21 = piece(125,375,"white", "bishop")
piece22 = piece(275,375,"white", "bishop")
piece26 = piece(175,375,"white", "queen")
piece27 = piece(175,25,"black", "queen")
piece28 = piece(75,375,"white", "knight")
piece29 = piece(225,375,"white","king")
piece30 = piece(225,25,"black","king")
piece31 = piece(325,375,"white","knight")
piece32 = piece(75,25,"black","knight")
piece33 = piece(325,25,"black","knight")
piecelist.append(piece33)
piecelist.append(piece32)
piecelist.append(piece31)
piecelist.append(piece21)
piecelist.append(piece22)
piecelist.append(piece24)
piecelist.append(piece25)
piecelist.append(piece23)
piecelist.append(piece26)
piecelist.append(piece27)
piecelist.append(piece28)
piecelist.append(piece29)
piecelist.append(piece30)
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

piecelist.append(piece10)
piecelist.append(piece11)
piecelist.append(piece12)
piecelist.append(piece13)
piecelist.append(piece14)
piecelist.append(piece15)
piecelist.append(piece16)
piecelist.append(piece17)
piecelist.append(piece18)
piecelist.append(piece19)
piecelist.append(piece20)

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
