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
    pathway_cleaner()
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

def pathway_cleaner(): # organizes the path lists
    x = 0
    while len(pathlist_used) > 0:
        pathlist_used[0].x = -100
        pathlist_used[0].y = -100
        canvas.moveto(pathlist_used[0].form, -100, -100)
        pathlist.append(pathlist_used[0])
        pathlist_used.pop(0)
        x += 1

def crossref(checkerlist, obj, way): # checks if the output of the direction checker and piecelist overlap
    matchlist = []
    z = False
    if obj.team == "white":
        z = True
    if obj.ttype == "rook" or "queen":
        if way == "updown":
            for i in range(0, len(piecelist)):
                if piecelist[i].y in (checkerlist[d].y for d in range(0, len(checkerlist))) and piecelist[i].x == obj.x:
                    matchlist.append(piecelist[i])
        if way == "leftright":
            for i in range(0, len(piecelist)):
                if piecelist[i].x in (checkerlist[d].x for d in range(0, len(checkerlist))) and piecelist[i].y == obj.y:
                    matchlist.append(piecelist[i])
    if obj.ttype == "bishop" or "queen":
        if way == "diagonal":
            for i in range(0, len(piecelist)):
                for d in range(0,len(checkerlist)):
                    if (piecelist[i].x, piecelist[i].y) == (checkerlist[d].x, checkerlist[d].y):
                        matchlist.append(piecelist[i])
    if obj.ttype == "pawn":
        for i in range(0, len(piecelist)):
            if piecelist[i].y in (checkerlist[d].y for d in range(0, len(checkerlist))) and piecelist[i].x == obj.x:
                matchlist.append(piecelist[i])
    if obj.ttype == "knight":
        teamlist = []
        for i in range(len(checkerlist)):
            for d in range(len(piecelist)):
                if (piecelist[d].x == checkerlist[i].x) and (checkerlist[i].y == piecelist[d].y) and (obj.team == piecelist[d].team):
                    checkerlist[i].put = "dont"
        matchlist = checkerlist
    if len(matchlist) == 0: # bad fix
        c = coordinates(-100,-100)
        matchlist = [c]
    return matchlist

def direction_checker_leftright(obj): # check left and right
    leftrightlist = []
    if obj.ttype == "rook":
        for i in range(25,425,50):
            if obj.x != i:
                a = coordinates(i, obj.y)
                leftrightlist.append(a)
    return leftrightlist

def direction_checker_west(obj):
    thelist = []
    for i in range(obj.x-50,-75,-50):
        a = coordinates(i, obj.y)
        thelist.append(a)
    return thelist
            
def direction_checker_east(obj):
    thelist = []
    for i in range(obj.x+50,425,50):
        a = coordinates(i, obj.y)
        thelist.append(a)
    return thelist
            
def direction_checker_north(obj):
    thelist = []
    for i in range(obj.y-50,-25,-50):
        a = coordinates(obj.x, i)
        thelist.append(a)
    return thelist

def direction_checker_south(obj):
    thelist = []
    for i in range(425,obj.y,-50):
        a = coordinates(obj.x, i)
        thelist.append(a)
    return thelist

def direction_checker_northeast(obj):
    thelist = []
    z = 0
    v = 0
    for i in range(obj.x+25, 375, 50):
        z = z + 50
        v = v - 50
        a = coordinates(obj.x+z, obj.y+v)
        thelist.append(a)
    return thelist

def direction_checker_northwest(obj):
    thelist = []
    z = 0
    for i in range(obj.x-25, 25, -50):
        z = z + 50
        a = coordinates(obj.x-z, obj.y-z)
        thelist.append(a)
    return thelist

def direction_checker_southwest(obj):
    thelist = []
    z = 0
    v = 0
    for i in range(obj.x-25, 25, -50):
        z = z + 50
        v = v - 50
        a = coordinates(obj.x-z, obj.y-v)
        thelist.append(a)
    return thelist

def direction_checker_southeast(obj):
    thelist = []
    z = 0
    for i in range(obj.x+25, 375, 50):
        z = z + 50
        a = coordinates(obj.x+z, obj.y+z)
        thelist.append(a)
    return thelist

def direction_checker_updown(obj): # check north and south for pawns
    updownlist = []
    if obj.ttype == "pawn":
        b = -50
        d = -25
        c = -50
        if obj.team == "black":
            b = 50
            d = 375
            c = 50
        for i in range(obj.y+b, d,c):
            a = coordinates(obj.x, i)
            updownlist.append(a)
    return updownlist

def pathways_checker_bishop2(somethingthere,somethingthere2, somethingthere3, somethingthere4, obj):
    z = 0
    t = 0
    t2 = 0
    t3 = 0
    t4 = 0
    if somethingthere[0].team == obj.team:
        t = 50
    if somethingthere2[0].team == obj.team:
        t2 = -50
    if somethingthere3[0].team == obj.team:
        t3 = -50
    if somethingthere4[0].team == obj.team:
        t4 = 50
    for i in range(obj.x, somethingthere[0].x+t, -50):
        z = z + 50
        canvas.moveto(pathlist[0].form, obj.x-z-25, obj.y-z-25)
        pathlist[0].x = obj.x-z
        pathlist[0].y = obj.y-z
        pathlist_used.append(pathlist[0])
        pathlist.pop(0)
    z = 0
    for i in range(obj.x, somethingthere2[0].x+t2, 50):
        z = z + 50
        canvas.moveto(pathlist[0].form, obj.x+z-25, obj.y+z-25)
        pathlist[0].x = obj.x+z
        pathlist[0].y = obj.y+z
        pathlist_used.append(pathlist[0])
        pathlist.pop(0)
    z = 0
    c = 0
    for i in range(obj.x, somethingthere3[0].x+t3, 50):
        z = z + 50
        c = c - 50
        canvas.moveto(pathlist[0].form, obj.x+z-25, obj.y+c-25)
        pathlist[0].x = obj.x+z
        pathlist[0].y = obj.y+c
        pathlist_used.append(pathlist[0])
        pathlist.pop(0)
    z = 0
    c = 0
    for i in range(obj.x, somethingthere4[0].x+t4, -50):
        z = z - 50
        c = c + 50
        canvas.moveto(pathlist[0].form, obj.x+z-25, obj.y+c-25)
        pathlist[0].x = obj.x+z
        pathlist[0].y = obj.y+c
        pathlist_used.append(pathlist[0])
        pathlist.pop(0)

def pathways_checker_bishop(obj):
    z = 0
    northwestlist = direction_checker_northwest(obj)
    southeastlist = direction_checker_southeast(obj)
    northeastlist = direction_checker_northeast(obj)
    southwestlist = direction_checker_southwest(obj)
    somethingthere = crossref(northwestlist, obj, "diagonal")
    somethingthere2 = crossref(southeastlist, obj, "diagonal")
    somethingthere3 = crossref(northeastlist, obj, "diagonal")
    somethingthere4 = crossref(southwestlist, obj, "diagonal")
    if somethingthere[0].y == -100:
        somethingthere[0].x = -25
    if somethingthere2[0].y == -100:
        somethingthere2[0].x = 425
    if somethingthere3[0].y == -100:
        somethingthere3[0].x = 425
    if somethingthere4[0].y == -100:
        somethingthere4[0].y = 425
    somethingthere.sort(key=lambda f: f.y, reverse=True)
    somethingthere2.sort(key=lambda f: f.y)
    somethingthere3.sort(key=lambda f: f.x)
    somethingthere4.sort(key=lambda f: f.x, reverse=True)
    pathways_checker_bishop2(somethingthere, somethingthere2, somethingthere3, somethingthere4, obj)

def pathways_checker_rook(obj):
    northlist = direction_checker_north(obj)
    southlist = direction_checker_south(obj)
    eastlist = direction_checker_east(obj)
    westlist = direction_checker_west(obj)
    somethingthere = crossref(northlist, obj, "updown")
    somethingthere2 = crossref(southlist, obj, "updown")
    somethingthere3 = crossref(eastlist, obj, "leftright")
    somethingthere4 = crossref(westlist, obj, "leftright")
    if somethingthere[0].y == -100:
        somethingthere[0].y = -25
    if somethingthere2[0].y == -100:
        somethingthere2[0].y = 425
    if somethingthere3[0].x == -100:
        somethingthere3[0].x = 425
    if somethingthere4[0].x == -100:
        somethingthere4[0].x = -25
    somethingthere.sort(key=lambda f: f.y, reverse=True)
    somethingthere2.sort(key=lambda f: f.y)
    somethingthere3.sort(key=lambda f: f.x)
    somethingthere4.sort(key=lambda f: f.x, reverse=True)
    pathways_checker_rook2(somethingthere, somethingthere2, somethingthere3, somethingthere4, obj)

def pathways_checker_rook2(somethingthere, somethingthere2, somethingthere3, somethingthere4, obj):
    t = 0
    t2 = 0
    t3 = 0
    t4 = 0
    if somethingthere[0].team == obj.team:
        t = 50
    if somethingthere2[0].team == obj.team:
        t2 = -50
    if somethingthere3[0].team == obj.team:
        t3 = -50
    if somethingthere4[0].team == obj.team:
        t4 = 50
    for i in range(obj.y-50, somethingthere[0].y-50+t, -50):
        canvas.moveto(pathlist[0].form, obj.x-25, i-25)
        pathlist[0].x = obj.x
        pathlist[0].y = i
        pathlist_used.append(pathlist[0])
        pathlist.pop(0)
    for i in range(somethingthere2[0].y+t2, obj.y, -50):
        canvas.moveto(pathlist[0].form, obj.x-25, i-25)
        pathlist[0].x = obj.x
        pathlist[0].y = i
        pathlist_used.append(pathlist[0])
        pathlist.pop(0)
    for i in range(obj.x+50, somethingthere3[0].x+50+t3, 50):
        canvas.moveto(pathlist[0].form, i-25, obj.y-25)
        pathlist[0].x = i
        pathlist[0].y = obj.y
        pathlist_used.append(pathlist[0])
        pathlist.pop(0)
    for i in range(somethingthere4[0].x+t4, obj.x, 50):
        canvas.moveto(pathlist[0].form, i-25, obj.y-25)
        pathlist[0].x = i
        pathlist[0].y = obj.y
        pathlist_used.append(pathlist[0])
        pathlist.pop(0)

def pathways_checker_king(obj):
    northwest = coordinates(obj.x-50, obj.y-50)
    north = coordinates(obj.x, obj.y-50)
    northeast = coordinates(obj.x+50, obj.y-50)
    east = coordinates(obj.x+50, obj.y)
    southeast = coordinates(obj.x+50, obj.y+50)
    south = coordinates(obj.x, obj.y+50)
    southwest = coordinates(obj.x-50, obj.y+50)
    west = coordinates(obj.x-50, obj.y)
    cordlist = [northwest,north,northeast,east,southeast,south,southwest,west]
    matchlist = cordlist
    for i in range(len(matchlist)):
        canvas.moveto(pathlist[0].form, matchlist[i].x-25, matchlist[i].y-25)
        pathlist[0].x = matchlist[i].x
        pathlist[0].y = matchlist[i].y
        pathlist_used.append(pathlist[0])
        pathlist.pop(0)
        
def pathways_checker_knight(obj):
    northwest = coordinates(obj.x-50, obj.y-100)
    westnorth = coordinates(obj.x-100, obj.y-50)
    southwest = coordinates(obj.x-50, obj.y+100)
    westsouth = coordinates(obj.x-100, obj.y+50)
    northeast = coordinates(obj.x+50, obj.y-100)
    eastnorth = coordinates(obj.x+100, obj.y-50)
    southeast = coordinates(obj.x+50, obj.y+100)
    eastsouth = coordinates(obj.x+100, obj.y+50)
    cordlist = [northwest, westnorth, southwest, westsouth, northeast, eastnorth, southeast, eastsouth]
    matchlist = crossref(cordlist, obj, "whatever")
    for i in range(len(matchlist)):
        if matchlist[i].put != "dont":
            canvas.moveto(pathlist[0].form, matchlist[i].x-25, matchlist[i].y-25)
            pathlist[0].x = matchlist[i].x
            pathlist[0].y = matchlist[i].y
            pathlist_used.append(pathlist[0])
            pathlist.pop(0)
    
def pathways_checker_pawn(obj): # Creates pathways on board for pawns
    x = obj.x
    y = obj.y
    e = -50
    k = -75
    h = -100
    r = -125
    if obj.team == "black":
        e = 50
        k = 25
        h = 100
        r = 75        
    updownlist = direction_checker_updown(obj)
    somethingthere = crossref(updownlist, obj, "updown")
    if obj.team == "black":
        somethingthere.sort(key=lambda f: f.y)
    else:
        somethingthere.sort(key=lambda f: f.y, reverse=True)
    if (obj.y+e) != somethingthere[0].y:
        pathlist_used.append(pathlist[0])
        pathlist.pop(0)
        canvas.moveto(pathlist_used[0].form, x-25,y+k)
        pathlist_used[0].x = x
        pathlist_used[0].y = y+e
        if obj.firstmove == 1 and (obj.y+h) != somethingthere[0].y:
            pathlist_used.append(pathlist[1])
            pathlist.pop(1)
            canvas.moveto(pathlist_used[1].form, x-25,y+r)
            pathlist_used[1].x = x
            pathlist_used[1].y = y+h
    if obj.team == "black":
        z = 100
    else:
        z = 0
    upper_x = [x-50, x+50]
    upper_y = y-50+z
    for i in range(0,len(piecelist)): # DIAGONALS
        if (piecelist[i].x in upper_x) and upper_y == piecelist[i].y:
             if obj.team != piecelist[i].team:
                 newpath = pathlist[0]
                 pathlist_used.append(newpath)
                 pathlist.pop(0)
                 canvas.moveto(newpath.form, piecelist[i].x-25, piecelist[i].y-25)
                 newpath.x = piecelist[i].x
                 newpath.y = piecelist[i].y
    

def pathways(obj):
    if obj.ttype == "pawn":
        pathways_checker_pawn(obj)
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
