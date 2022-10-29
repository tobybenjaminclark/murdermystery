from tkinter import *

class GUI():

    def __init__(self):

        self.master = Tk()
        self.master.geometry("1920x1080")
        self.master.attributes('-fullscreen','true')

        self.label = Label(self.master, text="Hello Tkinter!")
        self.label.pack()

        self.master.update()
        self.master.mainloop()

p = GUI()