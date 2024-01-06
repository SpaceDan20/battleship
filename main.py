import random
import time

class Ship:
  # Constructor
  def __init__(self, ship_type, size):
    self.ship_type = ship_type
    self.size = size
    self.coords = []

  def get_user_coords(self):
    """Gets x and y coordinates for current ship and returns them"""
    x = int(input(f"\nYou get a {self.ship_type}. Where do you want her? X-coordinate (1-10): ")) - 1
    y = int(input("Bow y-coordinate (1-10): ")) - 1
    return x, y

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

  def place_ship(self):
    """
    Calls get_user_coords() to get x and y coordinates from player.
    Calls find_orientations() function to determine possible placements. 
    Asks player for orientation, then builds ship in that orientation.
    """
    x, y = self.get_user_coords()
    player_board[y][x] = ship_letters[self.ship_type]
    possible_orientations = self.find_orientations(x, y)
    display_board(player_board)
    print(f"""\n
          This is your ship so far. It's the {ship_letters[self.ship_type]} surrounded by Os of water.
          That's right. We're constructing her out in the middle of the sea.
          Why? Cause we're insane. (and not very practical).
    """)
    placing = True
    while placing:
      chosen_orientation = input(f"You can create the rest of the ship in these orientations: {possible_orientations}. Which one do you want? ").lower()
      if chosen_orientation in possible_orientations:
        for i in range(self.size):
          if chosen_orientation == "left":
            player_board[y][x-i] = ship_letters[self.ship_type]
            self.coords.append((x-i, y))
          elif chosen_orientation == "right":
            player_board[y][x+i] = ship_letters[self.ship_type]
            self.coords.append((x+i, y))
          elif chosen_orientation == "up":
            player_board[y-i][x] = ship_letters[self.ship_type]
            self.coords.append((x, y-i))
          elif chosen_orientation == "down":
            player_board[y+i][x] = ship_letters[self.ship_type]
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

def check_for_ships(board, ship_letters):
  # Takes current board and iterates through sea spaces to check if any of the player's ships remain. Returns True if all ships are sunk.
  for row in board:
    for sea_space in row:
      if any(letter in sea_space for letter in ship_letters):
        return False
  return True

# Player Introduction
print("""
      Welcome to Battleship!
      Good news! The government allotted us more money at the expense of useless housing and road-fixing projects, so we have FIVE ships now!
      This will make us a VERY powerful navy that will put FEAR into the enemy computer.
      At the moment, our construction team isn't the brightest, so if you build two ships at the same place... well...
      Let's just say they won't bat an eye when the two ships merge into one. Try to avoid doing that, as smart as it seems.
      """)
ship_letters = {"patrol boat": "P", "destroyer": "D", "submarine": "S", "battleship": "B", "carrier": "C"}
ship_letter_list = [ship_letters[item] for item in ship_letters]

# Set up boards
player_board = [['O' for _ in range(10)] for _ in range(10)]

# Create player's patrol boat
player_patrol_boat = Ship(ship_type="patrol boat", size=1)
x = int(input(f"\nYou get a Patrol Boat. Where do you want her? X-coordinate (1-10): ")) - 1
y = int(input("Bow y-coordinate (1-10): ")) - 1
player_board[y][x] = "P"
display_board(player_board)

# Create remaining player ships and place them on the board, using player's inputs in 'place_ship()'
player_destroyer = Ship(ship_type="destroyer", size=2)
player_destroyer.place_ship()
player_submarine = Ship(ship_type="submarine", size=3)
player_submarine.place_ship()
player_battleship = Ship(ship_type="battleship", size=4)
player_battleship.place_ship()
player_carrier = Ship(ship_type="carrier", size=5)
player_carrier.place_ship()

print("----------------------------------------------------")
print("Player board:")
display_board(player_board)

print("""\n
      This is your part of the sea. For now. The letters represent your ships.
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
    if current_pick not in ["X", "-"]:
      print(f"\n      {random_x_cord+1}, {random_y_cord+1}!")

      # Computer hits battleship
      if current_pick in ship_letter_list:

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
      all_ships_sunk = check_for_ships(player_board, ship_letter_list)
      picking = False

print("Get SUNK mf!")

if plays > 75:
  print(f"\nIt took the enemy computer {plays} turns to sink your ships. What an idiot. Anyway, thanks for playing. Better luck next time.")
elif plays < 20:
  print(f"\nIt took the enemy computer {plays} turns to sink your ships. Oh wow, what a lucky fella. Anyway, thanks for playing. Better luck next time.")
else:
  print(f"\nIt took the enemy computer {plays} turns to sink your ships. Thanks for playing. Better luck next time.")