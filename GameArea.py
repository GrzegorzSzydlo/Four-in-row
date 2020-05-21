from tkinter import Frame, Canvas, LEFT, TOP, BOTTOM
from ActionGame import *

ROW_COUNT = 6
COLUMN_COUNT = 7

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600


class GameArea:

    def __init__(self, master):
        self.master = master
        self.action = ActionGame()
        self.table = self.action.createTablica()
        self.action.wypiszTablice(self.table)

    def frame_game(self):
        frame_main = Frame(self.master)
        frame1 = Frame(frame_main)
        self.canvas1 = Canvas(frame1, width=WINDOW_WIDTH, height=float((1 / 7) * WINDOW_HEIGHT),
                              background="blue")
        self.canvas1.place(x=0, y=0)
        self.canvas1.pack()
        frame1.pack(side=TOP)

        frame2 = Frame(frame_main)
        self.canvas2 = Canvas(frame2, width=WINDOW_WIDTH, height=float((6 / 7) * WINDOW_HEIGHT),
                              background="Green")
        self.canvas2.place(x=0, y=0)
        self.canvas2.pack()
        frame2.pack(side=TOP)

        frame_main.pack(side=LEFT)

        self.action.draw_circle(self.table, self.canvas2)
        self.canvas2.bind('<Button-1>', lambda e: self.action.game(self.table, self.canvas2, e))
