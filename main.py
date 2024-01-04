import random
import time

class Ship:
  # Constructor
  def __init__(self, ship_type, size):
    self.ship_type = ship_type
    self.size = size
    self.coords = []

  def find_orientations(self, x, y):
    """Takes x and y coordinates and returns possible orientations ship can be built"""
    possible_placements = []
    if y - self.size + 1 >= 0:
      possible_placements.append("up")
    if y + self.size - 1 <= 9:
      possible_placements.append("down")
    if x - self.size + 1 >= 0:
      possible_placements.append("left")
    if x + self.size - 1 <= 9:
      possible_placements.append("right")
    return possible_placements

  def place_ship(self, x, y):
    """Takes x and y coordinates and calls find_orientations() function to determine possible placements. Asks player for orientation, then builds ship in that orientation."""
    player_board[y][x] = "S"
    possible_orientations = self.find_orientations(x, y)
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
        for i in range(self.size):
          if chosen_orientation == "left":
            player_board[y][x-i] = "S"
            self.coords.append((x-i, y))
          elif chosen_orientation == "right":
            player_board[y][x+i] = "S"
            self.coords.append((x+i, y))
          elif chosen_orientation == "up":
            player_board[y-i][x] = "S"
            self.coords.append((x, y-i))
          elif chosen_orientation == "down":
            player_board[y+i][x] = "S"
            self.coords.append((x, y+i))
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

# Player Introduction
print("""
      Welcome to Battleship!
      Good news! The government allotted us more money at the expense of useless housing and road-fixing projects, so we have FIVE ships now!
      This will make us a VERY powerful navy that will put FEAR into the enemy computer.
      At the moment, our construction team isn't the brightest, so if you build two ships at the same place... well...
      Let's just say they won't bat an eye when the two ships merge into one. Try to avoid doing that, as smart as it seems.
      """)

# Set up boards
player_board = [['O' for _ in range(10)] for _ in range(10)]

# Creating bow coordinates and 0-indexed coordinates of player's ship

# Patrol Boat
player_patrol_boat = Ship(ship_type="patrol boat", size=1)
x = int(input(f"You get a Patrol Boat. Where do you want her? X-coordinate (1-10): ")) - 1
y = int(input("Bow y-coordinate (1-10): ")) - 1
player_patrol_boat.place_ship(x, y)

# Destroyer
player_destroyer = Ship(ship_type="destroyer", size=2)
x = int(input(f"You get a Destroyer. Where do you want her? X-coordinate (1-10): ")) - 1
y = int(input("Bow y-coordinate (1-10): ")) - 1
player_destroyer.place_ship(x, y)

# Submarine
player_submarine = Ship(ship_type="submarine", size=3)
x = int(input(f"You get a Submarine. Where do you want her? X-coordinate (1-10): ")) - 1
y = int(input("Bow y-coordinate (1-10): ")) - 1
player_submarine.place_ship(x, y)

# Battleship
player_battleship = Ship(ship_type="battleship", size=4)
x = int(input(f"You get a Battleship! Where do you want her? X-coordinate (1-10): ")) - 1
y = int(input("Bow y-coordinate (1-10): ")) - 1
player_battleship.place_ship(x, y)

# Carrier
player_carrier = Ship(ship_type="carrier", size=5)
x = int(input(f"You get an Aircraft Carrier. Where do you want her? X-coordinate (1-10): ")) - 1
y = int(input("Bow y-coordinate (1-10): ")) - 1
player_carrier.place_ship(x, y)

print("----------------------------------------------------")
print("Player board:")
display_board(player_board)

print("""\n
      This is your part of the sea. For now. The S's represent your ships.
      But...
      I got some bad news.
      We got so carried away with spending while building the ships that...
      Yeah... we can't afford to buy any ammunition for the ships already placed in the water.
      Unfortunate.
      I'm gonna try to sort this out with the admiral without getting honorably discharged.
      In the meantime, we've got reports of the enemy advancing on your position.
      They will be firing relentlessly pretty soon, so... I don't know. Maybe duck?\n
      """)

user_input = input("Okay. You ready? Type 'ready' or 'not': ")
print("Doesn't matter! Here come the artillery shells!\n")
time.sleep(2)

plays = 0
all_ships_sunk = False

# Iterates through until 'all_ships_sunk' finds no more "S"'s on the board, meaning all player ships have been sunk
while not all_ships_sunk:
  picking = True
  while picking:
    random_x_cord = random.randint(0, 9)
    random_y_cord = random.randint(0, 9)
    current_pick = player_board[random_y_cord][random_x_cord]
    # loops through to make sure computer doesn't choose already shot sector
    if current_pick in ["O", "S"]:
      print(f"\n      {random_x_cord+1}, {random_y_cord+1}!")

      # Computer hits battleship
      if current_pick == "S":

        player_board[random_y_cord][random_x_cord] = "X"
        print("      BOOM!")
        display_board(player_board)
        time.sleep(1)
        print(f"\nYeah mf!! Hit! Back to shooting off my shots at random.")
        time.sleep(1)

      # Computer misses
      else:
        time.sleep(0.3)
        player_board[random_y_cord][random_x_cord] = "-"
        display_board(player_board)

      # updates after each time computer shoots
      plays += 1
      all_ships_sunk = all("S" not in row for row in player_board)
      picking = False

print("Get SUNK mf!")

if plays > 75:
  print(f"\nIt took the enemy computer {plays} turns to sink your battleship. What an idiot. Anyway, thanks for playing. Better luck next time.")
elif plays < 20:
  print(f"\nIt took the enemy computer {plays} turns to sink your battleship. Oh wow, what a lucky fella. Anyway, thanks for playing. Better luck next time.")
else:
  print(f"\nIt took the enemy computer {plays} turns to sink your battleship. Thanks for playing. Better luck next time.")