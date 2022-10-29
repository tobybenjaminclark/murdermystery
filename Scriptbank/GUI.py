from tkinter import *

class GUI():

    def __init__(self):

        self.master = Tk()
        self.master.geometry("1920x1080")
        self.master.attributes('-fullscreen','true')

        self.create_generator()

        self.master.update()
        self.master.mainloop()

        # Selection Bar
        # Right Upper Display
        # Right Lower Display
        # Left Infoview

    def create_generator(self):
        self.generator_elements = []

        # Number of Rooms Slider
        self.room_var = DoubleVar()
        self.room_scale = Scale(self.master,
            variable = self.room_var, 
            from_ = 1,
            to = 100, 
            length = 500,
            sliderlength = 10,
            orient = HORIZONTAL)  

        self.room_scale.pack()
        
p = GUI()