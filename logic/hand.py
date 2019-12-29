class HandException(Exception):
        pass

class Hand:
        def __init__(self):
                self.cards = []

        def addCard(self, card):
                if card.rank == "Ace":
                        possibleTotal = sum(self.cards) + 11

                        if possibleTotal > 21:
                                card.value = 11
                        else:
                                card.value = 1

                self.cards.append(card)

        def showAllCards(self):
                for c in self.cards:
                        print(c)

        def getTotal(self):
                total = 0
                for c in self.cards:
                        total += c.value

                return total


                
                        