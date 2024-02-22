import tkinter as tk
import tkinter.messagebox as messagebox
import random

class BingoGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Bingo Game")
        self.cards = []
        self.bingo_check = [[False]*5 for _ in range(5)]
        self.players = {'a': 'Player 1', 'b': 'Player 2', 'c': 'Player 3', 'd': 'Player 4'}
        self.create_widgets()
        self.generate_cards()

    def create_widgets(self):
        self.info_label = tk.Label(self.master, text="Click on a number to draw", font=("Arial", 12))
        self.info_label.grid(row=0, column=0, columnspan=5, pady=10)
        self.number_buttons = [[tk.Button(self.master, text=str(i*5 + j), width=5, height=2, command=lambda x=i, y=j: self.check_number(x, y)) for j in range(5)] for i in range(5)]
        for i in range(5):
            for j in range(5):
                self.number_buttons[i][j].grid(row=i+1, column=j, padx=5, pady=5)

    def generate_cards(self):
        for _ in range(4):
            card = [[random.randint(i*15+1, (i+1)*15) for _ in range(5)] for i in range(5)]
            self.cards.append(card)

    def check_number(self, row, col):
        number = self.cards[0][row][col]
        for i, card in enumerate(self.cards):
            for j in range(5):
                if card[row][j] == number:
                    self.bingo_check[i][j] = True
                if card[j][col] == number:
                    self.bingo_check[i][j] = True
            if all(self.bingo_check[i][j] for j in range(5)):  # horizontal bingo check
                self.handle_bingo(self.players['abcd'[i]])
                return
            if all(self.bingo_check[i][i] for i in range(5)):  # diagonal bingo check
                self.handle_bingo(self.players['abcd'[i]])
                return
            if all(self.bingo_check[i][4-i] for i in range(5)):  # reverse diagonal bingo check
                self.handle_bingo(self.players['abcd'[i]])
                return

    def handle_bingo(self, player):
        messagebox.showinfo("Bingo!", f"{player} got BINGO!")
        self.master.destroy()

root = tk.Tk()
bingo_game = BingoGame(root)
root.mainloop()
