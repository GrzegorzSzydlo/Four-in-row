import math
import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600


class ActionGame:
    turn = 0
    gameover = False

    def createTablica(self):
        tablica = np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)
        return tablica

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

    def game(self, tab, canvas, event):
        if not self.gameover:
            if self.turn == 0:
                column = int(math.floor(event.x / (WINDOW_WIDTH / 7)))
                if self.wybranaLokalizacja(tab, column):
                    row = self.kolejnyDostepnyWiersz(tab, column)
                    self.ustawRuch(tab, row, column, 1)
                    self.wypiszTablice(tab)
                    self.draw_circle(tab, canvas)

                    if self.wygrywajacyRuch(tab, 1):
                        print("Wygrywa gracz: {}".format("Player 2"))
                        self.gameover = True

            else:
                column = int(math.floor(event.x / (WINDOW_WIDTH / 7)))
                if self.wybranaLokalizacja(tab, column):
                    row = self.kolejnyDostepnyWiersz(tab, column)
                    self.ustawRuch(tab, row, column, 2)
                    self.wypiszTablice(tab)
                    self.draw_circle(tab, canvas)
                    if self.wygrywajacyRuch(tab, 2):
                        print("Wygrywa gracz: {}".format("Player 2"))
                        self.gameover = True

        self.turn = (self.turn + 1) % 2

    def draw_circle(self, table, canvas2):
        for column in range(COLUMN_COUNT):
            for row in range(ROW_COUNT):
                if table[ROW_COUNT - row - 1][column] == 0:
                    canvas2.create_oval((column * (WINDOW_HEIGHT / 7.0)), (row * (WINDOW_WIDTH / 7)),
                                        ((WINDOW_HEIGHT / 7.0) + column * (WINDOW_WIDTH / 7)),
                                        ((WINDOW_HEIGHT / 7.0) + row * (WINDOW_WIDTH / 7.0)),
                                        fill="black")
                if table[ROW_COUNT - row - 1][column] == 1:
                    canvas2.create_oval((column * (WINDOW_HEIGHT / 7.0)), (row * (WINDOW_WIDTH / 7)),
                                        ((WINDOW_HEIGHT / 7.0) + column * (WINDOW_WIDTH / 7)),
                                        ((WINDOW_HEIGHT / 7.0) + row * (WINDOW_WIDTH / 7.0)),
                                        fill="red")

                if table[ROW_COUNT - row - 1][column] == 2:
                    canvas2.create_oval((column * (WINDOW_HEIGHT / 7.0)), (row * (WINDOW_WIDTH / 7)),
                                        ((WINDOW_HEIGHT / 7.0) + column * (WINDOW_WIDTH / 7)),
                                        ((WINDOW_HEIGHT / 7.0) + row * (WINDOW_WIDTH / 7.0)),
                                        fill="Yellow")
