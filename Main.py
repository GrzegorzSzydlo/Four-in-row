from tkinter import*

class Player:
    #name = ""
    #numer = 0
    def __init__(self,numer):
        self.numer = numer
        self.name = "Player {}".format(self.numer)

class Main:
    player1 = Player(1)
    player2 = Player(2)

    def __init__(self):
        self.master = Tk()
        self.master.title("Cztery w rzedzie")

        self.master.resizable(width=False, height=False)

        self.window_height = 550
        self.window_width = 600
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (self.window_width / 2))
        y_cordinate = int((screen_height / 2) - (self.window_height / 2))
        self.master.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x_cordinate, y_cordinate))


        nameButton = Button(self.master, text="Zmiana imienia", command=self.onButton)
        nameButton.pack()

        self.PlayerName = Frame(self.master)
        self.labelPlayer1 = Label(self.PlayerName, text = self.player1.name)
        self.labelPlayer1.pack()
        self.labelPlayer2 = Label(self.PlayerName, text = self.player2.name)
        self.labelPlayer2.pack()
        self.PlayerName.pack(side = TOP)


    def onButton(self):
        self.child = Toplevel(self.master)
        self.child.title("Imiona")
        self.child.resizable(width=False, height=False)

        window_height = 100
        window_width = 250
        screen_width = self.child.winfo_screenwidth()
        screen_height = self.child.winfo_screenheight()
        x_cordinate = int((screen_width / 2) - (window_width / 2))
        y_cordinate = int((screen_height / 2) - (window_height / 2))
        self.child.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        self.windowFrame = Frame(self.child)

        self.description1 = Frame(self.windowFrame, height = 20, width = 40)
        self.labelP1 = Label(self.description1, text="Player 1:")
        self.labelP1.pack(side = LEFT)
        self.entry1 = Entry(self.description1, width=30)
        self.entry1.pack(side = LEFT)
        self.description1.pack(side = TOP)

        self.description2 = Frame(self.windowFrame, height=20, width=40)
        self.labelP2 = Label(self.description2, text="Player 2:")
        self.labelP2.pack(side=LEFT)
        self.entry2 = Entry(self.description2, width=30)
        self.entry2.pack(side=LEFT)
        self.description2.pack(side = TOP)

        self.buttonFrame = Frame(self.windowFrame,height=40, width=40)
        self.changeName = Button(self.buttonFrame, text="OK", command=self.onNameButton)
        self.changeName.pack()
        self.buttonFrame.pack()

        self.windowFrame.pack()



    def onNameButton(self):
        self.labelPlayer1.configure(text = self.entry1.get())
        self.labelPlayer2.configure(text = self.entry2.get())
        self.child.destroy()


    def run(self):
        self.master.mainloop()





#***************Main***********************#
glowne = Main()
glowne.run()
