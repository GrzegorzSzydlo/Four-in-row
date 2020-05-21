from tkinter import *
from Interface import Interface
from GameArea import GameArea


class Main:
    master = Tk()

    def __init__(self):
        t = Interface()
        t.main_window(self.master)



def __main__():
    Main()


if __name__ == '__main__':
    Main()
