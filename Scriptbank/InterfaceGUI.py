from .GUI import GUI

class InterfaceGUI():

    def __init__(self, program):

        self.program = program
        self.gui = GUI()

    def submit_data(self):

        room_count = self.gui.room_scale.get()
        people_count = self.gui.people_scale.get()
        self.program.generate(room_count, people_count)

        self.gui.clear()