import random
y=8
x=4
map = [["w","e","e","e","e","e","e","e","w"],
       ["w","f","f","f","f","f","f","f","w"],
       ["w","f","f","f","f","f","f","f","w"],
       ["w","f","f","f","f","f","f","f","w"],
       ["w","f","f","sh","f","f","f","f","w"],
       ["w","f","f","f","f","sh","f","f","w"],
       ["w","f","f","f","f","f","f","sh","w"],
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
while play==True:
    dest = input("-> ")


    if dest == "w":
        if y > 0:
            y -= 1
    elif dest == "d":
        if x < x_len:
            x += 1
    elif dest == "s":
        if y < y_len:
            y += 1
    elif dest == "a":
        if x > 0:
            x -= 1
    current_tile = map[y][x]
    tilename = biom[current_tile]["t"]
    entile = biom[current_tile]["en"]

    if current_tile == "sh":
        print("there is a shop here.")
    elif current_tile == "w":
        print("there is a wall here, try another direction.")
        rollmoss=random.randint(1,10)
        if rollmoss==1:
            mosstime=True
            while mosstime==True:
                eatmoss=input("there is moss here. eat it? Y/N\n")
                if eatmoss.lower()=="y":
                    print("you ate the mosss.\n you feel great!")
                    mosstime=False
                elif eatmoss.lower() == "n":
                    print("loser.")
                    mosstime=False

    elif current_tile == "l":
        labcount=labcount+1
        if labcount==3:
            print("okay try pressing w bro, get AWAY from the lab, please.")
        else:
            print("there is a lab here")
    elif entile == True:
        print("enemies can spawn!")
