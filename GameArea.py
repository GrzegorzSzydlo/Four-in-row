from tkinter import Frame, Canvas, LEFT
from ActionGame import *

ROW_COUNT = 6
COLUMN_COUNT = 7

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600


class GameArea:

    def __init__(self, master, logic):
        self.master = master
        self.action = ActionGame(logic)
        self.table = self.action.initialize_table()

    def frame_game(self):
        """Tworzenie obszaru gry"""
        frame_main = Frame(self.master, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        frame1 = Frame(frame_main)
        canvas1 = Canvas(frame1, width=WINDOW_WIDTH, height=float((1 / 7) * WINDOW_HEIGHT),
                         background="blue")
        canvas1.place(x=0, y=0)
        canvas1.pack()
        frame1.pack(side=TOP)

        frame2 = Frame(frame_main)
        canvas2 = Canvas(frame2, width=WINDOW_WIDTH, height=float((6 / 7) * WINDOW_HEIGHT),
                         background="Green")
        canvas2.place(x=0, y=0)
        canvas2.pack()
        frame2.pack(side=TOP)

        frame_main.pack(side=LEFT)

        self.action.draw_circle(self.table, canvas2)
        self.action.one_circle(canvas1)
        self.action.reset_button(self.table, canvas1, canvas2)

        canvas1.bind('<Button-1>', lambda e: self.action.game(self.table, canvas1, canvas2, e))
        canvas2.bind('<Button-1>', lambda e: self.action.game(self.table, canvas1, canvas2, e))
        canvas1.bind('<Motion>', lambda e: self.action.move_circle(canvas1, e))
        canvas2.bind('<Motion>', lambda e: self.action.move_circle(canvas1, e))
