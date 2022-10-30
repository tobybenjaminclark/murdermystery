# import the text files from Databank

from Scriptbank import Generator as g
from Scriptbank import InterfaceGUI as ig

class Program():

    def __init__(self):

        self.girlsNames = open('Databank/girlsNames.txt')
        self.girlsNamesArr = self.girlsNames.readlines()
        self.girlsNames.close()
        self.boysNames = open('Databank/boysNames.txt')
        self.boysNamesArr = self.boysNames.readlines()
        self.boysNames.close()
        self.holdableItems = open('Databank/holdableItems.txt')
        self.holdableItemsArr = self.holdableItems.readlines()
        self.holdableItems.close()
        self.roomItems = open('Databank/roomItems.txt')
        self.roomItemsArr = self.roomItems.readlines()
        self.roomItems.close()
        self.topics = open('Databank/topics.txt')
        self.topicsArr = self.topics.readlines()
        self.topics.close()

        gui_interface = ig.InterfaceGUI(self)
        #self.generator = g.Generator(self, 5, 5)

    def generate(self,r_count,p_count):
        self.generator = g.Generator(self, r_count, p_count)


p = Program()

