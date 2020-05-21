from tkinter import *
from NameWindow import NameWindow

WINDOW_HEIGHT = 700
WINDOW_WIDTH = 600


class Interface:
    label_player1 = ""
    label_player2 = ""

    def main_window(self, master):
        master.title("For in row")
        master.resizable(width=False, height=False)

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - WINDOW_WIDTH / 2)
        y_coordinate = int((screen_height / 2) - WINDOW_HEIGHT / 2)
        master.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, x_coordinate, y_coordinate))

        self.change_name_button(master)
        self.name_label(master)

        master.mainloop()

    def change_name_button(self, master):
        frame = Frame(master)
        button = Button(frame, text="Zmiana imienia", command=lambda: self.on_name_button(master))
        button.pack()
        frame.pack(side=TOP)

    def on_name_button(self, master):
        window = NameWindow(master, self.label_player1, self.label_player2)
        window.name_window()

    def name_label(self, master):
        player_name = Frame(master)
        self.label_player1 = Label(player_name, text="Player 1")
        self.label_player1.pack(side=LEFT)
        self.label_player2 = Label(player_name, text="Player 2w")
        self.label_player2.pack(side=RIGHT)
        player_name.pack(side=TOP)
        master.update()
