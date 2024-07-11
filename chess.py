from tkinter import *
import time
import os
import threading

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
        self.pseudo = "na"
        self.passant = 0
        
class path_box():
    def __init__(self,x,y):
        self.pathimg = PhotoImage(file="pathway.png")
        self.x = x
        self.y = y
        self.form = canvas.create_image(x,y,image=self.pathimg)
        
class pseudo_path_box():
    def __init__(self,x,y):
        self.pathimg = PhotoImage(file="pseudopathway.png")
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

def north_recursion(obj, objx, objy, arg, xlist, pseudo):
    # print("north recursion")
    # print("y start", objy)
    arg += -1
    objy += -50
    coords = coordinates(objx,objy)
    for i in range(len(piecelist)):
        if objy < 25:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            if obj.ttype == "pawn":
                return xlist
            if obj.team != piecelist[i].team:
                if pseudo == 0:
                    coords.pseudo = "na"
                    pseudo += 1
                    break
                if pseudo > 0:
                    coords.pseudo = "pseudo"
                    pseudo += 1
                    break
            if obj.team == piecelist[i].team:
                pseudo += 2
                coords.pseudo = "pseudo"
                break
    if pseudo > 1:
        coords.pseudo = "pseudo"
    if pseudo == 1:
        pseudo += 1
    xlist.append(coords)
    if arg != 0:
        north_recursion(obj, objx, objy, arg, xlist, pseudo)
    else:
        return xlist

def south_recursion(obj, objx, objy, arg, xlist, pseudo):
    # print("south recursion")
    # print("y start", objy)
    arg += -1
    objy += 50
    coords = coordinates(objx,objy)
    for i in range(len(piecelist)):
        if objy > 375:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            if obj.ttype == "pawn":
                return xlist
            if obj.team != piecelist[i].team:
                if pseudo == 0:
                    coords.pseudo = "na"
                    pseudo += 1
                    break
                if pseudo > 0:
                    coords.pseudo = "pseudo"
                    pseudo += 1
                    break
            if obj.team == piecelist[i].team:
                pseudo += 2
                coords.pseudo = "pseudo"
                break
    if pseudo > 1:
        coords.pseudo = "pseudo"
    if pseudo == 1:
        pseudo += 1
    xlist.append(coords)
    if arg != 0:
        south_recursion(obj, objx, objy, arg, xlist, pseudo)
    else:
        return xlist

def east_recursion(obj, objx, objy, arg, xlist,pseudo):
    # print("south recursion")
    # print("x start", x)
    arg += -1
    objx += 50
    coords = coordinates(objx,objy)
    for i in range(len(piecelist)):
        if objx > 375:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            if obj.ttype == "pawn":
                return xlist
            if obj.team != piecelist[i].team:
                if pseudo == 0:
                    coords.pseudo = "na"
                    pseudo += 1
                    break
                if pseudo > 0:
                    coords.pseudo = "pseudo"
                    pseudo += 1
                    break
            if obj.team == piecelist[i].team:
                pseudo += 2
                coords.pseudo = "pseudo"
                break
    if pseudo > 1:
        coords.pseudo = "pseudo"
    if pseudo == 1:
        pseudo += 1
    xlist.append(coords)
    if arg != 0:
        east_recursion(obj, objx, objy, arg, xlist,pseudo)
    else:
        return xlist

def west_recursion(obj, objx, objy, arg, xlist, pseudo):
    # print("south recursion")
    # print("x start", x)
    arg += -1
    objx += -50
    coords = coordinates(objx,objy)
    for i in range(len(piecelist)):
        if objx < 25:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            if obj.ttype == "pawn":
                return xlist
            if obj.team != piecelist[i].team:
                if pseudo == 0:
                    coords.pseudo = "na"
                    pseudo += 1
                    break
                if pseudo > 0:
                    coords.pseudo = "pseudo"
                    pseudo += 1
                    break
            if obj.team == piecelist[i].team:
                pseudo += 2
                coords.pseudo = "pseudo"
                break
    if pseudo > 1:
        coords.pseudo = "pseudo"
    if pseudo == 1:
        pseudo += 1
    xlist.append(coords)
    if arg != 0:
        west_recursion(obj, objx, objy, arg, xlist, pseudo)
    else:
        return xlist

def northeast_recursion(obj, objx, objy, arg, xlist,pseudo):
    arg += -1
    objx += 50
    objy += -50
    coords = coordinates(objx,objy)
    for i in range(len(piecelist)):
        if objx > 375 or objy < 25:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            if obj.ttype == "pawn":
                return xlist
            if obj.team != piecelist[i].team:
                if pseudo == 0:
                    coords.pseudo = "na"
                    pseudo += 1
                    break
                if pseudo > 0:
                    coords.pseudo = "pseudo"
                    pseudo += 1
                    break
            if obj.team == piecelist[i].team:
                pseudo += 2
                coords.pseudo = "pseudo"
                break
    if pseudo > 1:
        coords.pseudo = "pseudo"
    if pseudo == 1:
        pseudo += 1
    xlist.append(coords)
    if arg != 0:
        northeast_recursion(obj, objx, objy, arg, xlist,pseudo)
    else:
        return xlist

def northwest_recursion(obj, objx, objy, arg, xlist,pseudo):
    arg += -1
    objx += -50
    objy += -50
    coords = coordinates(objx,objy)
    for i in range(len(piecelist)):
        if objx < 25 or objy < 25:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            if obj.ttype == "pawn":
                return xlist
            if obj.team != piecelist[i].team:
                if pseudo == 0:
                    coords.pseudo = "na"
                    pseudo += 1
                    break
                if pseudo > 0:
                    coords.pseudo = "pseudo"
                    pseudo += 1
                    break
            if obj.team == piecelist[i].team:
                pseudo += 2
                coords.pseudo = "pseudo"
                break
    if pseudo > 1:
        coords.pseudo = "pseudo"
    if pseudo == 1:
        pseudo += 1
    xlist.append(coords)
    if arg != 0:
        northwest_recursion(obj, objx, objy, arg, xlist,pseudo)
    else:
        return xlist

def southwest_recursion(obj, objx, objy, arg, xlist,pseudo):
    arg += -1
    objx += -50
    objy += 50
    coords = coordinates(objx,objy)
    for i in range(len(piecelist)):
        if objx < 25 or objy > 375:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            if obj.ttype == "pawn":
                return xlist
            if obj.team != piecelist[i].team:
                if pseudo == 0:
                    coords.pseudo = "na"
                    pseudo += 1
                    break
                if pseudo > 0:
                    coords.pseudo = "pseudo"
                    pseudo += 1
                    break
            if obj.team == piecelist[i].team:
                pseudo += 2
                coords.pseudo = "pseudo"
                break
    if pseudo > 1:
        coords.pseudo = "pseudo"
    if pseudo == 1:
        pseudo += 1
    xlist.append(coords)
    if arg != 0:
        southwest_recursion(obj, objx, objy, arg, xlist,pseudo)
    else:
        return xlist
        
def southeast_recursion(obj, objx, objy, arg, xlist,pseudo):
    arg += -1
    objx += 50
    objy += 50
    coords = coordinates(objx,objy)
    for i in range(len(piecelist)):
        if objx > 375 or objy > 375:
            return xlist
        if (objx == piecelist[i].x) and (objy == piecelist[i].y):
            if obj.ttype == "pawn":
                return xlist
            if obj.team != piecelist[i].team:
                if pseudo == 0:
                    coords.pseudo = "na"
                    pseudo += 1
                    break
                if pseudo > 0:
                    coords.pseudo = "pseudo"
                    pseudo += 1
                    break
            if obj.team == piecelist[i].team:
                pseudo += 2
                coords.pseudo = "pseudo"
                break
    if pseudo > 1:
        coords.pseudo = "pseudo"
    if pseudo == 1:
        pseudo += 1
    xlist.append(coords)
    if arg != 0:
        southeast_recursion(obj, objx, objy, arg, xlist,pseudo)
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
                    thislist[d].pseudo = "pseudo"
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

def fetcher(sele): # selects a piece
    pathway_cleaner()
    for i in range(0,len(piecelist)):
        if sele.x == piecelist[i].x and sele.y == piecelist[i].y:
            if sele.current_player == piecelist[i].team:
                pathways(piecelist[i], "real")
                xf = piecelist[i].x
                yf = piecelist[i].y
                sele.selectee = piecelist[i]
                canvas.moveto(flash_obj.form, xf-25, yf-25)
                return piecelist[i]

def impossiblecheck():
    c = len(sele.selectee.pathlist)
    b = 0
    for i in range(len(sele.selectee.pathlist)):
        # print("CROSS REFFING SELE:", "selex",sele.x, "seley",sele.y, "TO", "selecteepathlist",i,"x:", sele.selectee.pathlist[i].x,"y: ", sele.selectee.pathlist[i].y)
        if sele.selectee.pathlist[i].x == sele.x and sele.selectee.pathlist[i].y == sele.y:
                # print("incrementing b by 1")
                b = 1
    if b != 1:
        # print("IMPOSSIBLE MOVE")
        return 1

def pitcher(selectee,pathlist): # Sends the piece to the desired location
    global piece29, piece30
    piece29.danger = "clear"
    piece30.danger = "clear"
    for i in range(0,len(piecelist)):
        pathways(piecelist[i],"invis")
    a = 0
    b = 0
    occupied_by_friendly = False
    occupied_by_enemy = False
    occupied_by_king = False
    oldx = selectee.x
    oldy = selectee.y
    oldfirstmove = selectee.firstmove
    matchfound = 0
    if selectee.team == "white":
        playerking = piece29
    if selectee.team == "black":
        playerking = piece30
    
    impossible = impossiblecheck()
    if impossible == 1:
        board.after(0, printimpossible)
        return

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
                for i in range(len(obj.pathlist)):
                    if obj.team == "white":
                        if obj.pathlist[i].passant != 0:
                            if obj.pathlist[i].passant.x == sele.x and obj.pathlist[i].passant.y-50 == sele.y:
                                obj.pathlist[i].passant.x = -100
                                obj.pathlist[i].passant.y = -100
                                canvas.moveto(obj.pathlist[i].passant.form, obj.pathlist[i].passant.x-100, obj.pathlist[i].passant.y-100)
                    if obj.team == "black":
                        if obj.pathlist[i].passant != 0:
                            if obj.pathlist[i].passant.x == sele.x and obj.pathlist[i].passant.y+50 == sele.y:
                                obj.pathlist[i].passant.x = -100
                                obj.pathlist[i].passant.y = -100
                                canvas.moveto(obj.pathlist[i].passant.form, obj.pathlist[i].passant.x-100, obj.pathlist[i].passant.y-100)                                
                if obj.ttype == "king" and obj.team == "white" and obj.firstmove == 1:        
                    if sele.x == 325 and sele.y == 375:
                        for i in range(len(obj.pathlist)):
                            if obj.pathlist[i].x == 325 and obj.pathlist[i].y == 375:
                                if obj.pathlist[i].castle == "ready":
                                    piece18.x = 275
                                    canvas.moveto(piece18.form, piece18.x-25, piece18.y-25)
                    if sele.x == 125 and sele.y == 375:
                        for i in range(len(obj.pathlist)):
                            if obj.pathlist[i].x == 125 and obj.pathlist[i].y == 375:
                                if obj.pathlist[i].castle == "ready":
                                    piece17.x = 175
                                    canvas.moveto(piece17.form, piece17.x-25, piece17.y-25)
                if obj.ttype == "king" and obj.team == "black" and obj.firstmove == 1:        
                    if sele.x == 325 and sele.y == 25:
                        for i in range(len(obj.pathlist)):
                            if obj.pathlist[i].x == 325 and obj.pathlist[i].y == 25:
                                if obj.pathlist[i].castle == "ready":
                                    piece20.x = 275
                                    canvas.moveto(piece20.form, piece20.x-25, piece20.y-25)
                    if sele.x == 125 and sele.y == 25:
                        for i in range(len(obj.pathlist)):
                            if obj.pathlist[i].x == 125 and obj.pathlist[i].y == 25:
                                if obj.pathlist[i].castle == "ready":
                                    piece19.x = 175
                                    canvas.moveto(piece19.form, piece19.x-25, piece19.y-25)
                obj.x = sele.x
                obj.y = sele.y
                canvas.moveto(obj.form, obj.x-25, obj.y-25)
                canvas.moveto(flash_obj.form, -100, -100)
                canvas.delete(sele.form)
                sele.current_player, sele.waiting_player = sele.waiting_player, sele.current_player
                sele.selector, sele.waiter = sele.waiter, sele.selector
                sele.form = canvas.create_image(sele.x,sele.y, image=sele.selector)
                break
        pathway_cleaner()
    for i in range(0,len(piecelist)):
        pathways(piecelist[i],"invis")
    if occupied_by_enemy == True and matchfound == 1 and playerking.danger != "danger":
        enemy.x = -100
        enemy.y = -100
        canvas.moveto(enemy.form, -100,-100)
        # if occupied_by_king == True: probably redundant, delete later
            # print("GAME OVER")
    for i in range(0,len(piecelist)):
        pathways(piecelist[i],"invis")
    status1 = dangerchecker() 
    # print(playerking.team,"STATUS OF THE PLAYER KING", playerking.danger)
    pathways(selectee,"invis")
    # print("piece29.team =", piece29.team,"piece29.danger =", piece29.danger)
    # print("piece30.team =", piece30.team,"piece30.danger =", piece30.danger)
    status2 = dangerchecker2(oldx,oldy,selectee)
    # print("FIRSTMOVE STATUS", obj.firstmove)
    if status1 != "danger":
        if selectee.firstmove == 1:
            selectee.firstmove = 2
    if status1 == "danger" and status2 != "invalid":
        board.after(0, printcheck)
        checkmatechecker()
        

pathlist_used = []
pseudo_pathlist_used = []
pathlist = [path_box(-100,-100) for i in range(80)]
pseudo_pathlist = [pseudo_path_box(-100,-100) for i in range(80)]

# def checkmatechecker():
    # attackerlist = []
    # for i in range(0,len(piecelist)):
        # pathways(piecelist[i],"invis")
    # if piece29.danger == "danger":
        # king = piece29
        # enemylist = blacklist
    # if piece30.danger == "danger":
        # king = piece30
        # enemylist = whitelist
    # waysfound = len(king.pathlist) 
    # for d in range(len(king.pathlist)):
        # for t in range(len(enemylist)):
            # for p in range(len(enemylist[t].pathlist)):
                # if king.pathlist[d].x == enemylist[t].pathlist[p].x and king.pathlist[d].y == enemylist[t].pathlist[p].y:
                    # attackerlist.append(enemylist[t])
                    # waysfound -= 1
    # print("WAYS AT THE END OF THE FIRST LOOP", waysfound)
    # if waysfound <= 0:
        # waysfound = 0
        # for i in range(len(attackerlist)):
            # for g in range(len(attackerlist[i].pathlist)):
                # for t in range(len(whitelist)):
                    # for p in range(len(whitelist[t].pathlist)):
                        # if whitelist[t].ttype != "king":
                            # if attackerlist[i].pathlist[g].x == whitelist[t].pathlist[p].x and attackerlist[i].pathlist[g].y == whitelist[t].pathlist[p].y:
                                # waysfound += 1                                                
    # if waysfound < 0:
        # print("GAME OVER ")
    # print("AMOUNT OF WAYS FOUND AT THE END OF THE SECOND LOOP",waysfound)

def attackerloopback(king, attacker):
    xlist = []
    n = 0
    s = 0
    e = 0
    w = 0
    if attacker.x > king.x:
        e = 1
    if attacker.x < king.x:
        w = 1
    if attacker.y > king.y:
        s = 1
    if attacker.y < king.y:
        n = 1
    if n == 1 and (0 = e and w): # attack from north
        pass
    if s == 1 and (0 = e and w): # attack from south
        pass
    if e == 1 and (0 = n and s): # attack from east
        pass
    if w == 1 and (0 = n and s): # attack from west
        pass
    if n == 1 and w == 1: # attack from northwest
        pass
    if n == 1 and e == 1: # attack from northeast
        pass
    if s == 1 and w == 1: # attack from southwest
        pass
    if s == 1 and e == 1: # attack from southeast
        pass

def checkmatechecker():
    for i in range(0,len(piecelist)):
        pathways(piecelist[i],"invis")
    if piece29.danger == "danger":
        king = piece29
        enemylist = blacklist
        allylist = whitelist 
    if piece30.danger == "danger":
        king = piece30
        enemylist = whitelist
        allylist = blacklist
    waysfound = len(king.pathlist) 
    for i in range(len(enemylist)):
        for d in range(len(enemylist[i].pathlist)):
                if enemylist[i].pathlist[d].x == king.x and enemylist[i].pathlist[d].y == king.y:
                        attacker = enemylist[i]
                        print("ATTACKER LOCATED")
    for d in range(len(king.pathlist)): # loop to check every possible pathway of the king against every possible pathway(na/pseudo) of the enemies
        for t in range(len(enemylist)):
            for p in range(len(enemylist[t].pathlist)): # (king pseudo pathways? don't think they're possible but keep this in mind in case problems arise)
                if king.pathlist[d].x == enemylist[t].pathlist[p].x and king.pathlist[d].y == enemylist[t].pathlist[p].y:
                    waysfound -= 1
    print("WAYS AT THE END OF THE FIRST LOOP", waysfound)
    if waysfound <= 0:
        waysfound = 0
    for i in range(len(allylist)): # loop to check the attacking pathway 
        for d in range(len(allylist[i].pathlist)):
            for p in range(len(attacker.pathlist)):
                if allylist[i].pathlist[d].pseudo == "na" and attacker.pathlist[p].pseudo == "na":
                    if allylist[i].pathlist[d].x == attacker.pathlist[p].x and allylist[i].pathlist[d].y == attacker.pathlist[p].y:
                        waysfound += 1            
    if waysfound <= 0:
        print("GAME OVER")
    print("POTENTIAL PATHWAYS OF THE KING", len(king.pathlist))
    print("AMOUNT OF WAYS FOUND AT THE END OF THE SECOND LOOP",waysfound)
            

def dangerchecker():
    for i in range(0,len(piecelist)):
        pathways(piecelist[i],"invis")
    for i in range(len(piecelist)):
        for d in range(len(piecelist[i].pathlist)):
            if piecelist[i].pathlist[d].pseudo == "na":
                if piece29.x == piecelist[i].pathlist[d].x and piece29.y == piecelist[i].pathlist[d].y:
                    # print("DANGER FOUND IN DANGERCHECKER")
                    piece29.danger = "danger"
                    return "danger"
                else:
                    piece29.danger = "clear"
                    # print("CLEARRRRRR")
    for i in range(len(piecelist)):
        for d in range(len(piecelist[i].pathlist)):
            if piecelist[i].pathlist[d].pseudo == "na":
                if piece30.x == piecelist[i].pathlist[d].x and piece30.y == piecelist[i].pathlist[d].y:
                    # print("DANGER FOUND IN DANGERCHECKER")
                    piece30.danger = "danger"
                    return "danger"
                else:
                    piece30.danger = "clear"
                    # print("CLEARRRRRR")


def sendback(oldx, oldy, selectee):
    obj = selectee
    obj.x = oldx
    obj.y = oldy
    canvas.moveto(obj.form, oldx-25, oldy-25)
    canvas.moveto(flash_obj.form, -100, -100)
    canvas.delete(sele.form)
    sele.current_player, sele.waiting_player = sele.waiting_player, sele.current_player
    sele.selector, sele.waiter = sele.waiter, sele.selector
    sele.form = canvas.create_image(sele.x,sele.y, image=sele.selector)
    if selectee.team == "white":
        piece29.danger = "clear"          
    if selectee.team == "black":
        piece30.danger = "clear"    

def dangerchecker2(oldx, oldy, selectee):
    a = 1
    if piece29.danger == "danger":
        if selectee.team == "white":
            board.after(0, printinvalid)
            sendback(oldx,oldy, selectee)
            return "invalid"
    if piece30.danger == "danger":
        if selectee.team == "black":
            board.after(0, printinvalid)
            sendback(oldx,oldy,selectee)
            return "invalid"
    pathway_cleaner()        

def printcheck():
        checkrect = canvas.create_rectangle(100, 150, 300, 250, fill="orange")
        text = canvas.create_text(200,200,text="CHECK", font=("Tahoma", 17))
        board.after(1500, deleteinvalid, checkrect, text)
        
def printinvalid():
        invalidrect = canvas.create_rectangle(100, 150, 300, 250, fill="orange")
        text = canvas.create_text(200,200,text="CAN'T MOVE THERE,\n DANGER DETECTED", font=("Tahoma", 14))
        board.after(2000, deleteinvalid, invalidrect, text)

def printimpossible():
        imposrect = canvas.create_rectangle(100, 150, 300, 250, fill="orange")
        text = canvas.create_text(200,200,text="IMPOSSIBLE MOVE", font=("Tahoma", 14))
        board.after(800, deleteinvalid, imposrect, text)

def deleteinvalid(inv, txt):
    canvas.delete(inv, txt)
    

def pathways(obj, arg):
    plist = []
    if obj.x < 0 or obj.y < 0: # might be redundant, double check later
        return
    if obj.ttype == "pawn":
        z = 1
        if obj.firstmove == 1:
            z = 2
        if obj.team == "white":
            north_recursion(obj, obj.x, obj.y, z, plist, 0)
            for i in range(len(piecelist)):
                if piecelist[i].x == obj.x+50 and piecelist[i].y == obj.y-50:
                    if piecelist[i].team != obj.team:
                        coords = coordinates(obj.x+50,obj.y-50)
                        plist.append(coords)  
                if piecelist[i].x == obj.x-50 and piecelist[i].y == obj.y-50:
                    if piecelist[i].team != obj.team:
                        coords = coordinates(obj.x-50,obj.y-50)
                        plist.append(coords)  
                if obj.y == 175: # WHITE PASSANT
                    if piecelist[i].team != obj.team:
                        if piecelist[i].y == 175 and piecelist[i].x == obj.x-50:
                            coords = coordinates(obj.x-50,obj.y-50)
                            coords.passant = piecelist[i]
                            plist.append(coords)
                        if piecelist[i].y == 175 and piecelist[i].x == obj.x+50:
                            coords = coordinates(obj.x+50,obj.y-50)
                            coords.passant = piecelist[i]
                            plist.append(coords)                                  
            print(plist)
        if obj.team == "black":
            # nlist = north_recursion(obj.x, obj.y, 5, plist)
            south_recursion(obj, obj.x, obj.y, z, plist,0)
            for i in range(len(piecelist)):
                if piecelist[i].x == obj.x+50 and piecelist[i].y == obj.y+50:
                    if piecelist[i].team != obj.team:
                        coords = coordinates(obj.x+50,obj.y+50)
                        plist.append(coords)  
                if piecelist[i].x == obj.x-50 and piecelist[i].y == obj.y+50:
                    if piecelist[i].team != obj.team:
                        coords = coordinates(obj.x-50,obj.y+50)
                        plist.append(coords) 
                if obj.y == 225: # BLACK PASSANT
                    if piecelist[i].team != obj.team:
                        if piecelist[i].y == 225 and piecelist[i].x == obj.x-50:
                            coords = coordinates(obj.x-50,obj.y+50)
                            coords.passant = piecelist[i]
                            plist.append(coords)
                        if piecelist[i].y == 225 and piecelist[i].x == obj.x+50:
                            coords = coordinates(obj.x+50,obj.y+50)
                            coords.passant = piecelist[i]
                            plist.append(coords)                         
            print(plist)
    if obj.ttype == "rook":
        north_recursion(obj, obj.x, obj.y, 8, plist, 0)
        south_recursion(obj, obj.x, obj.y, 8, plist,0)
        east_recursion(obj, obj.x, obj.y, 8, plist,0)
        west_recursion(obj, obj.x, obj.y, 8, plist,0)
        print(plist)
    if obj.ttype == "bishop":
        northeast_recursion(obj, obj.x, obj.y, 8, plist, 0)
        northwest_recursion(obj, obj.x, obj.y, 8, plist, 0)
        southwest_recursion(obj, obj.x, obj.y, 8, plist, 0)
        southeast_recursion(obj, obj.x, obj.y, 8, plist, 0)
    if obj.ttype == "queen":
        north_recursion(obj, obj.x, obj.y, 8, plist, 0)
        south_recursion(obj, obj.x, obj.y, 8, plist,0)
        east_recursion(obj, obj.x, obj.y, 8, plist,0)
        west_recursion(obj, obj.x, obj.y, 8, plist,0)
        northeast_recursion(obj, obj.x, obj.y, 8, plist, 0)
        northwest_recursion(obj, obj.x, obj.y, 8, plist, 0)
        southwest_recursion(obj, obj.x, obj.y, 8, plist, 0)
        southeast_recursion(obj, obj.x, obj.y, 8, plist, 0)
        print(plist)
    if obj.ttype == "knight":
        plist = knight_checker(obj)
    if obj.ttype == "king":
        north_recursion(obj, obj.x, obj.y, 1, plist, 0)
        south_recursion(obj, obj.x, obj.y, 1, plist,0)
        east_recursion(obj, obj.x, obj.y, 1, plist,0)
        west_recursion(obj, obj.x, obj.y, 1, plist,0)
        northeast_recursion(obj, obj.x, obj.y, 1, plist, 0)
        northwest_recursion(obj, obj.x, obj.y, 1, plist, 0)
        southwest_recursion(obj, obj.x, obj.y, 1, plist, 0)
        southeast_recursion(obj, obj.x, obj.y, 1, plist, 0)
        if obj.team == "white": # castle white
            if piece18.firstmove == 1 and piece29.firstmove == 1: # right
                if piece22.x != 275 or piece22.y != 375:
                    if piece31.x != 325 or piece31.y != 375:
                        coords = coordinates(325,375)
                        coords.castle = "ready"
                        plist.append(coords)
            if piece29.firstmove == 1 and piece17.firstmove == 1: # left
                if piece28.x != 75 or piece28.y != 375:
                    if piece21.x != 125 or piece21.y != 375:
                        if piece26.x != 175 or piece26.y != 375:
                            coords2 = coordinates(125,375)
                            coords2.castle = "ready"
                            plist.append(coords2)                                   
        if obj.team == "black": # castle black
            if piece20.firstmove == 1 and piece30.firstmove == 1: # right
                if piece33.x != 325 or piece33.y != 25:
                    if piece25.x != 275 or piece25.y != 25:
                        coords = coordinates(325,25)
                        coords.castle = "ready"
                        plist.append(coords)
            if piece19.firstmove == 1 and piece30.firstmove == 1: # left
                if piece27.x != 175 or piece27.y != 25:
                    if piece24.x != 125 or piece24.y != 25:
                        if piece32.x != 75 or piece26.y != 25:
                            coords2 = coordinates(125,25)
                            coords2.castle = "ready"
                            plist.append(coords2)
    for i in range(len(plist)):
        print("THIS IS ABOUT TO GO THROUGH THE FUNCTIONS", plist[i].pseudo, plist[i].x, plist[i].y)
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
    while len(pseudo_pathlist_used) > 0:
        pseudo_pathlist_used[0].x = -100
        pseudo_pathlist_used[0].y = -100
        canvas.moveto(pseudo_pathlist_used[0].form, -100, -100)
        pseudo_pathlist.append(pseudo_pathlist_used[0])
        pseudo_pathlist_used.pop(0)

def pathways_placer(plist):
    print("PATHWAYS PLACER")
    # for i in range(len(plist)):  encountered a problem where I would have a "na" and "pseudo" duplicate of the same coordinates. This is a very bad fix.
        # for d in range(len(plist)):
            # if plist[i].x == plist[d].x and plist[i].y == plist[d].y:
                # if plist[i].pseudo != plist[d].pseudo:
                    # print("MATCH FOUND")
                    # plist[d].pseudo = "pseudo"
                    # plist[i].pseudo = "pseudo"
    for i in range(len(plist)):
        print(plist[i].pseudo)
        if plist[i].pseudo == "na":
            canvas.moveto(pathlist[0].form, plist[i].x-25, plist[i].y-25)
            pathlist[0].x = plist[i].x
            pathlist[0].y = plist[i].y
            pathlist_used.append(pathlist[0])
            pathlist.pop(0)
            
def pseudopathway_debug():
    object = fetcher(sele)
    for i in range(len(object.pathlist)):
        if object.pathlist[i].pseudo == "pseudo":
            canvas.moveto(pseudo_pathlist[0].form, object.pathlist[i].x-25, object.pathlist[i].y-25)
            pseudo_pathlist[0].x = object.x
            pseudo_pathlist[0].y = object.y
            pseudo_pathlist_used.append(pseudo_pathlist[0])
            pseudo_pathlist.pop(0)
    
def debugger():
    for i in range(len(piecelist)):
        if piecelist[i].team == "black":
            if piecelist[i].ttype != "king":
                piecelist[i].x = -100
                piecelist[i].y = -100
                canvas.moveto(piecelist[i].form, piecelist[i].x-25, piecelist[i].y-25)
    
piecelist = []
whitelist = []
blacklist = []
status1 = 0
status2 = 0

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

for i in range(len(piecelist)):
    if piecelist[i].team == "white":
        whitelist.append(piecelist[i])
    if piecelist[i].team == "black":
        blacklist.append(piecelist[i])

board.bind("<Right>", lambda x: mover(sele, x=50, y=0))
board.bind("<Left>", lambda x: mover(sele, x=-50, y=0))
board.bind("<Up>", lambda x: mover(sele, x=0, y=-50))
board.bind("<Down>", lambda x: mover(sele, x=0, y=50))
board.bind("x", lambda x: fetcher(sele))
board.bind("o", lambda x: debugger())
board.bind("p", lambda x: pseudopathway_debug())
board.bind("d", lambda x: pitcher(sele.selectee,pathlist))
board.bind("y", lambda x: print("team", piece29.team, "status", piece29.danger))
board.bind("u", lambda x: print("team", piece30.team, "status", piece30.danger))

#Places the graphical representation of the pieces on the board
for i in range(0,len(piecelist)):
    piece_initialiser(piecelist[i])
    pathways(piecelist[i],"invis")
    
board.mainloop()
