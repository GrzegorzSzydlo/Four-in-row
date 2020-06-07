from tkinter import *
from UserInterface import UserInterface


class Main:
    master = Tk()

    def __init__(self):
        t = UserInterface()
        t.main_window(self.master)


def __main__():
    Main()


if __name__ == '__main__':
    Main()
