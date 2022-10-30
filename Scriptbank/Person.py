# this contains information about a person in the murder mystery
# name, age, occupation
# unique person id

# could either have contains: here with items e.g. knife for murder weapon
# or have contains: in event class so no need to get info from this class

# boolean isMurderer, isDead

class Person:

    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.isMurderer = False # after set random person to true
        self.isDead = False
        self.contains = [] # maybe change this to in event
        self.currentRoom = -1
