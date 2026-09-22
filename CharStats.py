import random
import time
name=input("whats your name")
level=int(1)
hplevel=10*(level*1.5)
PlayerCharacter={"level":level , "HP": hplevel , "Name": name}
print("character is level :" PlayerCharacter["level"])
print(PlayerCharacter["HP"])
print(PlayerCharacter["Name"])
