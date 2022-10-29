# the events of all rooms at different times will be generated here

# cabin 1 6:00:
    # who was in the room (person IDs)

    # what each person contains at this time (either here or in person)
    # what the room contains at this time (either here or room)

    # relationships of each pairing could be pulled to generate dialogue
    # e.g. A and B are father and son, A dialogue can be i was with my son

# events can happen:
    # conversation(person1, person2, subject)
    # itemDropped(person, item)
    # itemPickedUp(person, item)

    # wasMurdered(person1 (murderer), person2 (murdered))
    # person1 must be murderer, person2 isDead = true