class Card:
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    VALS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7',
             '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, vals=0):
        self.suit = suit
        self.vals = vals

    def __str__(self):
        """
          >>> print(Card(2, 11))
          Queen of Hearts
        """
        return '{0} of {1}'.format(Card.VALS[self.vals],
                                   Card.SUITS[self.suit])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
            
def club(circlex, circley, size):
    pygame.draw.polygon(screen, BLACK, ((200, 100), (450, 100), (450, 400), (200, 400)), 2) # draws border
    pygame.draw.ellipse(screen, BLACK, ((circlex, circley), (size, size)), 0)
    pygame.draw.ellipse(screen, BLACK, ((circlex - 25, circley + 45), (size, size)), 0)
    pygame.draw.ellipse(screen, BLACK, ((circlex + 25, circley + 45), (size, size)), 0)
    pygame.draw.polygon(screen, BLACK, ((circlex + 25, circley + 75), (circlex, circley + 125), (circlex + 60, circley + 125)), 0)
club(300, 175, 60)
