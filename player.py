class Player():
    def __init__(self):
        self.guesses = []

    def make_player_guess(self):
        guessing = True
        while guessing:
            x = int(input("Guess x-coordinate: ")) - 1
            y = int(input("Guess y-coordinate: ")) - 1
            if 0 <= x <= 9 and 0 <= y <= 9:
                if (x, y) not in self.guesses:
                    self.guesses.append((x, y))
                    guessing = False
                    return (x, y)
                else:
                    print("\nAlready guessed. Please pick again.\n")
            else:
                print("\nLearn how to count, idiot")
