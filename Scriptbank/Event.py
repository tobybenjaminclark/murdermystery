from curses import REPORT_MOUSE_POSITION
from .Location import Location
from .Person import Person
from .Generator import Generator
from .RelationshipGraph import RelationshipGraph
from .LocationGraph import LocationGraph

class Event():

    def generateRoomTimes(self):
        # each room will have time intervals from e.g. 4pm - 11pm
        
        # cabin 1 6:00:
            # who was in the room (person IDs)

            # what each person contains at this time (either here or in person)
            # what the room contains at this time (either here or room)

            # relationships of each pairing could be pulled to generate dialogue

        pass

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



# the events of all rooms at different times will be generated here


