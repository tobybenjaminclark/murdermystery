from tkinter import *

class GUI():

    def __init__(self):

        self.sch = {
            1:"#2b2d42",
            2:"#8d99ae",
            3:"#edf2f4",
            4:"#ef233c",
            5:"#d90429",
            "bigfont":("Arial 16 bold"),
            "littelfont":("Arial 12")
        }
        
        
        self.master = Tk()
        self.logoimg = PhotoImage(file = "Scriptbank/Logo.gif")
        self.master.geometry("1920x1080")
        self.master.attributes('-fullscreen','true')
        self.master.configure(bg = self.sch[1])

        self.create_generator()

        self.master.update()
        self.master.mainloop()

        # Selection Bar
        # Right Upper Display
        # Right Lower Display
        # Left Infoview

    def create_generator(self):
        self.generator_elements = []

        # Logo
        self.logo = Label(self.master,
        image = self.logoimg,
        bg = self.sch[1])
        
        # Number of Rooms Slider Label
        self.room_scale_label = Label(self.master,
        text = "Number of Rooms",
        font = self.sch["bigfont"],
        bg = self.sch[1],
        fg = self.sch[3])

        # Number of Rooms Slider
        self.room_var = DoubleVar()
        self.room_scale = Scale(self.master,
            variable = self.room_var, 
            from_ = 5,
            to = 250,
            resolution = 5, 
            length = 500,
            sliderlength = 10,
            bg = self.sch[1],
            troughcolor = self.sch[2],
            fg = self.sch[3],
            orient = HORIZONTAL)  

        self.logo.pack()
        self.room_scale_label.pack()
        self.room_scale.pack()
        
p = GUI()