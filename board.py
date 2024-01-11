class Board():
    def __init__(self, name):
        self.board = [['O' for _ in range(10)] for _ in range(10)]
        self.name = name

    def show_board(self):
        # Prints current self.board (10x10 grid with sea spaces and any ships)
        print("-------------------------")
        print(f"{self.name} Board:")
        for row in self.board:
            print(" ".join(row))
        print("-------------------------")


    def place_bow(self, ship, x, y):
        # takes ship, x, and y and to place bow of ship
        self.board[y][x] = ship.letter
        ship.coords.append((x, y))


    def place_rest_of_ship(self, ship, orientation, x, y):
        # takes ship, x, y, and orientation to place rest of ship on board
        for i in range(1, ship.size):
            if orientation == "left":
                self.board[y][x-i] = ship.letter
                ship.coords.append((x-i, y))
            elif orientation == "right":
                self.board[y][x+i] = ship.letter
                ship.coords.append((x+i, y))
            elif orientation == "up":
                self.board[y-i][x] = ship.letter
                ship.coords.append((x, y-i))
            elif orientation == "down":
                self.board[y+i][x] = ship.letter
                ship.coords.append((x, y+i))

    def check_if_clear(self, ship, orientation, x, y):
        spaces_to_fill = []
        for i in range(1, ship.size):
            if orientation == "left":
                spaces_to_fill.append(self.board[y][x-i])
            elif orientation == "right":
                spaces_to_fill.append(self.board[y][x+i])
            elif orientation == "up":
                spaces_to_fill.append(self.board[y-i][x])
            elif orientation == "down":
                spaces_to_fill.append(self.board[y+i][x])
        # returns false if any of the spaces to fill equal ship letters
        if any(letter != 'O' for letter in spaces_to_fill):
            return False
        else:
            return True
