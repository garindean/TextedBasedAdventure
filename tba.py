from game import Game
from room import Room


rungame =True

#lights game



game = Game()
room1 = Room()
room2 = Room()

game.currentRoom = room1
room1.roomAfter = room2
room2.roomBefore = room1

#item class
class Item:
  def __init__(self,item,desc,acton):
      self.item = item
      self.desc = desc
      self.act = acton



#ROOM 1
largelever = Item("Lever", "The lever has a small imprint on it. it reads Main Power",game.actOnLever)
metaldoor = Item("Metal Door.",  "Flush with the wall, except for a knob",game.actOnDoor)
key = Item("Copper Key.", "Just a small copper key",game.actOnKey)
knob = Item("A metal knob.","it looks loose",game.actOnDoor)
watch = Item("Watch","You can't find your watch.",game.actOnDoor)
#room 2
genlever = Item("A Heavy Lever","The lever has a large imprint on it. It reads Computer Power.",game.actOnDoor)
computer = Item("A Large Computer","It is powered off.",game.actOnDoor)
lockdoor = Item("A Small Door.","It seems to have no power. You see a small lock.",game.actOnDoor)
room1.roominv.extend([largelever,metaldoor,key,knob,watch])
room2.roominv.extend([genlever,computer,lockdoor])
room1.name = "Maintenance Room"
room2.name = "Control Room"
dict = {"lever":largelever,"key":key,"door":metaldoor,"knob":knob,"watch":watch,"computer lever":genlever,"computer":computer,"locked door":lockdoor}





def process(otherinp):
    otherinp = otherinp.lower()
    if "act on" in otherinp:
        otherinp = otherinp.replace("act on ","")
        if dict[otherinp] in game.currentRoom.roominv:
            dict[otherinp].act(key, room1)
        else:
            print("There is no "+otherinp)

    elif "go" in otherinp:
        otherinp = otherinp.replace("go ","")
        try:
            if game.currentRoom.CanGoDirection[otherinp] == True:
                if otherinp == "forward":
                    game.currentRoom = game.currentRoom.roomAfter
                elif otherinp == "backward":
                    game.currentRoom = game.currentRoom.roomBefore
                print("You are in " + game.currentRoom.name)

            else:
                print("You cannot go there")
        except:
            print("I don't understand")


    elif otherinp == "debugdoor":
        game.lightsOn =True
        print("debug activated")
        game.inv.append(key)
        room1.roominv.remove(key)



    elif otherinp == "inventory":
        game.printinv()


    elif otherinp == "help":
        print("act on to see a itme ")

    elif otherinp == "debugroominv":
        game.currentRoom.printroominv()

    elif otherinp == "lights":
        print("")
        if game.lightsOn ==True:
            print("The lights are on!")
        else:
            print("The Lights are off!")
    else:
        try:
            print(dict[otherinp].desc)
        except:
            print("I don't understand.")


print("act on to act on a thing-")
print()
print()
print("You wake up in a small room. You check your watch, only to realize that it is missing.")
print()
print()
print("You see a few things at first glance. You see a Copper Key, Metal Door and a Lever.")
print()


while rungame ==True:
    print("")
    check = input("What do you want to check out? ")
    process(check)
