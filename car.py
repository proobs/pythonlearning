car = ""

while car != "quit":
    car = input("> ").lower()
    if car == "help":
        print("start - start car")
        print("stop - stop car")
        print("quit - exit")
    elif car == "start": 
        print("starting car")
    elif car == "stop":
        print("stopping car")
    elif car == "quit":
        print("quitting")
    else:
        print("i dont know")