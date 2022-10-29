from time import time
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
        self.generateRoomTimes()
        self.initialRooms()

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
        print(timeList)

        # need a list for every room.. could put this in location

        # {room:{time:eventManager, time:eventManager}, room2:{time:[events]. time:[events]}}


    def generateEvents(self):
        # events can happen:
        # conversation(person1, person2, subject)
        # itemDropped(person, item)
        # itemPickedUp(person, item)

        # wasMurdered(person1 (murderer), person2 (murdered))
        # person1 must be murderer, person2 isDead = true
        pass
    
    def moveRooms(self):
        # people can move to an adjacent room
        # or stay in the current room

        pass

    def initialRooms(self):
        # put everyone in a random room
        for person in self.people:
            room = self.rooms[random.randint(0, len(self.rooms)-1)]
            person.currentRoom = room.roomName
            print(person.name , "is in", room.roomName)





# the events of all rooms at different times will be generated here


