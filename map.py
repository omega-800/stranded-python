from room import Room

class Map:
    height = 4
    width = 4

    def __init__(self, rooms):
        self.rooms=rooms

    def display(self, playerCM, playerCT):
        string = ""
        h=1
        while h <= self.height:
            print(playerCM, playerCT)
            rh=1
            while rh <= Room.height:
                w=self.width
                while w >= 1:
                    print(self.rooms["x"+str(w)+"y"+str(h)])
                    if ("x"+str(w)+"y"+str(h) == playerCM):
                        print("fak")
                        string = self.rooms["x"+str(w)+"y"+str(h)].getrow(rh, playerCT) + string
                    else:
                        string = self.rooms["x"+str(w)+"y"+str(h)].getrow(rh, "") + string
                    string = "  " + string
                    w-=1
                string = "\n" + string
                rh+=1
            string = "\n" + string
            h+=1
        string+="\033[97m"
        print(string)