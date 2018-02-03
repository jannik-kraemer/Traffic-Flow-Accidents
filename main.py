# Main File
import sys
# from appJar import gui
import modules.interface as interface


if __name__ == '__main__':

    app = interface.UI("Test", "640x480")
    interface.Navigation()
    app.render()