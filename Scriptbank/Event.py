from time import time

from .EventInstance import EventInstance
from .Location import Location
from .Person import Person
from .RelationshipGraph import RelationshipGraph
from .LocationGraph import LocationGraph
import datetime
import random

class Event():

    def __init__(self, gen):
        self.gen = gen
        self.people = self.gen.people
        self.rooms = self.gen.rooms
        self.locationGraph = self.gen.locationGraph
        self.startTime = '16:00'
        self.topics = self.gen.topics
        self.generateRoomTimes()
        self.setupEvents()
        self.initialRooms()
        self.generateEvents()
        self.determineMurderer()


    def setupEvents(self):
        bigdict = {}
        for r in self.rooms:
            bigdict[r.id] = {}
            for t in self.timeList:
                e = EventInstance([],[],[])
                bigdict[r.id].update({t:e})
        self.bigdict = bigdict

    def generateRoomTimes(self):

        # each room will have time intervals from e.g. 4pm - 11pm
        
        # cabin 1 6:00:
            # who was in the room (person IDs)

            # what each person contains at this time (either here or in person)
            # what the room contains at this time (either here or room)

            # relationships of each pairing could be pulled to generate dialogue

        # i need to generate items belonging to each person and in each room, 
        # it would make sense to do this in generator but it would be weird,
        # idk whether to generate it in event or in the people and rooms holding them 

        startTime = 16 # 4pm
        endTime = 23 # 11pm
        spacing = 30    # in minutes

        lst = [str(i*datetime.timedelta(minutes=spacing)) for i in range(24*60//spacing)]
        timeList = []
        for x in range(0, len(lst)):
            lst[x] = lst[x][:-3]
            if(not(int(lst[x].split(':')[0]) < startTime or int(lst[x].split(':')[0]) > endTime)):
                timeList.append(lst[x])
        
        self.timeList = timeList

        # need a list for every room.. could put this in location

        # {room:{time:[events], time:[events]}, room2:{time:[events]. time:[events]}}

    def getPersonFromID(self,id):
        for x in self.people:
            if(x.id == id):
                return x

    def generateEvents(self):
        # events can happen:
        # conversation(person1, person2, subject)
        # itemDropped(person, item)
        # itemPickedUp(person, item)

        # wasMurdered(person1 (murderer), person2 (murdered))
        # person1 must be murderer, person2 isDead = true
        possibleEvents = ["conversation", "itemDropped", "itemPickedUp", "wasMurdered"]

        topic = self.topics
        
        for x in range(0, len(topic)):
            topic[x] = topic[x].strip('\t\n')
            topic[x].split('.', 1)[1]
            topic[x] = topic[x][3:len(topic)] 

            if(topic[x][0] == " "):
                topic[x] = topic[x][1:len(topic)]

        # this works
        
        for room in self.rooms:
            for time in self.timeList:

                movable = []

                
                for item in room.contains:
                    if(item.movable == True):
                        movable.append(item)

                if(len(movable) > 0):
                    if(random.random() < 0.5):
                        ppl = self.bigdict[room.id][time].people
                        if(len(ppl) > 0):
                            p = ppl[random.randint(0, len(ppl)-1)]
                            person = self.getPersonFromID(p)
                            item = movable[random.randint(0, len(movable)-1)]
                            person.contains.append(item)
                            room.contains.remove(item)
                            self.bigdict[room.id][time].events.append("itemPickedUp(" + str(person.id) + ", " + str(item.name) + ")")
                
                people = self.bigdict[room.id][time].people
                if(len(people) > 1): # there are multiple people in the room
                    if(random.random() < 0.3):
                        p1 = people[random.randint(0, len(people)-1)]
                        p2 = people[random.randint(0, len(people)-1)]
                        person1 = self.getPersonFromID(p1)
                        person2 = self.getPersonFromID(p2)
                        if(not(person1 == person2)):
                            chosenTopic = topic[random.randint(0, len(topic)-1)]
                            self.bigdict[room.id][time].events.append("conversation(" + str(person1.id) + ", " + str(person2.id) + ", " + chosenTopic + ")")
                            self.bigdict[room.id][time].events.append("conversation(" + str(person2.id) + ", " + str(person1.id) + ", " + chosenTopic + ")")
                    
                # people is id.. get person from id

                for p in people:
                    person = self.getPersonFromID(p)
                    if(len(person.contains) > 0):
                        # someone has an item
                        if(random.random() < 0.2):
                            item = person.contains[random.randint(0, len(person.contains)-1)]
                            person.contains.remove(item)
                            room.contains.append(item)
                            self.bigdict[room.id][time].events.append("itemDropped(" + str(person.id) + ", " + str(item.name) + ")")
            for item in room.contains:
                self.bigdict[room.id][time].roomContains.append(item.name)
            

        for time in self.timeList:
            for room in self.rooms:
                print(time + " " + str(room.id))
                print("people", self.bigdict[room.id][time].people)
                print("events", self.bigdict[room.id][time].events) 
                print("room contains", self.bigdict[room.id][time].roomContains)
                for p in self.bigdict[room.id][time].people:
                    p = self.getPersonFromID(p)
                    for item in p.contains:
                        print(p.id, "holds", item.name)
                
    def moveRooms(self, time):
        # people can move to an adjacent room
        # or stay in the current room
        locationGraph = self.gen.locationGraph
        for person in self.people:
            # use the location graph to get adjacent nodes

            if(random.random() > 0.7):
                connections = locationGraph.returnConnections(person.currentRoom)
                newLocationID = connections[random.randint(0, len(connections)-1)]
                # got the new id of where to move
                person.currentRoom = self.rooms[newLocationID].id
                self.bigdict[newLocationID][time].people.append(person.id)
            else:
                self.bigdict[person.currentRoom][time].people.append(person.id)
                
    def initialRooms(self):
        # put everyone in a random room

        for time in self.timeList:
            print(time, self.startTime)
            if(time == self.startTime):
                for person in self.people:
                    room = self.rooms[random.randint(0, len(self.rooms)-1)]
                    person.currentRoom = room.id
                    self.bigdict[room.id][self.startTime].people.append(person.id)
            else:
                self.moveRooms(time)

        # need to put people in different rooms in each time interval
        # started with first time interval, put people in random rooms
        # then move people to an adjacent room every interval
        # eventmanager stores the list of people in a room and the list of events that happen
        # eventmanager doesnt store time or room
        # {room:{time:eventManager, time:eventManager}, room2:{time:[events]. time:[events]}}

# the events of all rooms at different times will be generated here

    def determineMurderer(self):
        # the murderer must have a weapon or be on a balcony
        # the murderer must be with another person
        possibleMurderers = []
        for room in self.rooms:
            for time in self.timeList:
                if(len(self.bigdict[room.id][time].people) > 1):
                    for person in self.bigdict[room.id][time].people:
                        person = self.getPersonFromID(person)
                        if(len(person.contains) > 0):
                            # contains a murder weapon
                            possibleMurderers.append(person.id)
        print(possibleMurderers)
        if(len(possibleMurderers) == 0):
            print("regenerating")
            self.gen.parent.generate(self.gen.rcount, self.gen.pcount)
        else:
            murderer = self.people[possibleMurderers[random.randint(0, len(possibleMurderers)-1)]-1]
            print("murderer is", murderer.id)
            murderer.isMurderer = True


