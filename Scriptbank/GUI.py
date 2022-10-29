from tkinter import *
import random

class GUI():

    def __init__(self, parent):

        self.sch = {
            1:"#2b2d42",
            2:"#8d99ae",
            3:"#edf2f4",
            4:"#ef233c",
            5:"#d90429",
            "bigfont":("Arial 16 bold"),
            "littlefont":("Arial 12")
        }
        
        self.master = Tk()
        self.parent = parent
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
        
        # Introductory Paragraph
        introtext = """
        Murder Mystery is a desktop application that challenges you to use your
        sleuthing skills to find the killer! The game is set in a luxorious mansion,
        filled with guests holding dark secrets and intimate relationships.
        Can you interrogate the guests, refute the lies, and examine the
        relationships to discover the truth?
        
        The game settings are incredibly adaptable, allowing you to create 
        the perfect environment that fits your needs. You can change the
        number of people and rooms in your game: more components will allow
        for a more complex and challenging environment.
        
         """

        self.introlabel = Label(self.master,
        text = introtext,
        anchor=CENTER,
        fg = self.sch[3],
        bg = self.sch[1],
        font = self.sch['littlefont'])

        # Room Frame
        self.room_frame = Frame(self.master,
        bg = self.sch[1])

        # Number of Rooms Slider Label
        self.room_scale_label = Label(self.master,
        text = "Number of Rooms",
        font = self.sch["bigfont"],
        bg = self.sch[1],
        fg = self.sch[3])

        # Number of Rooms Slider
        self.room_var = DoubleVar()
        self.room_scale = Scale(self.room_frame,
            variable = self.room_var, 
            from_ = 5,
            to = 250,
            resolution = 5, 
            length = 500,
            sliderlength = 10,
            width = 20,
            bg = self.sch[1],
            troughcolor = self.sch[2],
            fg = self.sch[3],
            orient = HORIZONTAL) 

        # Number of Rooms Randomizer
        self.room_scale_random = Button(self.room_frame,
            text = "Random",
            fg = 'black',
            command = lambda e=1: self.randomRoomScale(e),
            font = self.sch['bigfont'],
            highlightbackground=self.sch[1])

        # People Frame
        self.people_frame = Frame(self.master,
        bg = self.sch[1])

        # Number of People Slider Label
        self.people_scale_label = Label(self.master,
        text = "Number of People",
        font = self.sch["bigfont"],
        bg = self.sch[1],
        fg = self.sch[3])

        # Number of People Slider
        self.people_var = DoubleVar()
        self.people_scale = Scale(self.people_frame,
            variable = self.people_var, 
            from_ = 5,
            to = 250,
            resolution = 5, 
            length = 500,
            width = 20,
            sliderlength = 10,
            bg = self.sch[1],
            troughcolor = self.sch[2],
            fg = self.sch[3],
            orient = HORIZONTAL) 

        # Number of Rooms Randomizer
        self.people_scale_random = Button(self.people_frame,
            text = "Random",
            fg = 'black',
            command = lambda e=1: self.randomPeopleScale(e),
            font = self.sch['bigfont'],
            highlightbackground=self.sch[1])

        self.submit_button = Button(self.master,
            text = "Continue",
            fg = 'black',
            highlightbackground=self.sch[1],
            font = self.sch['bigfont'],
            command = lambda e=1: self.submitData(e))

        self.logo.pack()

        self.introlabel.pack()

        self.room_scale_label.pack()
        self.room_scale.grid(row=0,column=0)
        self.room_scale_random.grid(row=0,column=1,pady=(20,0))
        self.room_frame.pack()

        self.people_scale_label.pack()
        self.people_scale.grid(row=0,column=0)
        self.people_scale_random.grid(row=0,column=1,pady=(20,0))
        self.people_frame.pack()

        self.submit_button.pack()

    def randomRoomScale(self,e):
        del e
        self.room_scale.set(random.randrange(5,250))
        self.master.update()

    def randomPeopleScale(self,e):
        del e
        self.people_scale.set(random.randrange(5,250))
        self.master.update()

    def submitData(self, e):
        del e
        self.parent.submit_data(self)
        

    def clear(self):
        for widget in self.master.winfo_children():
            widget.destroy()