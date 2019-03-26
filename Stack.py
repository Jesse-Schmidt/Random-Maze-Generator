from Pieces import *
import random

class myStack:
    def __init__(self, last_frame, data = Four_Way_Cross()):
        self.last_frame = last_frame
        self.next_frame = 0
        self.data = data
        self.directions_to_go = data.get_open()
        self.directions_gone = []
        self.completed = False
        self.end = False
        self.start = True
        self.location = (0,0)

    def get_last_frame(self):
        return self.last_frame

    def get_data(self):
        return self.data

    def set_data(self, newData):
        self.data = newData
        self.directions_to_go = self.data.get_open()
        self.directions_gone = []

    def set_completed(self):
        self.completed = True

    def set_end(self):
        self.end = True

    def get_end(self):
        return self.end

    def set_start(self):
        self.start = True

    def get_start(self):
        return self.start

    def get_location(self):
        return self.location

    def set_location(self, newLocation):
        self.location = newLocation

    def get_completed(self):
        return self.completed

    def get_directions_gone(self):
        return self.directions_gone

    def get_next_frame(self):
        return self.next_frame

    def set_next_frame(self, newFrame):
        self.next_frame = newFrame

    def choose_direction(self):
        if len(self.directions_to_go) > 0:
            choice = random.choice(self.directions_to_go)
            self.directions_to_go.remove(choice)
            self.directions_gone.append(choice)
            return choice
        else:
            return 0

    def edit_direction(self, direction):
        self.directions_to_go.append(direction)
        self.directions_gone. remove(direction)

    def check(self, other):
        while other.get_last_frame() != 0:
            if self.get_location() == other.get_location():
                return True
            else:
                other = other.get_last_frame()
        return False

    def check_done(self):
        if self.data.any_open():
            self.directions_to_go = self.data.get_open()
            self.directions_gone = []
            return False
        else:
            return True

