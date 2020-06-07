from tkinter import *
from GameArea import GameArea
from LogicArea import LogicArea

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 750


class UserInterface:

    def main_window(self, master):
        """Tworzenie okna głównego"""
        master.title("For in row")
        master.resizable(width=False, height=False)

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - WINDOW_WIDTH / 2)
        y_coordinate = int((screen_height / 2) - WINDOW_HEIGHT / 2)
        master.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, x_coordinate, y_coordinate))

        frame1 = Frame(master, width=WINDOW_WIDTH - 150, height=WINDOW_HEIGHT, background="Blue")
        frame2 = Frame(master, width=150, height=WINDOW_HEIGHT, background="#ffffff")

        frame1.pack(side=LEFT)
        frame2.pack(side=LEFT)

        logic = LogicArea(frame2)
        logic.logic_main()

        g = GameArea(frame1, logic)
        g.frame_game()

        master.mainloop()
