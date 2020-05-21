from tkinter import *
from NameWindow import NameWindow
from GameArea import *

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 850


class Interface:
    label_player1 = ""
    label_player2 = ""

    # Tworzenie okna głównego
    def main_window(self, master):
        master.title("For in row")
        master.resizable(width=False, height=False)

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - WINDOW_WIDTH / 2)
        y_coordinate = int((screen_height / 2) - WINDOW_HEIGHT / 2)
        master.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, x_coordinate, y_coordinate))

        frame1 = Frame(master, width=WINDOW_WIDTH - 150, height=WINDOW_HEIGHT, background="Blue")
        frame2 = Frame(master, width=150, height=WINDOW_HEIGHT, background="Green")

        self.change_name_button(frame2)
        self.name_label(frame2)

        frame1.pack(side=LEFT)
        frame2.pack(side=RIGHT)


        g = GameArea(frame1)
        g.frame_game()



        master.mainloop()

    # Przycisk na zmianę imienia
    def change_name_button(self, master):
        frame = master
        button = Button(frame, text="Zmiana imienia", command=lambda: self.on_name_button(master))
        button.pack()
        frame.pack(side=RIGHT)

    # Akcja jaka odbywa się po wciśnięciu przycisku name_button
    def on_name_button(self, master):
        window = NameWindow(master, self.label_player1, self.label_player2)
        window.name_window()

    # Ramkia z imionami graczy
    def name_label(self, master):
        player_name = master
        self.label_player1 = Label(player_name, text="Player 1", foreground="Red")
        self.label_player1.pack(side=LEFT)
        self.label_player2 = Label(player_name, text="Player 2", foreground="Orange")
        self.label_player2.pack(side=RIGHT)
        player_name.pack(side=TOP)
