import random

cardNumbers = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
cardSuits = ["Spades", "Hearts", "Clubs", "Diamonds"]

class Deck:
  def __init__(self):
    self.deck = []
    self.discards = []
    self.shuffle()
  @staticmethod
  def get_numbers():
    return cardNumbers
  @staticmethod
  def get_suits():
    return cardSuits
  def shuffle(self):
    deck = []
    for number in cardNumbers:
      for suit in cardSuits:
        deck.append({"number": number, "suit": suit})
    random.shuffle(deck)
    self.deck = deck
    self.discards = []
  def draw(self):
    try:
      card = self.deck.pop()
      self.discards.append(card)
      return card
    except IndexError:
      return None
  def get(self, index):
    try:
      return self.deck[-(index+1)]
    except IndexError:
      return None
  def get_discards(self):
    return self.discards
    
