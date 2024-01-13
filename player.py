class Player():
    def __init__(self):
        self.guesses = []


    def verify_coord(self, coord):
        # verifies coord is a digit between 1 and 10
        try:
            coord = int(coord)
            if 1 <= coord <= 10:
                coord = int(coord) - 1
                return coord
            else:
                print("\nBetween 1 and 10, please.\n")
        except ValueError:
            print("\nThat's not a number, silly.\n")


    def make_player_guess(self):
        guessing = True
        # loops through until valid, unguessed guess is made
        while guessing:
            while True:
                # loops until x is a digit between 1 and 10
                x = input("Guess x-coordinate: ")
                x = self.verify_coord(x)
                if x != None:
                    break
            while True:
                # loops until y is a digit between 1 and 10
                y = input("Guess y-coordinate: ")
                y = self.verify_coord(y)
                if y != None:
                    break
            if (x, y) not in self.guesses:
                self.guesses.append((x, y))
                guessing = False
                return (x, y)
            else:
                print("\nAlready guessed. Please pick again.\n")
