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
        self.danger = 0
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
def north_recursion(obj, objx, objy, arg, xlist):
    print("north recursion")
    print("y start", objy)
    arg += -1
    objy += -50
    for i in range(len(piecelist)):
        if objy < 25:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            print("something found")
            if obj.ttype == "pawn":
                return xlist
            if obj.team != piecelist[i].team:
                coords = coordinates(objx,objy)
                xlist.append(coords)
            return xlist
    coords = coordinates(objx,objy)
    xlist.append(coords)
    print("y at the end of cycle:", objy)
    print("xlist at the end of the cycle:")
    for i in range(len(xlist)): 
        print("list size:", len(xlist),"element:", xlist[i].x, xlist[i].y)
    if arg != 0:
        north_recursion(obj, objx, objy, arg, xlist)
    else:
        return xlist

def south_recursion(obj, objx, objy, arg, xlist):
    print("south recursion")
    print("y start", objy)
    arg += -1
    objy += 50
    for i in range(len(piecelist)):
        if objy > 375:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            print("something found")
            if obj.ttype == "pawn":
                return xlist
            if obj.team != piecelist[i].team:
                coords = coordinates(objx,objy)
                xlist.append(coords)
            return xlist
    coords = coordinates(objx,objy)
    xlist.append(coords)
    print("y at the end of cycle:", objy)
    print("xlist at the end of the cycle:")
    for i in range(len(xlist)): 
        print("list size:", len(xlist),"element:", xlist[i].x, xlist[i].y)
    if arg != 0:
        south_recursion(obj, objx, objy, arg, xlist)
    else:
        return xlist

def east_recursion(obj, objx, objy, arg, xlist):
    print("south recursion")
    print("x start", x)
    arg += -1
    objx += 50
    for i in range(len(piecelist)):
        if objx > 375:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            print("something found")
            if obj.team != piecelist[i].team:
                coords = coordinates(objx,objy)
                xlist.append(coords)
            return xlist
    coords = coordinates(objx,objy)
    xlist.append(coords)
    print("y at the end of cycle:", objy)
    print("xlist at the end of the cycle:")
    for i in range(len(xlist)): 
        print("list size:", len(xlist),"element:", xlist[i].x, xlist[i].y)
    if arg != 0:
        east_recursion(obj, objx, objy, arg, xlist)
    else:
        return xlist

def west_recursion(obj, objx, objy, arg, xlist):
    print("south recursion")
    print("x start", x)
    arg += -1
    objx += -50
    for i in range(len(piecelist)):
        if objx < 25:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            print("something found")
            if obj.team != piecelist[i].team:
                coords = coordinates(objx,objy)
                xlist.append(coords)
            return xlist
    coords = coordinates(objx,objy)
    xlist.append(coords)
    print("y at the end of cycle:", objy)
    print("xlist at the end of the cycle:")
    for i in range(len(xlist)): 
        print("list size:", len(xlist),"element:", xlist[i].x, xlist[i].y)
    if arg != 0:
        west_recursion(obj, objx, objy, arg, xlist)
    else:
        return xlist

def northeast_recursion(obj, objx, objy, arg, xlist):
    arg += -1
    objx += 50
    objy += -50
    for i in range(len(piecelist)):
        if objx > 375 or objy < 25:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            if obj.team != piecelist[i].team:
                coords = coordinates(objx,objy)
                xlist.append(coords)
            return xlist
    coords = coordinates(objx,objy)
    xlist.append(coords)
    if arg != 0:
        northeast_recursion(obj, objx, objy, arg, xlist)
    else:
        return xlist

def northwest_recursion(obj, objx, objy, arg, xlist):
    arg += -1
    objx += -50
    objy += -50
    for i in range(len(piecelist)):
        if objx < 25 or objy < 25:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            if obj.team != piecelist[i].team:
                coords = coordinates(objx,objy)
                xlist.append(coords)
            return xlist
    coords = coordinates(objx,objy)
    xlist.append(coords)
    if arg != 0:
        northwest_recursion(obj, objx, objy, arg, xlist)
    else:
        return xlist

def southwest_recursion(obj, objx, objy, arg, xlist):
    arg += -1
    objx += -50
    objy += 50
    for i in range(len(piecelist)):
        if objx < 25 or objy > 375:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            if obj.team != piecelist[i].team:
                coords = coordinates(objx,objy)
                xlist.append(coords)
            return xlist
    coords = coordinates(objx,objy)
    xlist.append(coords)
    if arg != 0:
        southwest_recursion(obj, objx, objy, arg, xlist)
    else:
        return xlist
        
def southeast_recursion(obj, objx, objy, arg, xlist):
    arg += -1
    objx += 50
    objy += 50
    for i in range(len(piecelist)):
        if objx > 375 or objy > 375:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            if obj.team != piecelist[i].team:
                coords = coordinates(objx,objy)
                xlist.append(coords)
            return xlist
    coords = coordinates(objx,objy)
    xlist.append(coords)
    if arg != 0:
        southeast_recursion(obj, objx, objy, arg, xlist)
    else:
        return xlist

def knight_checker(obj):
    northeast = coordinates(obj.x+50,obj.y-100)
    eastnorth = coordinates(obj.x+100,obj.y-50)
    northwest = coordinates(obj.x-50,obj.y-100)
    westnorth = coordinates(obj.x-100,obj.y-50)
    southeast = coordinates(obj.x+50, obj.y+100)
    eastsouth = coordinates(obj.x+100, obj.y+50)
    southwest = coordinates(obj.x-50, obj.y+100)
    westsouth = coordinates(obj.x-100, obj.y+50)
    thislist = [northeast, eastnorth, northwest, westnorth, southeast, eastsouth, southwest, westsouth]
    for d in range(len(thislist)):
        for i in range(len(piecelist)):
            if (thislist[d].x == piecelist[i].x) and (thislist[d].y == piecelist[i].y):
                if obj.team == piecelist[i].team:
                    thislist[d].x = -100
                    thislist[d].y = -100
                    break
    return thislist
    


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

def fetcher(sele,status): # selects a piece
    print(status)
    pathway_cleaner()
    for i in range(0,len(piecelist)):
        if sele.x == piecelist[i].x and sele.y == piecelist[i].y:
            if sele.current_player == piecelist[i].team:
                pathways(piecelist[i], "real")
                xf = piecelist[i].x
                yf = piecelist[i].y
                sele.selectee = piecelist[i]
                canvas.moveto(flash_obj.form, xf-25, yf-25)

def pitcher(selectee,pathlist,piece29,piece30,status): # Sends the piece to the desired location
    occupied_by_friendly = False
    occupied_by_enemy = False
    occupied_by_king = False
    oldx = selectee.x
    oldy = selectee.y
    if selectee.team == "white":
        king = piece29
    if selectee.team == "black":
        king = piece30
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
    
    pathways(selectee,"invis")
    
    status = dangerchecker(piece29,piece30,status) 
    
    if king.danger == "danger":
        obj = selectee
        obj.x = oldx
        obj.y = oldy
        canvas.moveto(obj.form, oldx-25, oldy-25)
        canvas.moveto(flash_obj.form, -100, -100)
        canvas.delete(sele.form)
        sele.current_player, sele.waiting_player = sele.waiting_player, sele.current_player
        sele.selector, sele.waiter = sele.waiter, sele.selector
        sele.form = canvas.create_image(sele.x,sele.y, image=sele.selector)
        pathway_cleaner()
    print(status)
    print("king.team =", king.team,"king.danger =", king.danger)
        

pathlist_used = []
pathlist = [path_box(-100,-100) for i in range(50)]

def dangerchecker(piece29,piece30,status):
    if sele.current_player == "black":
        king = piece29
    if sele.current_player == "white":
        king = piece30
    for i in range(len(piecelist)):
        for d in range(len(piecelist[i].pathlist)):
            print(piecelist[i].pathlist[d].x, piecelist[i].pathlist[d].y)
            if king.x == piecelist[i].pathlist[d].x and king.y == piecelist[i].pathlist[d].y:
                print("DANGER FOUND IN DANGERCHECKER")
                status = "danger"
                king.danger = "danger"
                return
            else:
                king.danger = "clear"
                print("CLEARRRRRR")
                
    

def pathways(obj, arg):
    plist = []
    if obj.ttype == "pawn":
        z = 1
        if obj.firstmove == 1:
            z = 2
        if obj.team == "white":
            north_recursion(obj, obj.x, obj.y, z, plist)
            print(plist)
        if obj.team == "black":
            # nlist = north_recursion(obj.x, obj.y, 5, plist)
            south_recursion(obj, obj.x, obj.y, z, plist)
            print(plist)
    if obj.ttype == "rook":
        north_recursion(obj, obj.x, obj.y, 8, plist)
        south_recursion(obj, obj.x, obj.y, 8, plist)
        east_recursion(obj, obj.x, obj.y, 8, plist)
        west_recursion(obj, obj.x, obj.y, 8, plist)
        print(plist)
    if obj.ttype == "bishop":
        northeast_recursion(obj, obj.x, obj.y, 8, plist)
        northwest_recursion(obj, obj.x, obj.y, 8, plist)
        southwest_recursion(obj, obj.x, obj.y, 8, plist)
        southeast_recursion(obj, obj.x, obj.y, 8, plist)
    if obj.ttype == "queen":
        north_recursion(obj, obj.x, obj.y, 8, plist)
        south_recursion(obj, obj.x, obj.y, 8, plist)
        east_recursion(obj, obj.x, obj.y, 8, plist)
        west_recursion(obj, obj.x, obj.y, 8, plist)
        northeast_recursion(obj, obj.x, obj.y, 8, plist)
        northwest_recursion(obj, obj.x, obj.y, 8, plist)
        southwest_recursion(obj, obj.x, obj.y, 8, plist)
        southeast_recursion(obj, obj.x, obj.y, 8, plist)
        print(plist)
    if obj.ttype == "knight":
        plist = knight_checker(obj)
    if obj.ttype == "king":
        north_recursion(obj, obj.x, obj.y, 1, plist)
        south_recursion(obj, obj.x, obj.y, 1, plist)
        east_recursion(obj, obj.x, obj.y, 1, plist)
        west_recursion(obj, obj.x, obj.y, 1, plist)
        northeast_recursion(obj, obj.x, obj.y, 1, plist)
        northwest_recursion(obj, obj.x, obj.y, 1, plist)
        southwest_recursion(obj, obj.x, obj.y, 1, plist)
        southeast_recursion(obj, obj.x, obj.y, 1, plist)
    if arg == "real":
        pathways_placer(plist)
    if arg == "invis":
        obj.pathlist = plist

def pathway_cleaner(): # organizes the path lists
    while len(pathlist_used) > 0:
        pathlist_used[0].x = -100
        pathlist_used[0].y = -100
        canvas.moveto(pathlist_used[0].form, -100, -100)
        pathlist.append(pathlist_used[0])
        pathlist_used.pop(0)

def pathways_placer(plist):
    for i in range(len(plist)):
        canvas.moveto(pathlist[0].form, plist[i].x-25, plist[i].y-25)
        pathlist[0].x = plist[i].x
        pathlist[0].y = plist[i].y
        pathlist_used.append(pathlist[0])
        pathlist.pop(0)
    
piecelist = []
status = "clear"

piece66 = piece(225,225,"black", "pawn")
piecelist.append(piece66)
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
# piecelist.append(piece23)
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
board.bind("x", lambda x: fetcher(sele, status))
board.bind("d", lambda x: pitcher(sele.selectee,pathlist, piece29, piece30, status))
board.bind("t", lambda x: print(status))
board.bind("y", lambda x: print("team", piece29.team, "status", piece29.danger))
board.bind("u", lambda x: print("team", piece30.team, "status", piece30.danger))

#Places the graphical representation of the pieces on the board
for i in range(0,len(piecelist)):
    piece_initialiser(piecelist[i])
    pathways(piecelist[i],"invis")
    
board.mainloop()
