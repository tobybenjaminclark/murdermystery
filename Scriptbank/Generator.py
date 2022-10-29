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

from Scriptbank.RelationshipGraph import RelationshipGraph
from .LocationGraph import LocationGraph
from .Location import Location
from .Person import Person
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
        self.createPeople(5)

    def createRelationships(self, peopleCount):
        relationships = {"acquaintance", "friend", "mother", "father", "son", "daughter", "husband", "wife", "brother", "sister"}
        relationshipGraph = RelationshipGraph()
        # people = list of all people..
        # everyone should have at least 1 connections

        for x in self.people:
            relationshipGraph.addNode(x.id)


        edgearr = []
        visited_people = []
        unvisited_people = []
        for person in self.people:
            unvisited_people.append(person.id)

        r1 = unvisited_people.pop(random.randrange(0,len(unvisited_people)))
        visited_people.append(r1)
        while len(unvisited_people) > 0: # everyone should have 1 relationship
            r2 = unvisited_people.pop(random.randrange(0,len(unvisited_people)))
            edgearr.append([r1,r2])
            visited_people.append(r2)
            r1 = r2

            # you can either be parent or sibling
            # anyone can be friends with anyone


        

        
        




    def createPeople(self, peopleCount):
        if(peopleCount == -1):
            peopleCount = random.randint(5,50)

        boys = self.boysNames.readlines()
        for x in range(0, len(boys)):
            boys[x] = boys[x].strip('\t\n')

        girls = self.girlsNames.readlines()
        for x in range(0, len(girls)):
            girls[x] = girls[x].strip('\t\n')

        self.people = []
        index = 1

        for x in range(0, peopleCount):


            if(random.random() < 0.5):
                # person is male
                name = boys[random.randint(0, len(boys))]
                self.people.append(Person(index, name, random.randint(0,80), 'male'))


            else:
                # person is female
                name = girls[random.randint(0, len(boys))]
                self.people.append(Person(index, name, random.randint(0,80), 'female'))

            index += 1
            
        for x in self.people:
            print(x.id, x.name, x.age, x.gender)
        
        self.createRelationships()
        




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

        edgedict = {}
        visited_rooms = []
        unvisited_rooms = []
        for roo in self.rooms:
            unvisited_rooms.append(roo.id)

        r1 = unvisited_rooms.pop(random.randrange(0,len(unvisited_rooms)))
        visited_rooms.append(r1)
        while len(unvisited_rooms) > 0:
            r2 = unvisited_rooms.pop(random.randrange(0,len(unvisited_rooms)))
            edgedict.update({r1:r2})
            locationGraph.addEdge(r1,r2)
            visited_rooms.append(r2)
            r1 = r2

        # adding more random connections
        while(True):
            start = random.randint(0, len(self.rooms) - 1)
            end = random.randint(0, len(self.rooms) - 1)

            if(not (start == end)):
                locationGraph.addEdge(self.rooms[start].id, self.rooms[end].id)

            if(random.random() > 0.8):
                break

        locationGraph.showGraph()
        
            




            


