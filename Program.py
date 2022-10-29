# import the text files from Databank

from Scriptbank import Generator

class Program():

    def __init__(self):

        self.girlNames = open('Databank/girlsNames.txt')
        self.boysNames = open('Databank/boysNames.txt')
        self.adjectives = open('Databank/adjectives.txt')
        self.holdableItems = open('Databank/holdableItems.txt')
        self.roomItems = open('Databank/roomItems.txt')
        self.surnames = open('Databank/surnames.txt')

        self.generator = Generator(self)

p = Program()

