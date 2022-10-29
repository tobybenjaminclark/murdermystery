# import the text files from Databank

from Scriptbank import Generator as g

class Program():

    def __init__(self):

        self.girlsNames = open('Databank/girlsNames.txt')
        self.boysNames = open('Databank/boysNames.txt')
        self.adjectives = open('Databank/adjectives.txt')
        self.holdableItems = open('Databank/holdableItems.txt')
        self.roomItems = open('Databank/roomItems.txt')
        self.surnames = open('Databank/surnames.txt')
        self.occupations = open('Databank/occupations.txt')
        self.topics = open('Databank/topics.txt')

        self.generator = g.Generator(self)

p = Program()

