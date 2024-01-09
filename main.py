import random
import time
from ship import Ship
from board import Board


def get_coords(ship):
  # Gets user coordinates for current ship
  x = int(input(f"\nYou get a {ship.ship_type}. Where do you want her? X-coordinate (1-10): ")) - 1
  y = int(input("Bow y-coordinate (1-10): ")) - 1
  return x, y


def find_orientations(ship, x, y):
  # Takes x and y coordinates and ship size to determine possible orientations
  possible_orientations = []
  if x - ship.size + 1 >= 0:
    possible_orientations.append("up")
  if y + ship.size - 1 <= 9:
    possible_orientations.append("down")
  if x - ship.size + 1 >= 0:
    possible_orientations.append("left")
  if x + ship.size - 1 <= 9:
    possible_orientations.append("right")
  return possible_orientations


def ask_for_orientation(ship, possible_orientations, x, y):
  # Takes ship and possible orientation and asks user which orientation it wants
  placing = True
  while placing:
    chosen_orientation = input(f"You can create the rest of the ship in these orientations: {possible_orientations}. Which one do you want? ").lower()
    if chosen_orientation in possible_orientations:
      player_board.place_rest_of_ship(ship, chosen_orientation, x, y)
      break


def place_ship(ship):
  x, y = get_coords(ship)
  print(x, y)
  player_board.place_bow(ship, x, y)
  possible_orientations = find_orientations(ship, x, y)
  ask_for_orientation(ship, possible_orientations, x, y)
  player_board.show_board()


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

# Set up boards
player_board = Board()

# Create player's patrol boat
player_patrol_boat = Ship(ship_type="patrol boat", size=1, letter="P")
x, y = get_coords(player_patrol_boat)
player_board.place_bow(player_patrol_boat, x, y)
player_board.show_board()

# Create remaining player ships and place them on the board, using player's inputs in 'place_ship()'
# Destroyer
player_destroyer = Ship(ship_type="destroyer", size=2, letter="D")
place_ship(player_destroyer)
# Submarine
player_submarine = Ship(ship_type="submarine", size=3, letter="S")
place_ship(player_submarine)
# Battleship
player_battleship = Ship(ship_type="battleship", size=4, letter="B")
place_ship(player_battleship)
# Carrier
player_carrier = Ship(ship_type="carrier", size=5, letter="C")
place_ship(player_carrier)

print("----------------------------------------------------")
print("Player board:")
player_board.show_board()

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
ship_letters = ["P", "D", "S", "B", "C"]

# Iterates through until 'all_ships_sunk' finds no more "S"'s on the board, meaning all player ships have been sunk
while not all_ships_sunk:
  picking = True
  while picking:
    random_x_cord = random.randint(0, 9)
    random_y_cord = random.randint(0, 9)
    current_pick = player_board.board[random_y_cord][random_x_cord]
    # loops through to make sure computer doesn't choose already shot sector
    if current_pick not in ["X", "-"]:
      print(f"\n      {random_x_cord+1}, {random_y_cord+1}!")

      # Computer hits battleship
      if current_pick in ship_letters:

        player_board.board[random_y_cord][random_x_cord] = "X"
        print("      BOOM!")
        player_board.show_board()
        time.sleep(1)
        print(f"\nYeah mf!! Hit! Back to shooting off my shots at random.")
        time.sleep(1)

      # Computer misses
      else:
        time.sleep(0.3)
        player_board.board[random_y_cord][random_x_cord] = "-"
        player_board.show_board()

      # updates after each time computer shoots
      plays += 1
      all_ships_sunk = check_for_ships(player_board.board, ship_letters)
      picking = False

print("Get SUNK mf!")

if plays > 75:
  print(f"\nIt took the enemy computer {plays} turns to sink your ships. What an idiot. Anyway, thanks for playing. Better luck next time.")
elif plays < 20:
  print(f"\nIt took the enemy computer {plays} turns to sink your ships. Oh wow, what a lucky fella. Anyway, thanks for playing. Better luck next time.")
else:
  print(f"\nIt took the enemy computer {plays} turns to sink your ships. Thanks for playing. Better luck next time.")