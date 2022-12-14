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
from .Event import Event
from .Item import Item
import random


class Generator():

    def __init__(self, parent, r_count, p_count):
        self.roomItems = parent.roomItemsArr # closed
        self.holdableItems = parent.holdableItemsArr # closed
        self.girlsNames = parent.girlsNamesArr # closed
        self.boysNames = parent.boysNamesArr # closed
        self.topics = parent.topicsArr # closed
        self.createRooms(r_count)
        self.createPeople(p_count)
        self.parent = parent
        self.rcount = r_count
        self.pcount = p_count
        
        self.distributeItems()
        
        self.e = Event(self)
        

    def getLocationFromID(self,id):
        for x in self.rooms:
            if(x.id == id):
                return x        


    def distributeItems(self):
        # moveable:
            # can belong to person or room
            # max 2 per person.. 3 per room

        # not moveable:
            # can belong to room
            # max 2 per room

        index = 0

        # non movable
        nmItems = self.roomItems

        for x in range(0, len(nmItems)):
            nmItems[x] = nmItems[x].strip('\t\n')
        
        while(True):
            chosenRoom = self.rooms[random.randint(0, len(self.rooms) - 1)]
            itemName = nmItems[random.randint(0, len(nmItems) - 1)]
            index += 1

            if(len(chosenRoom.contains) < 2):
                chosenRoom.contains.append(Item(index, itemName, False))
                print("Placed ",itemName,' into ',chosenRoom.roomName, "not movable")
            
            if(random.random() < 0.2):
                break
            


        mItems = self.holdableItems
        for x in range(0, len(mItems)-1):
            mItems[x] = mItems[x].strip('\t\n')
        
        while(True):
            # can either go to a room or a person.. 50% chance of each
            roomOrPerson = random.random()
            if(roomOrPerson < 0.5):
                # room
                chosenRoom = self.rooms[random.randint(0, len(self.rooms) - 1)]
                item = mItems[random.randint(0, len(mItems) - 1)]

                if(len(chosenRoom.contains) < 3):
                    chosenRoom.contains.append(Item(index, item,True))
                    print("Placed ",item,' into ',chosenRoom.roomName, "movable")
                
                if(random.random() < 0.2):
                    break
    
            else:
                # person
                chosenPerson = self.people[random.randint(0, len(self.people) - 1)]
                item = mItems[random.randint(0, len(mItems) - 1)]

                if(len(chosenPerson.contains) < 2):
                    chosenPerson.contains.append(Item(index, item, True))
                    print("Placed ",item,' into ',chosenRoom.roomName, "movable")
                
                if(random.random() < 0.2):
                    break


    def createRelationships(self, peopleCount):

        # relationships go: is 'mother' of / is 'father' of / is 'daughter' of
        relationships = ["friend", "mother", "father", "son", "daughter", "husband", "wife", "brother", "sister"]
        relationshipGraph = RelationshipGraph()
        # people = list of all people..
        # everyone should have at least 1 connections

        for x in self.people:
            relationshipGraph.addNode(x.id)

        # friend -> friend -> friend -> frien
        # random relationships father -> son/father -> son from a list of unvisited.

        # Makes sure there is a main link between everyone
        for x in range(0,random.randrange(1,4)): # adjust the 2,5 to change how close everyone is.
            vpeople, upeople = [], []
            for p in self.people:
                upeople.append(p.id)

            p1 = upeople.pop(random.randrange(0,len(upeople)))
            vpeople.append(p1)
            while(len(upeople)) > 0:
                p2 = upeople.pop(random.randrange(0,len(upeople)))
                relationshipGraph.addEdge(p1, p2, 0)
                relationshipGraph.addEdge(p2, p1, 0)
                vpeople.append(p2)
                p1 = p2
                # this is a list of friends

        # Adding random family elements
        vpeople, upeople = [], []
        for p in self.people:
            upeople.append(p)

        while(len(upeople)) > len(self.people) * 0.25:
            p1 = upeople.pop(random.randrange(0,len(upeople)))
            p2 = upeople.pop(random.randrange(0,len(upeople)))

            # making sure the mother / father are the right gender
            r = random.randrange(1,5)
            if(r == 1 or r == 2):
                if(p1.gender == 'male'):
                    r = 1
                else: r = 2

            if r == 1:
                # FATHER / CHILD
                p1.age = p2.age+random.randrange(22,32)
                relationshipGraph.addEdge(p1.id,p2.id,1)
                if p2.gender == 'female':
                    relationshipGraph.addEdge(p2.id,p1.id,4)
                else:
                    relationshipGraph.addEdge(p2.id,p1.id,3)

            elif r == 2:
                # MUM / CHILD
                p1.age = p2.age+random.randrange(22,40)
                relationshipGraph.addEdge(p1.id,p2.id,2)
                if p2.gender == 'female':
                    relationshipGraph.addEdge(p2.id,p1.id,4)
                else:
                    relationshipGraph.addEdge(p2.id,p1.id,3)
            
            elif r == 3:
                # HUSBAND/HUSBAND / WIFE/WIFE / HUSBAND/WIFE
                # 5 = husband, 6 = wife | is husband of, is wife of
                if p1.gender == 'male':
                    relationshipGraph.addEdge(p1.id,p2.id,5)
                else:
                    relationshipGraph.addEdge(p1.id,p2.id,6)
                
                if p2.gender == 'male':
                    relationshipGraph.addEdge(p2.id,p1.id,5)
                else:
                    relationshipGraph.addEdge(p2.id,p1.id,6)
             
            elif r == 4:
                # SIBLING 7 = Brother, 8 = Sister
                # is brother of/is sister of

                if p1.gender == 'male':
                    relationshipGraph.addEdge(p1.id,p2.id,7)
                else:
                    relationshipGraph.addEdge(p1.id,p2.id,8)
                
                if p2.gender == 'male':
                    relationshipGraph.addEdge(p2.id,p1.id,7)
                else:
                    relationshipGraph.addEdge(p2.id,p1.id,8)



    def createPeople(self, peopleCount):
        if(peopleCount == -1):
            peopleCount = random.randint(5,50)

        boys = self.boysNames
        for x in range(0, len(boys)):
            boys[x] = boys[x].strip('\t\n')

        girls = self.girlsNames
        for x in range(0, len(girls)):
            girls[x] = girls[x].strip('\t\n')

        self.people = []
        index = 1

        for x in range(0, peopleCount):


            if(random.random() < 0.5):
                # person is male
                name = boys[random.randint(0, len(boys)-1)]
                self.people.append(Person(index, name, random.randint(0,80), 'male'))


            else:
                # person is female
                name = girls[random.randint(0, 499)]
                self.people.append(Person(index, name, random.randint(0,80), 'female'))

            index += 1

        self.createRelationships(peopleCount)
            
        
        

    def createRooms(self,roomCount):

        # generate amount of rooms
        if(roomCount == -1):
            roomCount = random.randint(5,50)

        # make every room a node in the graph
        locationGraph = LocationGraph()

        possibleRooms = ["Bedroom ", "Corridor ", "Kitchen ", "Lounge ", "Balcony "]

        count = 0
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

        self.locationGraph = locationGraph
        
            




            


