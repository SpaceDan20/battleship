import random

class Ship:
  # Constructor
  def __init__(self, ship_type, size, letter):
    self.ship_type = ship_type
    self.size = size
    self.letter = letter
    self.coords = []
    