import time
username="N/A"
level=int(0)

def startup():
    pass
    print("...")
    time.sleep(1)
    print("???: do you hear me?... survivor?..")
    time.sleep(1)
    username=input("what is your name?\n")

    print("ah yes",username)
    print("that checks out.")
    time.sleep(1)
    print("welcome to..")
    time.sleep(2)
    print("______ _____  ___ ______   _    _  ___   _      _   __")
    print("|  _  \  ___|/ _ \|  _  \ | |  | |/ _ \ | |    | | / / ")
    print("| | | | |__ / /_\ \ | | | | |  | / /_\ \| |    | |/ /")
    print("| | | |  __||  _  | | | | | |/\| |  _  || |    |    \ ")
    print("| |/ /| |___| | | | |/ /  \  /\  / | | || |____| |\  \ ")
    print("|___/ \____/\_| |_/___/    \/  \/\_| |_/\_____/\_| \_/")

    print("[¬º-°]¬")

    print("(m to initiate movement and wasd for moving)")
    print("")

print("welcome to dead walk")
starting= True
while starting == True:
    start=input("would you like to start? y/n \n")
    if start=="y":
        starting= False
        startup()
    else:
        print("okay?..")

