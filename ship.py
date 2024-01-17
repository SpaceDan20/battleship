import random

class Ship:
  # Constructor
  def __init__(self, ship_type, size, letter):
    self.ship_type = ship_type
    self.size = size
    self.letter = letter
    self.coords = []
    self.crew = {"patrol boat": 100,
                 "destroyer": 200,
                 "submarine": 500,
                 "battleship": 1000,
                 "carrier": 3000}
    