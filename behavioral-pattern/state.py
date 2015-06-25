#! /usr/bin/python


class State(object):

    """Base state. This is to share functionality"""

    def scan(self):
        """Scan the dial to the next station"""
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Scanning... Station is", self.stations[self.pos], self.name)


class AmState(State):
    """
    ConcreteStateA
    """
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle(self):
        print("Switching to FM")
        self.radio.state = self.radio.fmstate


class FmState(State):
    """
    ConcreteStateB
    """

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle(self):
        print("Switching to AM")
        self.radio.state = self.radio.amstate


class Radio(object):
    """
    context class
    """
    def __init__(self):
        """We have an AM state and an FM state"""
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle(self):
        self.state.toggle()

    def scan(self):
        self.state.scan()


# Test our radio out
if __name__ == '__main__':
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle] + [radio.scan] * 2
    actions *= 2

    for action in actions:
        action()
