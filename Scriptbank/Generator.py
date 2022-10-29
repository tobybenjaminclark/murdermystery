# generate first names: 100 female 100 male?
# generate last names: 100?
# generate location names:
    # - we are in a mansion, so Bedroom 1..n, Dining Hall 1..n,
    # Corridors, Kitchens, Living Rooms, Balconys...

# generate items, include a murder weapon
    # knife, chair, ...
    # probs about 50 items

# generate conversation subjects

# save all as txt files?

from .LocationGraph import LocationGraph
from .Location import Location
import random


class Generator():

    def __init__(self, parent):
        self.roomItems = parent.roomItems
        self.holdableItems = parent.holdableItems
        self.girlsNames = parent.girlsNames
        self.boysNames = parent.boysNames
        self.surnames = parent.surnames
        self.adjectives = parent.adjectives
        self.createRooms(5)

    def createRelationships():
        relationships = {"stranger", "acquaintance", "friend", "mother", "father", "son", "daughter", "husband", "wife", "brother", "sister"}

        # make relationship map
        # every person has a relationship to every other person

        # stranger -> stranger
        # friend -> friend
        # acquaintance -> acquaintance 

        # father (male) -> son (male)
        # father (male) -> daughter (female)
        # mother (female) -> son (male)
        # mother (female) -> daughter (female)

        # brother (male) -> brother (male)
        # brother (male) -> sister (female)
        
        # husband (male) -> wife (female)

        # you can either have a parent or a sibling



    def createPerson(self, gender):
        #if(gender == "f"):
            # use girl name file
            #index = random.get


        #else:
            # use boy name file
        print("")


    def createRooms(self,roomCount):

        # generate amount of rooms
        if(roomCount == -1):
            roomCount = random.randint(5,50)

        # make every room a node in the graph
        locationGraph = LocationGraph()

        possibleRooms = ["Bedroom ", "Dining Hall ", "Corridor ", "Kitchen ", "Living Room ", "Balcony "]

        count = 1
        self.rooms = []
        roomAmounts = { }

        for i in possibleRooms:
            roomAmounts[i] = 0

        for x in range(0, roomCount):
            # assign the room to a room in possibleRooms

            chosenRoom = possibleRooms[random.randint(0, len(possibleRooms)-1)]
            roomAmounts[chosenRoom] += 1
            roomName = chosenRoom + str(roomAmounts[chosenRoom])

            self.rooms.append(Location(count, roomName))
            print(self.rooms[x].id , " " , roomName)
            count +=1

        self.createLocationGraph()
        

    def createLocationGraph(self):
        # rooms: list of all rooms

        locationGraph = LocationGraph()

        for x in self.rooms:
            locationGraph.addNode((x.id))
        # add a node of every room

        # add random connections
        # min: 0, max: rooms!
        # if(every node is connected to every other node): stop
        # if()

        while(True):
            start = random.randint(0, len(self.rooms) - 1)
            end = random.randint(0, len(self.rooms) - 1)

            if(not (start == end)):
                locationGraph.addEdge(self.rooms[start].id, self.rooms[end].id)

            if(random.random() > 0.9):
                break

        duplicates = locationGraph.showGraph()
        
            




            


