"""
File: deadoralive.py

This module defines the Deadoralive, Player, and Dealer classes.
"""
from cards import Deck, Card

class Card(object):
    """ A card object with a suit and rank."""

    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

    SUITS = ('Spades', 'Diamonds', 'Hearts', 'Clubs')

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit

    def __lt__(self, other):
        """Less than operator overload."""
        return self.rank < other.rank

    def __gt__(self, other):
        """Greater than operator overload."""
        return self.rank > other.rank

    def __eq__(self, other):
        """Equal to operator overload."""
        return self.rank == other.rank

class Player(object):
    """This class represents a player in the Deadoralive game."""

    def __init__(self, cards):
        self._cards = cards

    def __str__(self):
        """Returns string representation of cards."""
        result = ", ".join(map(str, self._cards))
        return result

    def hit(self, card):
        self._cards.append(card)

    def getRank(self):
        """Returns the rank of the highest card in hand."""
        return max(card.rank for card in self._cards)

class Dealer(Player):
    """Like a Player, but with some restrictions."""

    def __init__(self, cards):
        """Initial state: show one card only."""
        Player.__init__(self, cards)
        self._showOneCard = True

    def __str__(self):
        """Return just one card if not hit yet."""
        if self._showOneCard:
            return str(self._cards[0])
        else:
            return Player.__str__(self)

    def hit(self, deck):
        """Add cards until rank >= player's rank,
        then allow all cards to be shown."""
        self._showOneCard = False
        playerRank = self.getRank()
        while self.getRank() < playerRank:
            self._cards.append(deck.deal())

class Deadoralive(object):

    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()
        self._player = Player([self._deck.deal()])
        self._dealer = Dealer([self._deck.deal()])
        self._player_wins = 0
        self._player_losses = 0

    def play(self):
        print("Player: ", self._player)
        print("Dealer: ", self._dealer)
        while len(self._deck) > 0:
            playerRank = self._player.getRank()
            dealerRank = self._dealer.getRank()
            if playerRank > dealerRank:
                self._player_wins += 2
                print("Player wins")
            elif playerRank < dealerRank:
                self._player_losses += 2
                print("Dealer wins")
            else:
                print("Tie! The game continues.")
            self._player.hit(self._deck.deal())
            self._dealer.hit(self._deck)
            print("Player: ", self._player)
            print("Dealer: ", self._dealer)
        print("Game over")
        print("Player wins:", self._player_wins)
        print("Player losses:", self._player_losses)

def main():
    game = Deadoralive()
    game.play()

main()
