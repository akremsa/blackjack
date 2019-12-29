from logic import card
from logic import deck
from logic import bank
from logic import hand


while True:
        try:
                print("\nWelcome!")

                total = int(input("Please provide you bank account total: "))
                if total <= 0:
                        raise ValueError("Total amount can not be less than 0")

                b = bank.Bank(total)
                        
                d = deck.Deck()
                d.shuffle()

                dealerHand = hand.Hand()
                playerHand = hand.Hand()

                # hide one dealer card
                print("\nDealer's hand:\nHidden Card")
                dealerHand.addCard(d.deal(False))
                dealerHand.addCard(d.deal(True))

                print("\nPlayer's hand")
                playerHand.addCard(d.deal(True))
                playerHand.addCard(d.deal(True))

                bet = 0
                while bet <= 0 :
                        try:
                                bet = int(input("\nPlease input your bet: "))
                                if bet <= 0:
                                        raise ValueError("Bet can not be less than 0")

                        except ValueError as e:
                                print(e)

                bust = False
                while True:
                        res = input("Would you like to hit or stand? h/s: ")
                        if res[0].lower() == "s":
                                break
                        if res[0].lower() == "h":
                                playerHand.addCard(d.deal(True))
                        else:
                                print("Please choose a correct option")
                                continue

                        if playerHand.getTotal() > 21:
                                print("You got over 21, your score is {0}! Game over!".format(playerHand.getTotal()))
                                bust = True
                                break
                
                if not bust:
                        print("\nDealer's turn")

                        while dealerHand.getTotal() < 17:
                                dealerHand.addCard(d.deal(True))

                        print("\nDealer's cards:")
                        dealerHand.showAllCards()
                        print("\nPlayer's cards:")
                        playerHand.showAllCards()

                        if dealerHand.getTotal() > playerHand.getTotal():
                                print("Dealer wins! Dealer: {0}, player: {1}".format(dealerHand.getTotal(), playerHand.getTotal()))
                                b.loose()
                        elif dealerHand.getTotal() < playerHand.getTotal():
                                print("Player wins! Dealer: {0}, player: {1}".format(dealerHand.getTotal(), playerHand.getTotal()))
                                b.win()
                        else:
                                print("Dealer and Player tie! It's a push.")

        except bank.BankException as e:
                print(e)

        except ValueError as e:
                print(e)

        except Exception as e :
                print(e)

        finally:
                answer = input("Do you want to play again? y/n: ")

                if answer != "y":
                        break
        
                


