#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
      self.cards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
      print('Shuffling cards...')
      shuffle(self.cards)
    
    def split(self):
      print('Splitting cards...')
      return self.cards[:26], self.cards[26:]



class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
      self.cards = cards

    def __str__(self):
      return 'Hand contains {} cards'.format(self.cards)

    def add(self,cards):
      self.cards.extend(cards)

    def remove(self):
      return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
      self.name = name
      self.hand = hand

    def __str__(self):
      return 'Player, "{}", is holding cards {}'.format(self.name, self.hand)

    def play_card(self):
      card_played = self.hand.remove()
      print('{} played {}'.format(self.name, card_played))
      return card_played

    def wage_war(self):
      war_cards = []
      if (len(self.hand.cards) >= 3):
        for _ in range(3):
          war_cards.append(self.hand.remove())
      return war_cards

    def has_cards(self):
      return len(self.hand.cards) != 0

######################
#### GAME PLAY #######
######################
class Game:
  """
  This is the Game class which contains the game logic. The game is played out 
  automatically. Each game consists of the Player and the Computer. Each player
  must forfeit their cards to a war pile. Winner of the round will take everything
  in the war pile. To start, instantiate Game and run start_new_game() method.
  """
  def __init__(self):
    self.war_pile = []

  def deal_cards(self):
    deck = Deck()
    deck.shuffle()
    hand1 = Hand(deck.split()[0])
    hand2 = Hand(deck.split()[1])
    computer = Player('Computer', hand1)
    player = Player('Player', hand2)
    return (computer, player)

  def check_card_ranks(self, c_card, p_card):
    card_value = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 
      '8': 8, '9': 9,  '10': 10,  'J': 11,  'Q': 12, 'K': 13, 'A': 14 }
    c_value = card_value[c_card[1]]
    p_value = card_value[p_card[1]]
    if (p_value == c_value):
      print('Cards have the same rank! A war has started!')
      self.war()
    elif (p_value > c_value):
      print('Player has won this round')
      self.player.hand.add(self.war_pile)
      self.war_pile = []
    else:
      print('Computer has won this round')
      self.computer.hand.add(self.war_pile)
      self.war_pile = []

    self.play_card()

    

  def war(self):
    print('Settling war...')
    c_war_draw = self.computer.wage_war()
    p_war_draw = self.player.wage_war()
    self.war_pile.extend(c_war_draw)
    self.war_pile.extend(p_war_draw)

  def play_card(self):
    if self.player.has_cards() == False:
      self.computer.hand.add(self.war_pile)
      return print('Computer has won the game!!!')
    elif self.computer.has_cards() == False:
      self.player.hand.add(self.war_pile)
      return print('Player has won the game!!!')
    else:
      print('Player played a card')
      player_card = self.player.play_card()
      print('Computer played a card')
      computer_card = self.computer.play_card()
      print('Added cards to war pile and comparing ranks of played cards')
      self.war_pile.extend([player_card, computer_card])
      self.check_card_ranks(computer_card, player_card)


  def start_new_game(self):
    print("Welcome to War, let's begin!")
    self.computer, self.player = self.deal_cards()

    while self.player.has_cards() and self.computer.has_cards():
      self.play_card()
    
    return

war = Game()
war.start_new_game()

