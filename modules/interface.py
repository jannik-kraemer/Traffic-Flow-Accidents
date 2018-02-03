#
from appJar import gui

class UI():

    def __init__(self, title = "SimpleText", size="640x480"):
        # Creates app env.
        self.app = gui(title, size)
        # Adds object to widget
        self.createLabel()

    def createLabel(self):
        self.app.addLabel("test", "This is a test")

    def render(self):
        # Runs everything
        self.app.go()
        # Don't put sth down here

