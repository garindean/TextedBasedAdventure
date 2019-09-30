class Room:
    def __init__(self):
        self.CanGoDirection = {"forward":False,"backward":False}
        self.roominv = []
        self.roomBefore = None
        self.roomAfter = None
        self.name = ""
    def printroominv(self):
        for i in self.roominv:
            print(i.item)
