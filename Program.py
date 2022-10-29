# import the text files from Databank

from Scriptbank import Generator as g
from Scriptbank import InterfaceGUI as ig

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

        gui_interface = ig.InterfaceGUI(self)
        #self.generator = g.Generator(self, 5, 5)
        

    def generate(self,r_count,p_count):
        self.generator = g.Generator(self, r_count, p_count)
        

p = Program()

