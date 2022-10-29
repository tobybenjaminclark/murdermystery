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

from Scriptbank import LocationGraph, Location
import random


class Generator():

    def __init__(self, parent):
        self.roomItems = parent.roomItems
        self.holdableItems = parent.holdableItems
        self.girlsNames = parent.girlsNames
        self.boysNames = parent.boysNames
        self.surnames = parent.surnames
        self.adjectives = parent.adjectives
        print("Fuck!")
        self.createRooms(5)

    def createRelationships():
        relationships = {"stranger", "acquaintance", "friend", "mother", "father", "son", "daughter", "husband", "wife", "brother", "sister"}



    def createPeople():
        # random choice of being m or f
        # random first name from file
        # random surname

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
        print("")

    def createRooms(self,roomCount):

        print("hi")
        
        # generate amount of rooms
        if(roomCount == -1):
            roomCount = random.randint(5,50)

        # make every room a node in the graph
        locationGraph = LocationGraph()

        possibleRooms = {"Bedroom ", "Dining Hall ", "Corridor ", "Kitchen ", "Living Room ", "Balcony "}

        rooms = []
        for x in range(0, roomCount):
            # assign the room to a room in possibleRooms

            chosenRoom = random.randint(0, len(possibleRooms)-1)
            rooms.append(Location(possibleRooms[chosenRoom]))
            print(rooms[x])

        

        # starts off as Bedroom 1. Another bedroom added = bedroom 2...



