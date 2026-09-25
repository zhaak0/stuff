from playsound3 import playsound
import random
import time

from script6 import labbacktotal

MapGame = False


level=int(0)

def intro():
    print("...")
    input()
    print("???: do you hear me?... soldier?..")
    input()
    print("???:what is your name?\n")
    username = input("your name:")
    print("\n???:ah yes",username)
    print("???:that checks out.")
    input()
    print("???:are you even conscious...")
    input()
    print("???:WAKEUP DAMN!")
    playsound("sounds/spray.wav")
    playsound("sounds/scream.wav")
    print("NAR:your nostrils bleed.")
    print("???:nothing like some skatole and ammonium sulfide (fart spray.), am i right!?")
    input()
    print("???:no?... okay........")
    input()
    print("???:you're probably confused...")
    input()
    print("well to start off, my name is...")
    playsound("sounds/drumroll.mp3")
    print("???:THE DOCTOR!!")
    time.sleep(2)
    print("doc:why are you looking at me like that.")
    input()
    print("doc:well so basically like")
    input()
    print("doc:well errr so bascially whats happening is that..")
    input()
    print("doc:so its kkindaaa baaaadd-")
    time.sleep(0.5)
    print("???:THERES A ZOMBIE APOCALYPSE AND YOU'RE THE WORLDS LAST HOPE.")
    print("1.'im the worlds last hope???'\n2.'ok now who are you.'\n3.'AAAAAAAAAHH'")
    dc=input("ya")
    if dc=="1":
        print("doc:*cough* yeah pretty much...")
    elif dc=="2":
        print("don't worry about her, shes just a little passionate about this whole zombie thing")
        input()
        print("???:RAAAAHHGG ZOMBIE SAVIOUR WOOAAW!!")
    elif dc=="3":
        print("???:RAAAAAAAAAAAH")
        input()
        print("doc:SHUT UP! THE BOTH OF YOU!!")
        input()
        print("???:okay sorry.")
        dc=input("1.'sorry not sorry ahahah'\n2.'yeah sorry... kinda.'")
        if dc=="1":
            print("???:ahahahahaahahaha good one ahaha")
        elif dc=="2":
            print("yeah totally yeah like sorry probably no not really ITS A ZOMBIE APOCALYPSE SHUT UP")
        
            

introIs=True
while introIs==True:
    introchoice=input("do you want the intro y/n")
    if introchoice=="y":
        intro()
        introIs=False
    elif introchoice=="n":
        break

def menu():
    global MapGame
    print("______ _____  ___ ______   _    _  ___   _      _   __")
    print("|  _  \\  ___|/ _ \\|  _  \\ | |  | |/ _ \\ | |    | | / / ")
    print("| | | | |__ / /_\\ \\ | | | | |  | / /_\\ \\| |    | |/ /")
    print("| | | |  __||  _  | | | | | |/\\| |  _  || |    |    \\ ")
    print("| |/ /| |___| | | | |/ /  \\  /\\  / | | || |____| |\\  \\ ")
    print("|___/ \\____/\\_| |_/___/    \\/  \\/\\_| |_/\\_____/\\_| \\_/")

    print("[¬º-°]¬\n")
    print("----------------------")
    print("# 1 --> play")
    print("# 2 --> controls")
    print("# 3 --> quit(no please stay.)")
    print("----------------------")
    while True:
        print("what is your choice?:")
        menuchoice = input("->")
        if menuchoice == "1":
            MapGame=True
            break
        if menuchoice == "2":
            print("wasd movement, e to interact probably, m to come back here")
        if menuchoice == "3":
            print("okay bye")
            break
menu()


while MapGame==True:
    y=8
    x=4
    lab = [["w", "e", "e", "e", "e", "e", "e", "e", "w"],
           ["w","f","f","f","f","f","f","f","w"],
           ["w","f","f","f","f","f","f","f","w"],
           ["w","f","f","f","f","f","f","f","w"],
           ["w","f","f","sh","f","f","f","f","w"],
           ["w","f","f","f","f","sh","f","f","w"],
           ["w","f","f","f","sh","f","f","sh","w"],
           ["w","sh","f","f","f","f","f","f","w"],
           ["w","w","w","l","l","l","w","w","w"]]

    tunnel=[["w","e","e","e","e","e","e","e","w"],
           ["w","f","f","f","f","f","f","f","w"],
           ["w","f","f","f","f","f","f","f","w"],
           ["w","f","f","f","f","f","f","f","w"],
           ["w","f","f","sh","f","f","f","f","w"],
           ["w","f","f","f","f","sh","f","f","w"],
           ["w","f","f","f","sh","f","f","sh","w"],
           ["w","sh","f","f","f","f","f","f","w"],
           ["e","e","e","e","e","e","e","e","e"]]
    currentmap=lab
    y_len = len(currentmap)-1
    x_len = len(currentmap[0])-1

    biom = {
        "w": {"t": "wall", "en": True},
        "e": {"t": "entrance", "en": False},
        "f": {"t": "floor", "en": True},
        "sh": {"t": "shop", "en": False},
        "l": {"t": "lab", "en": False}      #naming the tiles on the map
    }

    current_tile = currentmap[y][x]
    tilename=biom[current_tile]["t"]
    entile=biom[current_tile]["en"]

    play = True
    print("w - north")
    print("d - east")
    print("s - south")
    print("a - west")
    print("0 - stop moving")
    print("-> means input movement\n")
    print("you've woken up in the lab.")

    labcount=0
    encounter=0

    inputs={"walkinputs": "wasd" , "interacting": "e" }  #the inputs the player is allowed to do
    while play:
        current_tile = currentmap[y][x]
        choice = input("-> ").lower()
        if not any(char in choice for char in inputs["walkinputs"]):
            print("INVALID")
            playsound("sounds/invalid input.wav")   #if the input the player gives is invalid it tells them and makes a sound

            if choice == "m":
                menu()
        if choice == "w":
            if y > 0:
                y -= 1
        elif choice == "d":
            if x < x_len:
                x += 1
        elif choice == "s":
            if y < y_len:
                y += 1
        elif choice == "a":
            if x > 0:
                x -= 1              #movement with built in boundaries
        print(x,y)

        current_tile = currentmap[y][x]   #]
        tilename = biom[current_tile]["t"]#] finds out what tile the player is standing on
        entile = biom[current_tile]["en"] #]

        print(tilename)
        if choice == "e":
            if current_tile == "sh":
                print("you stealin")
            if current_tile == "e":
                if currentmap == lab:
                    currentmap = tunnel
                    print("you went into the tunnel.")
                    y = y+8

        if current_tile == "sh":
            print("there is a shop here.")

        elif current_tile == "f":
            print("nothing here.")

        elif current_tile == "w":
            if y == 0 and x == 0 or x == 8 and y == 0 or y== 8 and x == 0 or x == 8 and y == 8:
                print("you're in a corner.")
            elif y == 0:
                print("there is a wall above you.")
            elif x == 0:
                print("there is a wall to your right.")
            elif x == 8:
                print("there is a wall to your left")
            elif y == 8:
                print("there is a wall below you.")


            rollmoss=random.randint(1,10)
            if rollmoss==1:
                mosstime=True
                while mosstime==True:
                    eatmoss=input("there is moss here. eat it? Y/N\n")
                    if eatmoss.lower()=="y":
                        print("you ate the moss.\n you feel great!")
                        mosstime=False
                    elif eatmoss.lower() == "n":
                        print("loser.")
                        mosstime=False                               #an Easter egg referencing a game

        elif current_tile == "l":
            labcount=labcount+1
            if labcount==3:
                print("okay try pressing w bro, get AWAY from the lab, please.")
            else:
                print("there is a lab here")

        if entile == True:
            encounter = random.randint(1,8)
            if encounter==1:
                print("youre going into battle! but not yet because i havent made it")

        if any(char in choice for char in walkinputs):
            playsound("sounds/walk.wav")
