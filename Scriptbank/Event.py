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
        self.generateRoomTimes()
        self.setupEvents()
        self.initialRooms()
        

    def setupEvents(self):
        bigdict = {}
        for r in self.rooms:
            bigdict[r.id] = {}
            for t in self.timeList:
                e = EventInstance([],[])
                bigdict[r.id].update({t:e})
        print(bigdict)
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


    def generateEvents(self):
        # events can happen:
        # conversation(person1, person2, subject)
        # itemDropped(person, item)
        # itemPickedUp(person, item)

        # wasMurdered(person1 (murderer), person2 (murdered))
        # person1 must be murderer, person2 isDead = true
        pass
    
    def moveRooms(self, time):
        # people can move to an adjacent room
        # or stay in the current room
        locationGraph = self.gen.locationGraph
        for person in self.people:
            # use the location graph to get adjacent nodes
            
            #connections = locationGraph.returnConnections(person.currentRoom)
            #newLocationID = connections[random.randint(0, len(connections)-1)]
            # got the new id of where to move
            #person.currentRoom = self.rooms[newLocationID].id
            #self.bigdict[newLocationID][time].people.append(person.id)
            pass




        
    def initialRooms(self):
        # put everyone in a random room

        
        for time in self.timeList:
            if(time == self.startTime):
                for person in self.people:
                    room = self.rooms[random.randint(0, len(self.rooms)-1)]
                    person.currentRoom = room.id
                    print(self.bigdict[room.id][self.startTime])
                    #self.bigdict[room.id][self.startTime].people.append(person.id)
            else:
                self.moveRooms(time)
            
        print(self.bigdict)

        

        # need to put people in different rooms in each time interval
        # started with first time interval, put people in random rooms
        # then move people to an adjacent room every interval
        # eventmanager stores the list of people in a room and the list of events that happen
        # eventmanager doesnt store time or room
        # {room:{time:eventManager, time:eventManager}, room2:{time:[events]. time:[events]}}
        
        








# the events of all rooms at different times will be generated here


