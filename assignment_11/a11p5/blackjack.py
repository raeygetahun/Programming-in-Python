"""
File: deadoralive.py

This module defines the Deadoralive, Player, and Dealer classes.
"""
from cards import Deck, Card

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

    def play(self):
        print("Player: ", self._player)
        print("Dealer: ", self._dealer)
        while len(self._deck) > 0:
            playerRank = self._player.getRank()
            dealerRank = self._dealer.getRank()
            if playerRank > dealerRank:
                print("Player wins")
            elif playerRank < dealerRank:
                print("Dealer wins")
            else:
                playerSuit = self._player._cards[-1].suit
                dealerSuit = self._dealer._cards[-1].suit
                suits = Card.SUITS
                if suits.index(playerSuit) < suits.index(dealerSuit):
                    print("Player wins")
                else:
                    print("Dealer wins")
            self._player.hit(self._deck.deal())
            self._dealer.hit(self._deck)
            print("Player: ", self._player)
            print("Dealer: ", self._dealer)
        print("Game over")

def main():
    game = Deadoralive()
    game.play()

main()
