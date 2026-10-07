from playsound3 import playsound
import random
import time

from win32con import MIIM_CHECKMARKS

wallcount=int(0)
MapGame = False
def line():
    print("----------------------")

def yougot(gaineditem):
    gaineditem=str(gaineditem)
    gaineditem=gaineditem.upper()
    print(f"you got a {gaineditem}!") #says "you got(this item)" so i dont have to type this whole thing out over
#                                      and over when you get a new item from looting or killing mobs

using={"weapons":"nothing","armour":"nothing"}

weparm={
    "weapons": {"nothing":0 ,"stick": 3, "crowbar": 6, "knife": 10},
    "armour":{"nothing":0 ,"leather vest":4, "metal sheets":7}
}

level = int(5)
maxhp = 15
maxhp = (level*3)+maxhp+weparm["armour"][using["armour"]]
hp = float(maxhp)
kills=0
atk = (level*1.5)+4+weparm['weapons'][using['weapons']]
levscale = level * 0.5
inventory={"weapons":[],"armour":[],"foods":[], "level": level, "HP": (hp,"/",maxhp), "attack":atk, "kills":kills }

def inv():
    global choice,inventory,using


    print(inventory)
    print("1. equip weapon  2.equip armour  3. eat something  4. exit")
    while True:
        choice=input("->")
        if choice == "3":
            if inventory["foods"] == "":
                print("you have no foods!?!?")
            else:
                findex = len((inventory["foods"]))
                tnum = 0

                for i in range(int(findex)):
                    print(tnum, ".", inventory["foods"][tnum])
                    tnum = tnum + 1
                while True:
                    try:
                        eating = int(input("->"))
                    except TypeError:
                        print("not a choice presented")

                    if inventory["foods"][eating] == "SPRsoup":
                        print("you feel so souper!")
                        print("ATK and HP increase.")
                        hp = hp + 7
                        atk = atk + 3
                        break

                    elif inventory["foods"][eating] == "CANbeans":
                        print("hienz beanz mmm")
                        print("HP increase.")
                        hp = hp + 4
                        break

        elif choice == "1":
            if inventory["weapons"] == "":
                print("you have no weapons to equip.")
            findex = len((inventory["weapons"]))
            tnum = 0

            for i in range(int(findex)):
                print(tnum, ".", inventory["weapons"][tnum])
                tnum = tnum + 1
            equipping = int(input("->"))
            using["weapons"] = inventory["weapons"][equipping]
            print(using)
            break
        if choice == "4":
            break
        elif choice == "2":
            if inventory["armour"] == "":
                print("you have no armour to equip.")

            findex = len(inventory["armour"])
            tnum = 0

            for i in range(int(findex)):
                print(tnum, ".", inventory["armour"][tnum])
                tnum = tnum + 1
            equipping = int(input("->"))
            using["armour"][0] = inventory["armour"][equipping]
            print(using)
            break

elist=["zombie","skelezombie","fatbie"]

mobs = {
    "zombie": {"attack": 4 + levscale, "HP": 7 + levscale, "rar": 1, "desc1": "the regular, mindless green prick.",
               "desc2": "hes green and greedy.\n or i mean gluttonous."},
    "skelezombie": {"attack": 7 + levscale, "HP": 4 + levscale, "rar": 2},
    "fatbie": {"attack": 2 + levscale, "HP": 12 + levscale, "rar": 3}
}
def battle():
    global atk,hp,level,maxhp,kills

    enemy=random.choice(elist)
    print(enemy)
    ehp = mobs[enemy]["HP"]
    ehp=int(ehp)
    emaxhp = ehp
    eatk = mobs[enemy]["attack"]
    rarity = mobs[enemy]["rar"]
    print(f"a {enemy} approaches!")
    turn=True
    while True:
        if ehp > 0:
            if turn == True:
                print(enemy,"-", "HP",ehp,"/",emaxhp)
                print("1. FIGHT  2.ITEM  3.RUN")
                batinput = input("->")
                if batinput == "1":
                    print("you did",atk,"damage")
                    ehp = ehp - atk
                    turn=False
                elif batinput == "2":
                    findex = len((inventory["foods"]))
                    tnum=0
                    for i in range(int(findex)):
                        print(tnum,".",inventory["foods"][tnum])
                        tnum = tnum + 1
                    eating=int(input("->"))

                    if inventory["foods"][eating] == "SPRsoup":
                        print("you feel so souper!")
                        print("ATK and HP increase.")
                        hp=hp+7
                        atk=atk+3
                        turn = False

                    elif inventory["foods"][eating] == "CANbeans":
                        print("hienz beanz mmm")
                        print("HP increase.")
                        hp=hp+4
                        turn = False

                    inventory["foods"].pop(eating)
                elif batinput=="3":
                    break
            else:
                print("the",enemy,"attacked!")
                print("the",enemy,"did",mobs[enemy]["attack"],"damage!")
                hp = hp - mobs[enemy]["attack"]
                print("your hp is now:",hp,"/",maxhp)
                turn = True
        elif ehp <= 0:
            print("battle won woo")
            print("+1 kill")
            kills = kills+1

            if kills == 5:
                print("level up!")
                level = level+1
                print("you are now level",level)
                kills = 0
            print(tilename)
            break
        if hp <= 0:
            print("you died.\nyour mission is over.")
            exit

def intro(): #module intro so you can skip the whole thing
            print("broken missing intro soz")

introIs = True #to skip the intro
while introIs == True:
    introchoice = input("do you want the intro y/n")
    if introchoice == "y":
        intro()
        introIs = False
    elif introchoice == "n":
        break


def menu(): #the menu you can access while ingame!!
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
            MapGame = True
            break
        if menuchoice == "2":
            print("")
            line()
            print("WASD to move\nE to interact with buildings and on map items\ni to access your inventory\nM to come back to this menu")
            print("-> means input")
            line()
            print("BATTLE CONTROLS\nbattles are played with the numbers corresponding to what thing you would like to select.\n1.ATTACK 2.IEM 3.RUN\nyou would enter 1 2 or 3 depending on your choice.")
            line()
            print("1 to play now ok go play press 1 thanks okay bye")
        if menuchoice == "3":
            print("okay bye")
            break


menu()

while MapGame == True:
    y = 8
    x = 4
    lab = [["w", "e", "e", "e", "e", "e", "e", "e", "w"],
           ["w", "f", "f", "f", "f", "f", "f", "f", "w"],
           ["w", "f", "f", "f", "f", "f", "f", "f", "w"],
           ["w", "f", "f", "f", "f", "f", "f", "f", "w"],
           ["w", "f", "f", "sh", "f", "f", "f", "f", "w"],
           ["w", "f", "f", "f", "f", "sh", "f", "f", "w"],
           ["w", "f", "f", "f", "sh", "f", "f", "sh", "w"],
           ["w", "sh", "f", "f", "f", "f", "f", "f", "w"],
           ["w", "w", "w", "l", "l", "l", "w", "w", "w"]]

    tunnel = [["w", "e", "e", "e", "e", "e", "e", "e", "w"],
              ["w", "f", "f", "f", "f", "f", "f", "f", "w"],
              ["w", "f", "f", "f", "f", "f", "f", "f", "w"],
              ["w", "f", "f", "f", "f", "f", "f", "f", "w"],
              ["w", "f", "f", "sh", "f", "f", "f", "f", "w"],
              ["w", "f", "f", "f", "f", "sh", "f", "f", "w"],
              ["w", "f", "f", "f", "sh", "f", "f", "sh", "w"],
              ["w", "sh", "f", "f", "f", "f", "f", "f", "w"],
              ["e", "e", "e", "e", "e", "e", "e", "e", "e"]]
    currentmap = lab
    y_len = len(currentmap) - 1
    x_len = len(currentmap[0]) - 1

    biom = {
        "w": {"t": "wall", "en": True},
        "e": {"t": "entrance", "en": False},
        "f": {"t": "floor", "en": True},
        "sh": {"t": "shop", "en": False},
        "l": {"t": "lab", "en": False},
        "rsh": {"t": "a looted shop.", "en": False}# naming the tiles on the map
    }

    current_tile = currentmap[y][x]
    tilename = biom[current_tile]["t"]
    entile = biom[current_tile]["en"]

    play = True
    print("-> means input movement\n")
    print("you've woken up in the lab.")

    labcount = 0
    encounter = 0
    encounternum=0


    while play:
        interacts=["e","i","m"]#interactions
        mapinputs = ["w","a","s","d","e","i","m"]# the inputs the player is allowed to do
        walks = ["w","a","s","d"]#walk inputs

        current_tile = currentmap[y][x]

        choice = input("-> ").lower()
        if not any(char in choice for char in mapinputs):
            print("INVALID")
            #playsound("sounds/invalid input.wav")  # if the input the player gives is invalid it tells them and makes a sound

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
                x -= 1  # movement with built in boundaries


        def icheck(itemtocheck, whatclassitem):
            if itemtocheck in inventory["weapons"] or itemtocheck in inventory["armour"]:
                print("but you already have one.")
            else:
                inventory[whatclassitem].append(itemtocheck)

        def stealing():
            for i in range(1, 3):
                whatclass = random.randint(1, 3)
                if whatclass == 1:
                    robc = random.randint(1, 10)
                    if robc == 1 or 2 or 3 or 4 or 5:
                        yougot("stick")
                        icheck("stick", "weapons")
                    elif robc == 6 or 7 or 8:
                        yougot("crowbar")
                        icheck("crowbar", "weapons")
                    elif robc == 9 or 10:
                        yougot("knife")
                        icheck("knife", "weapons")
                elif whatclass == 2:
                    robc = random.randint(1, 6)
                    if robc == 1 or 2 or 3:
                        yougot("leather vest")
                        icheck("leather vest","armour")
                    elif robc == 6 or 5:
                        yougot("metal sheets??")
                        icheck("metal sheets","armour")
                elif whatclass == 3:
                    robc = random.randint(1, 5)
                    if robc == 1 or 2 or 3:
                        yougot("canned beans")
                        inventory["foods"].append("CANbeans")
                    if robc == 4 or 5:
                        yougot("super soup!")
                        inventory["foods"].append("SPRsoup")

        current_tile = currentmap[y][x]  # ]
        tilename = biom[current_tile]["t"]  # ] finds out what tile the player is standing on
        entile = biom[current_tile]["en"]  # ]


        print(tilename)

        if choice == "i":
            inv()
        if choice == "m":
            menu()
        if choice == "e":
            if current_tile == "sh":
                print("you stealin")
                stealing()
                currentmap[y][x]="rsh"
                current_tile = currentmap[y][x]
            elif current_tile == "e":
                if currentmap == lab:
                    currentmap = tunnel
                    print("you went into the tunnel.")
                    y = y + 8
            elif current_tile == "l":
                print("the lab, you're too busy to go back there")
                labcount
            elif current_tile == "w":
                if wallcount==0:
                    print("its a wall, bland and concrete, designed to protect the town. doesnt seem like it did much of a job.")
                    wallcount=1
                elif wallcount!=0:
                    print("the wall that failed.")
        if current_tile == "sh":
            print("there is a shop here.")
        elif current_tile == "f":
            print("nothing here.")

        elif current_tile == "w":
            if y == 0 and x == 0 or x == 8 and y == 0 or y == 8 and x == 0 or x == 8 and y == 8:
                print("you're in a corner.")
            elif y == 0:
                print("there is a wall above you.")
            elif x == 0:
                print("there is a wall to your right.")
            elif x == 8:
                print("there is a wall to your left")
            elif y == 8:
                print("there is a wall below you.")

            rollmoss = random.randint(1, 10)
            if rollmoss == 1:
                mosstime = True
                while mosstime == True:
                    eatmoss = input("there is moss here. eat it? Y/N\n")
                    if eatmoss.lower() == "y":
                        print("you ate the moss.\n you feel great!")
                        mosstime = False
                    elif eatmoss.lower() == "n":
                        print("loser.")
                        mosstime = False  # an Easter egg referencing a game

        elif current_tile == "l":
            labcount = labcount + 1
            if labcount == 3:
                print("okay try pressing w bro, get AWAY from the lab, please.")
            else:
                print("there is a lab here")

        if entile == True:
            encounter = random.randint(1, 10)
            if encounter == 1:
                battle()
        if any(char in choice for char in walks):
            pass
            #playsound("sounds/walk.wav")
        elif any(char in choice for char in interacts):
            pass
            #playsound("sounds/bell.mp3")
