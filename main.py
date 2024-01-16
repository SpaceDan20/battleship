import random
import time
from ship import Ship
from board import Board
from player import Player
from computer_player import ComputerPlayer


def find_orientations(ship, x, y):
  # Takes x and y coordinates and ship size to determine possible orientations
  possible_orientations = []
  if y - ship.size + 1 >= 0:
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
      return chosen_orientation


def place_player_ship(ship):
  # runs other functions related to building a player's ship
  x, y = player.get_coords(ship)
  player_board.place_bow(ship, x, y)
  possible_orientations = find_orientations(ship, x, y)
  orientation = ask_for_orientation(ship, possible_orientations, x, y)
  player_board.place_rest_of_ship(ship, orientation, x, y)
  player_ships.append(ship)
  player_board.show_board()


def check_for_ships(board, ship_letters):
  # Takes current board and iterates through sea spaces to check if any of the player's ships remain. Returns True if a ship is detected.
  for row in board:
    for sea_space in row:
      if any(letter in sea_space for letter in ship_letters):
        return True
  return False


def find_ship_matching_coordinate(x, y, player):
  # Takes guessed coordinates and current player to look in opponent ship list to see if they've struck a ship.
  selected_coords = (x, y)
  if player == "player":
    for ship in computer_ships:
      if selected_coords in ship.coords:
        print(f"\nWowza! You got a hit!")
        ship.coords.remove(selected_coords)
        if not ship.coords:
          time.sleep(1)
          print(f"\nYou sunk their {ship.ship_type}! Way to go!")
  if player == "computer":
    for ship in player_ships:
      if selected_coords in ship.coords:
        print(f"Oh no! They hit your {ship.ship_type}!")
        ship.coords.remove(selected_coords)
        if not ship.coords:
          time.sleep(1)
          print(f"\nOH NO! They sunk your {ship.ship_type}! That cost us a lot of money! {random.randint(1, 1000)} crew also perished. Damn.")
          computer_player.recent_hit = ()


# Player Introduction
print("""
      Welcome to Battleship!
      Good news! The government allotted us more money at the expense of useless housing and road-fixing projects, so we have FIVE ships now!
      This will make us a VERY powerful navy that will put FEAR into the enemy computer.
      At the moment, our construction team isn't the brightest, so if you build two ships at the same place... well...
      Let's just say they won't bat an eye when the two ships merge into one. Try to avoid doing that, as smart as that seems.
      """)

# Set up players and boards
player = Player()
player_ships = []
computer_player = ComputerPlayer()
computer_ships = []
player_board = Board("Player")
computer_board = Board("Computer")
# This board is the board shown to the player when taking turns firing
hidden_computer_board = Board("Computer")

# Create player's patrol boat
player_patrol_boat = Ship(ship_type="patrol boat", size=1, letter="P")
x, y = player.get_coords(player_patrol_boat)
player_board.place_bow(player_patrol_boat, x, y)
player_ships.append(player_patrol_boat)
player_board.show_board()

# Create remaining player ships and place them on the board, using player's inputs in 'place_ship()'
# Destroyer
player_destroyer = Ship(ship_type="destroyer", size=2, letter="D")
place_player_ship(player_destroyer)
# Submarine
player_submarine = Ship(ship_type="submarine", size=3, letter="S")
place_player_ship(player_submarine)
# Battleship
player_battleship = Ship(ship_type="battleship", size=4, letter="B")
place_player_ship(player_battleship)
# Carrier
player_carrier = Ship(ship_type="carrier", size=5, letter="C")
place_player_ship(player_carrier)

# Computer creates and places its ships
computer_patrol_boat = Ship(ship_type="patrol boat", size=1, letter="P")
computer_player.place_computer_boat(computer_patrol_boat, computer_board)
computer_ships.append(computer_patrol_boat)
computer_destroyer = Ship(ship_type="destroyer", size=2, letter="D")
computer_player.place_computer_boat(computer_destroyer, computer_board)
computer_ships.append(computer_destroyer)
computer_submarine = Ship(ship_type="submarine", size=3, letter="S")
computer_player.place_computer_boat(computer_submarine, computer_board)
computer_ships.append(computer_submarine)
computer_battleship = Ship(ship_type="battleship", size=4, letter="B")
computer_player.place_computer_boat(computer_battleship, computer_board)
computer_ships.append(computer_battleship)
computer_carrier = Ship(ship_type="carrier", size=5, letter="C")
computer_player.place_computer_boat(computer_carrier, computer_board)
computer_ships.append(computer_carrier)

# Show board
player_board.show_board()

print("""\n
      This is your part of the sea. Let's keep it that way.
      The letters represent your ships, who are willing to sling large-caliber shells
      toward the enemy computer's ships in their part of the sea.
      However, we must respect the laws of combat and only fire one at a time, before
      waiting for the enemy to barrage one of our coordinates.
      I don't know man, that's just what the admiral told me.
      I tried to get permission for you to fire a salvo, but she declined it.
      Said it was 'unhumanlike' ...
      Personally, I think the computer is unhumanlike.
      You know what? Nevermind. We'll be in combat pretty soon, commander.
      General Quarters!!\n
      """)

user_input = input("Okay. You ready? Type 'ready' or 'not ready': ")
print("Doesn't matter! Here come the shells!\n")
time.sleep(2)

plays = 0
all_ships_sunk = False
ship_letters = ["P", "D", "S", "B", "C"]
any_player_ships = check_for_ships(player_board.board, ship_letters)
any_computer_ships = check_for_ships(computer_board.board, ship_letters)

# Iterates through until 'all_ships_sunk' finds no more "S"'s on the board, meaning all player ships have been sunk
while any_player_ships and any_computer_ships:

  # Computer guesses
  player_board.show_board()
  time.sleep(1)
  # Checks to see if computer had a hit recently in order to make informed guess, if possible
  if computer_player.recent_hit:
    computer_x, computer_y = computer_player.make_informed_guess()
  else:
    computer_x, computer_y = computer_player.make_random_guess()
  print(f"The computer chooses {computer_x + 1}, {computer_y + 1}")
  time.sleep(2)
  current_guess = player_board.board[computer_y][computer_x]
  if current_guess not in ship_letters:
    print("\nHaha he missed.")
    player_board.board[computer_y][computer_x] = "-"
  else:
    player_board.board[computer_y][computer_x] = "X"
    computer_player.recent_hit = (computer_x, computer_y)
    find_ship_matching_coordinate(computer_x, computer_y, "computer")
  player_board.show_board()
  time.sleep(2)
  any_player_ships = check_for_ships(player_board.board, ship_letters)

  # Player guesses
  hidden_computer_board.show_board()
  guess_x, guess_y = player.make_player_guess()
  current_player_guess = computer_board.board[guess_y][guess_x]
  if current_player_guess not in ship_letters:
    computer_board.board[guess_y][guess_x] = "-"
    hidden_computer_board.board[guess_y][guess_x] = "-"
    print("\nHaha YOU missed!")
  else:
    # Finds struck ship and notifies user of hit/sinking
    find_ship_matching_coordinate(guess_x, guess_y, "player")
    computer_board.board[guess_y][guess_x] = "X"
    hidden_computer_board.board[guess_y][guess_x] = "X"
  hidden_computer_board.show_board()
  time.sleep(2)
  any_computer_ships = check_for_ships(computer_board.board, ship_letters)


# Winning conditions
if any_computer_ships:
  player_board.show_board()
  print("""
Well, you blew it. All of our ships are gone. Good going, commander.
Just wait until the admiral hears about this. She's gonna be PISSED at you.
""")
else:
  computer_board.show_board()
  print("""
We won??
Wait, we won?!
...
I mean...
Of course we won. I always knew you had it in you, commander.
Just wait until the admiral hears about this.
I'm definitely getting promoted!
""")