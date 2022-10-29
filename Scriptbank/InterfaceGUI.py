from .GUI import GUI

class InterfaceGUI():

    def __init__(self, program):

        self.program = program
        self.mastergui = GUI(self)

    def submit_data(self, gui):

        room_count = gui.room_scale.get()
        people_count = gui.people_scale.get()
        self.program.generate(room_count, people_count)

        gui.clear()