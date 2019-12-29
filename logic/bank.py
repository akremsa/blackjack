class BankException(Exception):
        pass 

class Bank:
        def __init__(self, total):
                self.total = total
                self.bet = 0

        def loose(self):
                if self.bet == 0:
                        raise BankException("Please make a bet.")
                self.total -= self.bet

        def win(self):
                self.total += self.bet

        def makeBet(self, bet):
                if self.total < bet:
                        raise BankException("Not enough money on your bank account")

                self.bet = bet
        