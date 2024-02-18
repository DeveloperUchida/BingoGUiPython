import tkinter as tk


class BingoGUI:
    def __init__(self, master):
        self.master = master
        master.title("Bingo Game")

        self.b = [
            [5, 5, 5, 1, 3],
            [3, 5, 5, 3, 1],
            [4, 3, 3, 2, 1],
            [4, 0, 1, 0, 1],
            [1, 2, 2, 0, 2]
        ]
        self.players = {'a': set(), 'b': set(), 'c': set(), 'd': set()}
        self.player_names = {'a': 'player A',
                             'b': 'player B', 'c': 'player C', 'd': 'player D'}

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=0, column=0, columnspan=5)

        self.buttons = []
        for i in range(5):
            for j in range(5):
                btn = tk.Button(master, text=self.b[i][j], width=5, height=2,
                                command=lambda row=i, col=j: self.button_click(row, col))
                btn.grid(row=i+1, column=j)
                self.buttons.append(btn)

    def button_click(self, row, col):
        number = self.b[row][col]
        for player, card in self.players.items():
            if number in card:
                card.remove(number)
                if self.check_bingo(card):
                    self.result_label.config(
                        text=f"Bingo!! {self.player_names[player]} wins!")
                    for btn in self.buttons:
                        btn.config(state=tk.DISABLED)
                    return

    def check_bingo(self, card):
        lines = [
            card,  # Horizontal
            {self.b[i][j]
                for i in range(5) for j in range(5) if j == i},  # Diagonal 1
            {self.b[i][j] for i in range(5) for j in range(
                5) if j == 4 - i},  # Diagonal 2
        ]
        for line in lines:
            if len(line) == 0:
                return True
        return False


root = tk.Tk()
app = BingoGUI(root)
root.mainloop()
