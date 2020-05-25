from tkinter import *
from NameWindow import NameWindow

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 150


class LogicArea:
    label_player1 = Label
    label_player2 = Label
    frame1 = Frame
    frame2 = Frame

    def __init__(self, frame):
        self.frame = frame

    def logic_main(self):
        self.frame1 = Frame(self.frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT * 0.75, background="#ffffff")
        self.frame1.pack(side=TOP, pady=80)
        self.frame2 = Frame(self.frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT * 0.25, background="#ffffff")
        self.frame2.pack(side=BOTTOM, pady=25)

        self.name_label(self.frame1)
        self.change_name_button(self.frame1, self.frame2)

        self.quit_button(self.frame2)

    # Przycisk na zmianę imienia
    def change_name_button(self, frame1, frame2):
        button = Button(frame2, text="Zmiana imienia", width=WINDOW_WIDTH, height=2, command=lambda: self.on_name_button(frame1))
        button.pack(side=TOP, pady=10)

    # Akcja jaka odbywa się po wciśnięciu przycisku name_button
    def on_name_button(self, master):
        window = NameWindow(master, self.label_player1, self.label_player2)
        window.name_window()

    # Ramka z imionami graczy
    def name_label(self, master):
        label1 = Label(master, text="Player 1", width=WINDOW_WIDTH, height=2, font=("Times new roman", 20),
                       background="#ffffff")
        label1.pack(side=TOP)
        self.label_player1 = Label(master, text="Player 1", foreground="Red", width=WINDOW_WIDTH, height=2,
                                   font=("Times new roman", 15),
                                   background="#ffffff")
        self.label_player1.pack(side=TOP)

        label2 = Label(master, text="Player 2", width=WINDOW_WIDTH, height=2, font=("Times new roman", 20),
                       background="#ffffff")
        label2.pack(side=TOP)
        self.label_player2 = Label(master, text="Player 2", foreground="Orange", width=WINDOW_WIDTH, height=2,
                                   font=("Times new roman", 15),
                                   background="#ffffff")
        self.label_player2.pack(side=TOP)

    def quit_button(self, frame2):
        button = Button(frame2, text="Quit", width=150, command=self.on_quit_button)
        button.pack(side=BOTTOM, pady=10)

    def on_quit_button(self):
        exit(0)
