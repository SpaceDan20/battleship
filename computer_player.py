import random

class ComputerPlayer():
    def __init__(self):
        self.guesses = []
        self.choices = []
        self.recent_hit = ()


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
                orientation = self.find_and_choose_orientations(ship, board, coords[0], coords[1])
                board.place_ship(ship, orientation, coords[0], coords[1])
                break


    def make_random_guess(self):
        # loops through until random, unguessed coordinate is chosen
        guessing = True
        while guessing:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if (x, y) not in self.guesses:
                self.guesses.append((x, y))
                guessing = False
                return (x, y)
                
    
    def make_informed_guess(self):
        # loops through until informed, unguessed coordinate is chosen
        guessing = True
        while guessing:
            x = self.recent_hit[0]
            y = self.recent_hit[1]
            # finds adjacent sea spaces and populates self.choices with them
            self.choices = [(x + 1, y),
                        (x - 1, y),
                        (x, y + 1),
                        (x, y - 1)]
            # Loops through choices to make sure list only contains unchosen, adjacent coordinates
            for choice in self.choices.copy():
                if choice[0] in [-1, 10] or choice[1] in [-1, 10] or choice in self.guesses:
                    self.choices.remove(choice)
            # if choices isn't empty, selects one of them as the guess
            if self.choices:
                x, y = random.choice(self.choices)
                if (x, y) not in self.guesses:
                    self.guesses.append((x, y))
                    guessing = False
                    return (x, y)
            # if choices is empty, clears recent_hit and makes random guess
            else:
                self.recent_hit = ()
                guessing = False
                x, y = self.make_random_guess()
                return (x, y)
