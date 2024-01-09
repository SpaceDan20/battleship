class Board():
    def __init__(self):
        self.board = [['O' for _ in range(10)] for _ in range(10)]
        print(self)

    def show_board(self):
        # Prints current self.board (10x10 grid with sea spaces and any ships)
        print("")
        for row in self.board:
            print(" ".join(row))


    def place_bow(self, ship, x, y):
        # takes ship, x, and y and to place bow of ship
        self.board[y][x] = ship.letter


    def place_rest_of_ship(self, ship, orientation, x, y):
        # takes ship, x, y, and orientation to place rest of ship on board
        for i in range(ship.size):
            if orientation == "left":
                self.board[y][x-i] = ship.letter
            elif orientation == "right":
                self.board[y][x+i] = ship.letter
            elif orientation == "up":
                self.board[y-i][x] = ship.letter
            elif orientation == "down":
                self.board[y+i][x] = ship.letter
