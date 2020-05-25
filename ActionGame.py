import math
from tkinter import Button, S, ALL, TOP

import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

SIZE_H = WINDOW_HEIGHT / 7
SIZE_W = WINDOW_WIDTH / 7


class ActionGame:
    turn = 0
    gameover = False
    coord = []
    id_circle = 0

    def __init__(self, logic):
        self.logic = logic

    def createTablica(self):
        table = np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)
        return table

    def wypiszTablice(self, tab):
        print(np.flip(tab, 0))

    def ustawRuch(self, tab, row, col, kto):
        tab[row][col] = kto

    def wybranaLokalizacja(self, tab, col):
        return tab[ROW_COUNT - 1][col] == 0

    def kolejnyDostepnyWiersz(self, tab, col):
        for r in range(ROW_COUNT):
            if tab[r][col] == 0:
                return r

    def wygrywajacyRuch(self, tab, kto):
        # sprawdzam w poziomie
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if tab[r][c] == kto and tab[r][c + 1] == kto \
                        and tab[r][c + 2] == kto and tab[r][c + 3] == kto:
                    return True

        # sprawdzam w pionowie
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if tab[r][c] == kto and tab[r + 1][c] == kto \
                        and tab[r + 2][c] == kto and tab[r + 3][c] == kto:
                    return True

        # sprawdzam przekątną dodatnią
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if tab[r][c] == kto and tab[r + 1][c + 1] == kto \
                        and tab[r + 2][c + 2] == kto \
                        and tab[r + 3][c + 3] == kto:
                    return True

        # sprawdzam przekątną ujemną
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if tab[r][c] == kto and tab[r - 1][c + 1] == kto \
                        and tab[r - 2][c + 2] == kto and \
                        tab[r - 3][c + 3] == kto:
                    return True

    def game(self, tab, canvas1, canvas2, event):
        if not self.gameover:
            if self.turn == 0:
                column = int(math.floor(event.x / SIZE_W))
                if self.wybranaLokalizacja(tab, column):
                    row = self.kolejnyDostepnyWiersz(tab, column)
                    self.ustawRuch(tab, row, column, 1)
                    self.wypiszTablice(tab)
                    self.draw_circle(tab, canvas2)

                    if self.wygrywajacyRuch(tab, 1):
                        self.winner(canvas1, self.logic.label_player1["text"])
                        self.gameover = True
                else:
                    self.turn -= 1

            else:
                column = int(math.floor(event.x / SIZE_W))
                if self.wybranaLokalizacja(tab, column):
                    row = self.kolejnyDostepnyWiersz(tab, column)
                    self.ustawRuch(tab, row, column, 2)
                    self.wypiszTablice(tab)
                    self.draw_circle(tab, canvas2)

                    if self.wygrywajacyRuch(tab, 2):
                        self.winner(canvas1, self.logic.label_player2["text"])
                        self.gameover = True
                else:
                    self.turn -= 1

        self.color_circle(canvas1)
        self.turn = (self.turn + 1) % 2
        self.draw(tab, canvas1)

    def draw_circle(self, table, canvas2):
        canvas2.delete(ALL)
        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT):
                if table[ROW_COUNT - row - 1][column] == 0:
                    canvas2.create_oval((column * SIZE_H), (row * SIZE_W),
                                        (SIZE_H + column * SIZE_W),
                                        (SIZE_H + row * SIZE_W),
                                        fill="black")
                if table[ROW_COUNT - row - 1][column] == 1:
                    canvas2.create_oval((column * SIZE_H), (row * SIZE_W),
                                        (SIZE_H + column * SIZE_W),
                                        (SIZE_H + row * SIZE_W),
                                        fill="red")

                if table[ROW_COUNT - row - 1][column] == 2:
                    canvas2.create_oval((column * SIZE_H), (row * SIZE_W),
                                        (SIZE_H + column * SIZE_W),
                                        (SIZE_H + row * SIZE_W),
                                        fill="Yellow")

    def one_circle(self, canvas1):
        self.id_circle = canvas1.create_oval(
            ((WINDOW_WIDTH / 2 - SIZE_W / 2), 0, (WINDOW_WIDTH / 2 + SIZE_W / 2), SIZE_H),
            fill="Red")
        self.coord = canvas1.coords(id)

    def color_circle(self, canvas):
        if self.turn == 1:
            canvas.itemconfig(self.id_circle, fill="red")
        if self.turn == 0:
            canvas.itemconfig(self.id_circle, fill="yellow")

    def move_circle(self, canvas, event):
        if not self.gameover:
            x, y = event.x, event.y
            canvas.coords(self.id_circle, (x - (SIZE_W / 2), 0, x + (SIZE_W / 2), SIZE_H))
            if self.turn == 0:
                canvas.itemconfig(self.id_circle, fill="red")
            if self.turn == 1:
                canvas.itemconfig(self.id_circle, fill="yellow")

    def winner(self, canvas, kto):
        canvas.delete(self.id_circle)
        canvas.create_text((WINDOW_WIDTH / 2, SIZE_H / 2), text=("Wygrywa: {}".format(kto)), fill="orange",
                           font=("Times new roman", 40))

    def draw(self, table, canvas):
        iter = 0
        for c in range(COLUMN_COUNT):
            if table[ROW_COUNT - 1][c] == 0:
                iter += 1

        if iter == 0:
            canvas.delete(self.id_circle)
            canvas.create_text((WINDOW_WIDTH / 2, SIZE_H / 2), text="Remis", fill="orange",
                               font=("Times new roman", 40))

    def reset_button(self, table, canvas1, canvas2):
        button = Button(self.logic.frame2, text="Reset", width=150, height=0,
                        command=lambda: self.on_reset_button(table, canvas1, canvas2))
        button.pack(side=TOP, pady=10)

    def on_reset_button(self, table, canvas1, canvas2):
        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT):
                table[row][column] = 0

        self.turn = 0
        self.gameover = False
        canvas1.delete(ALL)
        self.one_circle(canvas1)
        self.draw_circle(table, canvas2)
