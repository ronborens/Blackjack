
from random import shuffle
from typing import NamedTuple


CardType = NamedTuple("Card", [('rank', int),('suite', str)])
cardRanks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '11']
cardSuites = ["Spades", "Hearts", "Clubs", "Diamonds"]


class Deck:
    def __init__(self):
        self.deck = []
        for suites in cardSuites:
            for ranks in cardRanks:
                self.deck.append(CardType(ranks, suites))

    def drawCard(self):
        return self.deck.pop()

    def shuffle(self):
        shuffle(self.deck)

class Hand:
    def __init__(self):
        self.handCards = []
        self.totalValue = 0
        self.numAces = 0

    def addCard(self, card):
        self.handCards.append(card)
        self.totalValue += int(card[0])
        if int(card[0]) == 11:
            self.numAces += 1

def checkforAces(hand):
    while hand.totalValue>21 and hand.numAces > 0:
        hand.numAces -= 1
        print("Total Value over 21, changing Aces from 11 to 1. Old Total:",hand.totalValue, end='')
        hand.totalValue -= 10
        print(", New Total:", hand.totalValue)
    
def playerChoice(deck, hand):
    if hand.totalValue == 21:
        keepPlaying = False
    else:
        keepPlaying = True
    while keepPlaying:
        inp = input("\nChoose stay or hit: ")
        print("")
        if inp.lower() == "stay":
            print("Stay selected. Dealer's turn")
            keepPlaying = False
        elif inp.lower() == "hit":
            hand.addCard(deck.drawCard())
            print("Player's Hand:", *hand.handCards, sep='\n')
            checkforAces(hand)
            print("Player Value:", hand.totalValue, sep='\n')
            if(hand.totalValue >= 21 and hand.numAces < 1):
                keepPlaying = False
        else:
            print("Incorrect input.")

    print("")


def showCards(player, dealer):
    print("Dealer's Hand:", *dealer.handCards, "Dealer Value:", dealer.totalValue, "", sep='\n')
    print("Player's Hand:", *player.handCards, "Player Value:", player.totalValue, sep='\n')

def printEndGame(hand, isDealer):
    if isDealer:
        if hand.totalValue > 21:
            print("Dealer Bust! Player Wins!")
        if hand.totalValue == 21:
            print("Dealer Jackpot! Dealer Wins!")
    if not isDealer:
        if hand.totalValue > 21:
            print("Player Bust! Dealer Wins!")
        if hand.totalValue == 21:
            print("Player Jackpot! Player Wins!")
    

def playGame():
    playAgain = 1
    while playAgain:
        print("Welcome to black jack!\n")
        deck = Deck()
        deck.shuffle()
        player = Hand()
        dealer = Hand()
        # draw 2 cards for both player and dealer
        player.addCard(deck.drawCard())
        player.addCard(deck.drawCard())
        dealer.addCard(deck.drawCard())
        dealer.addCard(deck.drawCard())
        showCards(player, dealer)
        while True:
            playerChoice(deck, player)
            while dealer.totalValue <= 17 and player.totalValue <= 21:
                dealer.addCard(deck.drawCard())
                print("Dealer hit. New total: ", dealer.totalValue)
            if dealer.totalValue >= 21 or player.totalValue >= 21:
                printEndGame(player, False) if player.totalValue>= 21 else printEndGame(dealer, True)
            elif dealer.totalValue < player.totalValue:
                print("Dealer's total: ", dealer.totalValue, "Player's total: ", player.totalValue, "Player Wins!")
            elif dealer.totalValue > player.totalValue:
                print("Dealer's total: ", dealer.totalValue, "Player's total: ", player.totalValue, "Dealer Wins!")
            else:
                print("\nGame Tie!")
            break
        playAgain = input("\nEnter 0 to quit, any other key to continue. ")

if __name__ == "__main__":
    playGame()