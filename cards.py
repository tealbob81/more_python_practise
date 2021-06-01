import random

class Card():
    """Create a card class that takes value and suit as attributes.
       When a Card is printed it is formatted to value of suit."""

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value} of {self.suit}'
        #return '{} of {}'.format(self.value, self.suit)
    
class Deck():

    """A class for deck of cards. A list creating all 52 cards is created upon initilizing.
       When Deck is preinted the amount of cards left in deck is given.
       Count returns the amount of cards in Deck.
       _deal removes n number of cards from deck.
       Shuffle uses random.shuffle module to mix up the order of the deck. It can only be done on a full deck.
       Deal_card deals just one card.
       Deal_hand deals n number of cards."""

    
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7','8', '9', '10', 'J', 'Q', 'K']
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f'Deck of {len(self.cards)} cards'
        #return 'Deck of {} cards'.format(len(self.cards))

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError('All cards have been dealt')
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def shuffle(self):
        if len(self.cards) == 52:
            return random.shuffle(self.cards)
        else:
            raise ValueError('Only full decks can be shuffled')

    def deal_card(self):
        return self._deal(1)[0]
        

    def deal_hand(self, num):
        return self._deal(num)
        


d = Deck()
d.shuffle()
print(d.deal_card())
        



        





##        self.cards = []
##        for i in Card.suit:
##            for j in Card.value:
##                self.cards.append(f'{j} of {i}')
        

#card = Card('4', 'spades')
#print(card)
#deck = Deck(cards)

