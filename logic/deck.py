import logic.card as card
import random

class Deck:
        def __init__(self):
                self.deck = []
                
                for suit in card.suits:
                        for rank in card.ranks:
                                self.deck.append(card.Card(suit, rank))

        def __str__(self):
                res = ""
                for c in self.deck:
                        res += "{0} {1}\n".format(c.rank, c.suit)
                return res

        def shuffle(self):
                random.shuffle(self.deck)

        def deal(self, show):
                card = self.deck.pop()

                if show:
                        print(card)

                return card