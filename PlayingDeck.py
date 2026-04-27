#Essencially you draw cards until you run out of cards in deck. Simple, effective and serves as a blueprint for future reference.
import random
Hand = []
OutDeck = []
ValidChoice = ["Y","N"]
print("Your Hand: ")
def DrawHandSort():
    HandSize = 5
    if len(OutDeck) > (52 - 5): #adjusting handsize if there are not enough cards to draw a 5 card hand
        HandSize = (52 - len(OutDeck))
    while len(Hand) < HandSize:   #Loops x times (x is handsize), chooses a card at random and adds it to hand
        Suit = random.choice(["Spades","clubs","Diamonds","Hearts"])
        Rank = random.choice(["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","Kings"])
        CardAppend = (Rank+" of "+Suit)
        if CardAppend not in OutDeck:
            Hand.append(CardAppend)
            OutDeck.append(CardAppend) #making sure that the computer doesnt draw the exact same card twice
        continue
    Hand.sort()

while True: #basic input, draw a random hand of playing cards at will, discards the hand after they are played
    DrawChoice = input("Would you like to Draw Cards?").capitalize()
    if DrawChoice not in ValidChoice: #valid input check
        print("Please answer with Y or N")
        continue
    elif DrawChoice == ValidChoice[0]:
        DeckSize = int(52 - len(OutDeck))
        if DeckSize > 0:
            Hand.clear()
            DrawHandSort()
            for i in Hand:
                print(i)
            print("There are "+str(DeckSize)+" cards left in deck")
        else:
            print("No more cards in deck!")
            break       
    elif DrawChoice == ValidChoice[1]:
        break

input("press enter to close the program")