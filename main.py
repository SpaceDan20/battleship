import random
import time

class Ship:
  # Constructor
  def __init__(self):
    self.coords = []


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

print("Welcome to Battleship!")
x_cord = int(input("You get 1 battleship. Yeah... budget's tight this year. Where do you want her? Bow x-coordinate (1-10): "))
y_cord = int(input("Bow y-coordinate (1-10): "))

# Create player battleship and update board
player_battleship = Ship()
player_board[y_cord-1][x_cord-1] = "B"

# Checking if ship can be placed left or right
possible_placements = ["up", "down", "left", "right"]
if x_cord-1 < 4:
  possible_placements.remove("left")
if x_cord-1 > 5:
  possible_placements.remove("right")
if y_cord-1 < 4:
  possible_placements.remove("up")
if y_cord-1 > 5:
  possible_placements.remove("down")

display_board(player_board)
print("""\nThis is your ship so far. It's the B surrounded by Os of water.
That's right. We're constructing her out in the middle of the sea.
Why? Cause we're insane. (and not very practical)""")

# Placing rest of battleship
placing = True
while placing:
  placement = input(f"\nYou can build the rest of your ship in one of the following orientations: {possible_placements}\nWhich orientation do you want? ").lower()
  if placement in possible_placements:
    for i in range(5):
      if placement == "left":
        player_board[y_cord-1][x_cord-i-1] = "B"
        player_battleship.coords.append((x_cord-1-i, y_cord-1))
      elif placement == "right":
        player_board[y_cord-1][x_cord+i-1] = "B"
        player_battleship.coords.append((x_cord-1+i, y_cord-1))
      elif placement == "up":
        player_board[y_cord-i-1][x_cord-1] = "B"
        player_battleship.coords.append((x_cord-1, y_cord-1-i))
      elif placement == "down":
        player_board[y_cord+i-1][x_cord-1] = "B"
        player_battleship.coords.append((x_cord-1, y_cord-1+i))
      placing = False
  else:
    print("\nThat's not a valid option. Try again.")

print("----------------------------------------------------")
print(f"These are your battleship's coordinates (they are 0-indexed):\n{player_battleship.coords}")
print("Don't know what 0-indexed means? Don't worry about it :)")
print("Player board:")
display_board(player_board)

print("""\nThis is your part of the sea. For now. The B's represent your ship.
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
    random_x_cord = random.randint(1, 10)
    random_y_cord = random.randint(1, 10)
    current_pick = player_board[random_y_cord-1][random_x_cord-1]
    # loops through to make sure AI doesn't choose already shot sector
    if current_pick in ["O", "B"]:
      print(f"\n      {random_x_cord}, {random_y_cord}!")

      # AI hits battleship
      if current_pick == "B":

        player_board[random_y_cord-1][random_x_cord-1] = "X"
        print("      BOOM!")
        display_board(player_board)
        time.sleep(1)
        print(f"\nYeah mf!! Hit! Back to shooting off my shots at random.")
        player_battleship.coords.remove((random_x_cord-1, random_y_cord-1))
        time.sleep(1)

      # AI misses
      else:
        time.sleep(0.3)
        player_board[random_y_cord-1][random_x_cord-1] = "-"
        display_board(player_board)

      # updates after each time AI shoots
      plays += 1
      picking = False

print("Get SUNK mf!")

if plays > 75:
  print(f"\nIt took the AI {plays} turns to sink your battleship. What an idiot. Anyway, thanks for playing. Better luck next time.")
else:
  print(f"\nIt took the AI {plays} turns to sink your battleship. Thanks for playing. Better luck next time.")