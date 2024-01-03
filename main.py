import random
import time

class Ship:
  # Constructor
  def __init__(self, type):
    self.type = type
    self.ship_bounds = {"battleship": 3}
    self.coords = []

  def create_bounds(self, x, y):
    """Takes x and y coordinates and returns possible orientations ship can be built"""
    bounds = self.ship_bounds[self.type]
    print(f"These the mf bounds: {bounds}")
    possible_placements = ["up", "down", "left", "right"]
    if x < 4:
      possible_placements.remove("left")
    if x > 5:
      possible_placements.remove("right")
    if y < 4:
      possible_placements.remove("up")
    if y > 5:
      possible_placements.remove("down")
    return possible_placements

  def place_ship(self, x, y):
    """Takes x and y coordinates and calls create_bounds() function to determine possible placements. Asks player for orientation, then builds ship in that orientation."""
    player_board[y][x] = "S"
    possible_orientations = self.create_bounds(x, y)
    display_board(player_board)
    print("""\n
          This is your ship so far. It's the S surrounded by Os of water.
          That's right. We're constructing her out in the middle of the sea.
          Why? Cause we're insane. (and not very practical).
    """)
    placing = True
    while placing:
      chosen_orientation = input(f"You can create the rest of the ship in these orientations: {possible_orientations}. Which one do you want? ").lower()
      if chosen_orientation in possible_orientations:
        for i in range(5):
          if chosen_orientation == "left":
            player_board[y][x-i] = "S"
            player_battleship.coords.append((x-i, y))
          elif chosen_orientation == "right":
            player_board[y][x+i] = "S"
            player_battleship.coords.append((x+i, y))
          elif chosen_orientation == "up":
            player_board[y-i][x] = "S"
            player_battleship.coords.append((x, y-i))
          elif chosen_orientation == "down":
            player_board[y+i][x] = "S"
            player_battleship.coords.append((x, y+i))
        placing = False
      else:
        print("\nThat's not a valid option. Try again.")

def display_board(board):
  """
  Displays the game board

  Returns:
  list(board): A 10x10 grid where O represents empty sea spaces, X represents a hit, and - represents a miss
  """
  print("")
  for row in board:
    print(" ".join(row))


# Set up boards
player_board = [['O' for _ in range(10)] for _ in range(10)]

# Creating bow coordinates and 0-indexed coordinates of player's ship
print("Welcome to Battleship!")
x_cord = int(input("You get 1 battleship. Yeah... budget's tight this year. Where do you want her? Bow x-coordinate (1-10): "))
y_cord = int(input("Bow y-coordinate (1-10): "))
x = x_cord-1
y = y_cord-1

# Create player battleship and update board
player_battleship = Ship("battleship")
player_battleship.place_ship(x, y)

print("----------------------------------------------------")
print(f"These are your battleship's coordinates (they are 0-indexed):\n{player_battleship.coords}")
print("Don't know what 0-indexed means? Don't worry about it :)")
print("Player board:")
display_board(player_board)

print("""\nThis is your part of the sea. For now. The S's represent your ship.
Now, in a few seconds, watch in utter helplessness as the enemy computer barrages your
part of the sea with completely random strikes that you can't do anything about,
until your stupid new ship has sunk. The computer wants you OUT of this waterspace.
One day though... you may exact your sweet, sweet revenge.
For now, I don't know. Maybe duck?\n""")

user_input = input("Okay. You ready? Type 'ready' or 'not': ")
print("Doesn't matter! Here comes the AI shells!\n")
time.sleep(2)

plays = 0
while player_battleship.coords:
  picking = True
  while picking:
    random_x_cord = random.randint(0, 9)
    random_y_cord = random.randint(0, 9)
    current_pick = player_board[random_y_cord][random_x_cord]
    # loops through to make sure AI doesn't choose already shot sector
    if current_pick in ["O", "S"]:
      print(f"\n      {random_x_cord+1}, {random_y_cord+1}!")

      # AI hits battleship
      if current_pick == "S":

        player_board[random_y_cord][random_x_cord] = "X"
        print("      BOOM!")
        display_board(player_board)
        time.sleep(1)
        print(f"\nYeah mf!! Hit! Back to shooting off my shots at random.")
        player_battleship.coords.remove((random_x_cord, random_y_cord))
        time.sleep(1)

      # AI misses
      else:
        time.sleep(0.3)
        player_board[random_y_cord][random_x_cord] = "-"
        display_board(player_board)

      # updates after each time AI shoots
      plays += 1
      picking = False

print("Get SUNK mf!")

if plays > 75:
  print(f"\nIt took the AI {plays} turns to sink your battleship. What an idiot. Anyway, thanks for playing. Better luck next time.")
else:
  print(f"\nIt took the AI {plays} turns to sink your battleship. Thanks for playing. Better luck next time.")