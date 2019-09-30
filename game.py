class Game:
    def __init__(self):
        self.lightsOn = False
        self.dooropen = False
        self.inv = []
        self.currentRoom = None

    def actOnKey(self, key, room1):
        self.inv.append(key)
        room1.roominv.remove(key)
        print("You pick up the key. It feels cold in your hands.")


    def actOnLever(self, *args):
        if self.lightsOn == True:
            print("the lights turned off")
            self.lightsOn = False

        elif self.lightsOn == False:
            print("the lights turned on")
            self.lightsOn = True

    def printinv(self):
        for i in self.inv:
            print(i.item)

    def actOnDoor(self, *args):
        if self.dooropen == True:
            print("The door closed.")
            print("")
            self.dooropen = False
            self.currentRoom.CanGoDirection["forward"] = False

        elif self.dooropen == False:
            if self.lightsOn == True:
                print("The door opened, with the sound of grinding metal.")
                print("")
                self.dooropen = True
                self.currentRoom.CanGoDirection["forward"] = True
            else:
                print("The door won't budge. It seems to be locked and electronic.")
