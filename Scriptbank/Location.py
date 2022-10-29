# contains a graph of the different locations in the map
# undirected graph, edges act as doors, nodes contain rooms

# location (cabin 1, main hall 1, etc)

# could either have what the room contains in here 
# or in event class

class Location():

    count = 1

    def __init__(self, id, roomName):
        # roomName
        self.id = count
        count+=1

        self.roomName = roomName
        