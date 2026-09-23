y=0
x=0
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

print(y_len,x_len)
print(x,y)

biom = {
    "w": {"t": "wall", "en": True},
    "e": {"t": "entrance", "en": False},
    "f": {"t": "floor", "en": True},
    "sh": {"t": "shop", "en": False},
    "l": {"t": "lab", "en": False}
}

current_tile = map[y][x]
print(current_tile)
tilename=biom[current_tile]["t"]
print(tilename)
entile=biom[current_tile]["en"]
print(entile)

play = True
print("w - north")
print("d - east")
print("s - south")
print("a - west")
print("0 - stop moving")
print("# means input movement")

while play==True:
    current_tile = map[y][x]
    tilename = biom[current_tile]["t"]
    print(current_tile)
    dest=input("# ")
    if current_tile == "sh":
        print("there is a shop here.")
    if dest == "0":
        break
    elif dest == "w":
        if y > 0:
            y-= 1
    elif dest == "d":
        if x < x_len:
            x+= 1
    elif dest == "s":
        if y < y_len:
            y+= 1
    elif dest == "a":
        if x > 0:
            x-=1
    current_tile = map[y][x]
    tilename = biom[current_tile]["t"]
