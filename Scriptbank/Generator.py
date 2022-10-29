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

import LocationGraph


class Generator:
    def __init__(self, parent):
        self.roomItems = parent.roomItems
        self.holdableItems = parent.holdableItems
        self.girlsNames = parent.girlsNames
        self.boysNames = parent.boysNames
        self.surnames = parent.surnames
        self.adjectives = parent.adjectives

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

    def createRooms():
        possibleRooms = {""}

        # - we are in a mansion, so Bedroom 1..n, Dining Hall 1..n,
        # Corridors, Kitchens, Living Rooms, Balconys...

        

        # rooms should have a size
        # cabin: 1

    