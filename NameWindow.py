from tkinter import *

WINDOW_HEIGHT = 100
WINDOW_WIDTH = 250


class NameWindow:
    player1 = "Player 1"
    player2 = "Player 2"
    entry_player1 = ""
    entry_player2 = ""

    def __init__(self, parent, label1, label2):
        self.parent = parent
        self.label1 = label1
        self.label2 = label2

    #Tworzenie drugiego okna
    def name_window(self):
        child = Toplevel(self.parent)
        child.title("Zmiana imion")
        child.resizable(width=False, height=False)

        screen_width = child.winfo_screenwidth()
        screen_height = child.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (WINDOW_WIDTH / 2))
        y_cordinate = int((screen_height / 2) - (WINDOW_HEIGHT / 2))
        child.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH, WINDOW_HEIGHT, x_cordinate, y_cordinate))

        self.frame_description(child)
        self.button_ok(child)

        child.mainloop()

    #Pobranie imion graczy
    def frame_description(self, master):
        frame = Frame(master)
        frame_player1 = Frame(frame)
        label_player1 = Label(frame_player1, text="Player 1")
        label_player1.pack(side=LEFT)
        self.entry_player1 = Entry(frame_player1, width=30)
        self.entry_player1.pack(side=LEFT)
        frame_player1.pack(side=TOP)

        frame_player2 = Frame(frame)
        label_player2 = Label(frame_player2, text="Player 2")
        label_player2.pack(side=LEFT)
        self.entry_player2 = Entry(frame_player2, width=30)
        self.entry_player2.pack(side=LEFT)
        frame_player2.pack(side=TOP)

        frame.pack()

    def button_ok(self, master):
        frame = Frame(master)
        button = Button(frame, text="OK", command=lambda: self.on_ok_button(master))
        button.pack()
        frame.pack(side=TOP)

    def zmiana_imienia(self, name1, name2):
        self.label1.configure(text=name1.get())
        self.label2.configure(text=name2.get())

    def on_ok_button(self, master):
        self.zmiana_imienia(self.entry_player1, self.entry_player2)
        master.destroy()
