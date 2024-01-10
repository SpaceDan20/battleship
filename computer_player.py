import random

class ComputerPlayer():
    def __init__(self):
        self.guesses = []

    def generate_coords(self):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        return [x, y]
    
    def find_and_choose_orientations(self, ship, board, x, y):
        # Takes x and y coordinates and ship size to determine possible orientations
        possible_orientations = []
        if y - ship.size + 1 >= 0:
            if board.check_if_clear(ship, "up", x, y):
                possible_orientations.append("up")
        if y + ship.size - 1 <= 9:
            if board.check_if_clear(ship, "down", x, y):
                possible_orientations.append("down")
        if x - ship.size + 1 >= 0:
            if board.check_if_clear(ship, "left", x, y):
                possible_orientations.append("left")
        if x + ship.size - 1 <= 9:
            if board.check_if_clear(ship, "right", x, y):
                possible_orientations.append("right")
        chosen_orientation = random.choice(possible_orientations)
        return chosen_orientation

    def place_computer_boat(self, ship, board):
        # Loops through while generating coords so ships aren't placed on top of each other.
        placing = True
        while placing:
            coords = self.generate_coords()
            if board.board[coords[1]][coords[0]] == "O":
                board.place_bow(ship, coords[0], coords[1])
                orientation = self.find_and_choose_orientations(ship, board, coords[0], coords[1])
                board.place_rest_of_ship(ship, orientation, coords[0], coords[1])
                break

    def make_computer_guess(self):
        # loops through to generate random coordinate guess not already chosen
        guessing = True
        while guessing:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if (x, y) not in self.guesses:
                self.guesses.append((x, y))
                guessing = False
                return (x, y)
