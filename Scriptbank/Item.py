# unique item id
# item name
# bool isMurderWeapon
# either can be held by a person or in a room

class Item():
    def __init__(self, id, name, movable):
        self.id = id
        self.name = name
        self.movable = movable