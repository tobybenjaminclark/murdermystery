from tkinter import *
import random
from turtle import xcor

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
        self.program = parent.program
        self.logoimg = PhotoImage(file = "Scriptbank/Logo.gif")
        self.logoimgsmall = PhotoImage(file = "Scriptbank/LogoSmall.gif")
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
        
    def makeTopBar(self):
        
        self.top_frame = Frame(self.master,
        bg = self.sch[1])
        
        self.logo = Label(self.top_frame,
        image = self.logoimgsmall)

        self.exit_button = Button(self.top_frame,
        text = "Exit1",
        bg = self.sch[1],
        highlightbackground=self.sch[1],
        font = self.sch['bigfont'],
        width=30,
        command = lambda e=0:self.Quit(e))

        self.exit_button2 = Button(self.top_frame,
        text = "Exit2",
        bg = self.sch[1],
        highlightbackground=self.sch[1],
        font = self.sch['bigfont'],
        width=30,
        command = lambda e=0:self.Quit(e))

        self.exit_button3 = Button(self.top_frame,
        text = "Exit3",
        bg = self.sch[1],
        highlightbackground=self.sch[1],
        font = self.sch['bigfont'],
        width=30,
        command = lambda e=0:self.Quit(e))

        self.exit_button4 = Button(self.top_frame,
        text = "Exit4",
        bg = self.sch[1],
        highlightbackground=self.sch[1],
        font = self.sch['bigfont'],
        width=30,
        command = lambda e=0:self.Quit(e))

        self.logo.grid(row=0,column=0)
        self.exit_button.grid(row=0,column=1)
        self.exit_button2.grid(row=0,column=2)
        self.exit_button3.grid(row=0,column=3)
        self.exit_button4.grid(row=0,column=4)    

    def Quit(self,e):
        self.master.destroy()
        quit()

    def makeCanvas(self):
    
        self.canvasFrame = Frame(self.rightmaster,
        bg = self.sch[1])

        self.canvasFrame2 = Frame(self.canvasFrame,
        bg = self.sch[1])

        time_buttons = []
        
        for x in range(0,5):
            time_buttons.append(Button(
                self.canvasFrame2,
                text = x,
                font = self.sch['bigfont'],
                highlightbackground=self.sch[1]
            ))
        
        for x in range(0, len(time_buttons)):
             time_buttons[x].grid(row=0,column=x)
        canvascolspan = x

        self.canvas = Canvas(self.canvasFrame,
        width = 600, height = 500)

        # filling canvas with locations
        currentx = 10
        currenty = 10
        coords = []
        location_objects = []
        locations = self.program.generator.rooms
        for l in locations:
            txt = l.roomName + " " + str(l.id)
            foo = self.canvas.create_oval(currentx,currenty,currentx+45,currenty+45,fill=self.sch[5])
            location_objects.append(foo)
            currenty += 55
            if currenty > (55*8)+10:
                currenty=10
                currentx+=55

        self.canvasFrame2.pack()
        self.canvas.pack()

    def makeLowerInfoPanel(self):
        
        self.lower_infopanel = Frame(self.rightmaster,
        bg = self.sch[1])

        people_buttons = []
        for x in range(0,5):
            people_buttons.append(Button(
                self.lower_infopanel,
                text = ("Person"+str(x)),
                font = self.sch['bigfont'],
                highlightbackground=self.sch[1]
            ))
            people_buttons[x].grid(row=0,column=x)
        
    def makeLeftInfoPanel(self):
        self.leftinfoframe = Frame(self.master,
        bg = self.sch[1])

        self.infolabel = Label(self.leftinfoframe,
        text = "Name: Fuck\nOccupation:Imposter",
        font = self.sch['bigfont'],
        bg = self.sch[1],
        fg = self.sch[3])
        self.infolabel.pack()



    def display_main(self):

        self.rightmaster = Frame(self.master,
        bg = self.sch[1])

        self.makeLowerInfoPanel()
        self.makeTopBar()
        self.makeCanvas()
        self.makeLeftInfoPanel()

        self.top_frame.grid(row=0,column=0,columnspan=2)
        self.canvasFrame.pack()
        self.lower_infopanel.pack()
        self.rightmaster.grid(row=1,column=1)
        self.leftinfoframe.grid(row=1,column=0 )

        self.master.update()

    def clear(self):
        for widget in self.master.winfo_children():
            widget.destroy()