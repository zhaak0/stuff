
y=0
x=5
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

