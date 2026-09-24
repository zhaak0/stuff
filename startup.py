from playsound3 import playsound
import random
import time

MapGame = False

username="N/A"
level=int(0)

def intro():
    print("...")
    time.sleep(1)
    print("???: do you hear me?... soldier?..")
    time.sleep(1)
    print("???:what is your name?\n")
    username=input("->")
    print("\n???:ah yes",username)
    print("???:that checks out.")
    time.sleep(1)
    print("???:are you even concious...")
    time.sleep(2)
    print("???:WAKEUP DAMN!")
    playsound("sounds/spray.wav")
    playsound("sounds/scream.wav")
    print("NAR:your nostrils bleed.")
    print("???:nothing like some skatole and ammonium sulfide (fart spray.), am i right!?")
    time.sleep(2)
    print("???:no?... okay........")
    time.sleep(1)
    print("???:you're probably confused...")
    time.sleep(1)
    print("well to start off, my name is...")
    playsound("sounds/drumroll.mp3")
    print("???:THE DOCTOR!!")
    time.sleep(2)
    print("the doctor:why are you looking at me like that.")

introIs=True
while introIs==True:
    introchoice=input("do you want the intro y/n")
    if introchoice=="y":
        intro()
        introIs=False
    elif introchoice=="n":
        break

def menu():

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
menu()

while (True):
    print("what is your choice?:")
    menuchoice = input("->")

    if menuchoice == "1":
        MapGame = True
        break
    if menuchoice == "2":
        print("wasd movement, e to interact probably")
    if menuchoice == "3":
        print("okay bye")
        break
while MapGame==True:
    y=8
    x=4
    map = [["w","e","e","e","e","e","e","e","w"],
           ["w","f","f","f","f","f","f","f","w"],
           ["w","f","f","f","f","f","f","f","w"],
           ["w","f","f","f","f","f","f","f","w"],
           ["w","f","f","sh","f","f","f","f","w"],
           ["w","f","f","f","f","sh","f","f","w"],
           ["w","f","f","f","sh","f","f","sh","w"],
           ["w","sh","f","f","f","f","f","f","w"],
           ["w","w","w","l","l","l","w","w","w"]]

    y_len = len(map)-1
    x_len = len(map[0])-1

    biom = {
        "w": {"t": "wall", "en": True},
        "e": {"t": "entrance", "en": False},
        "f": {"t": "floor", "en": True},
        "sh": {"t": "shop", "en": False},
        "l": {"t": "lab", "en": False}
    }

    current_tile = map[y][x]
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
    MoveChoice=("wasd")
    while play==True:
        choice = input("-> ")
        if not any(char in choice for char in MoveChoice):
            print("INVALID")
            playsound("sounds/invalid input.wav")


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
                x -= 1
        current_tile = map[y][x]
        tilename = biom[current_tile]["t"]
        entile = biom[current_tile]["en"]

        if current_tile == "sh":
            print("there is a shop here.")

        elif current_tile == "f":
            print("nothing here.")

        elif current_tile == "w":
            print("there is a wall here, try another direction.")

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
                        mosstime=False                               #an easter egg referencing a game

        elif current_tile == "l":
            labcount=labcount+1
            if labcount==3:
                print("okay try pressing w bro, get AWAY from the lab, please.")
            else:
                print("there is a lab here")

        if entile == True:
            encounter = random.randint(1,8)
            print(encounter)
            if encounter==1:
                print("youre going into battle! but not yet because i havent made it")

        if any(char in choice for char in MoveChoice):
            playsound("sounds/walk.wav")
