import random

#Linked list class
class Node:
    def __init__(self, data=None):
        # Data stored in the node
        self.data = data
        # Reference to the next node in the singly linked list
        self.next = None


def main():
    #ChatGPT helped with instructions and understanding python formatting and problem solving
    print("The memory card game, also known as Concentration, is a card-matching game where all cards are laid face down.")
    print("You will take turns flipping over two cards at a time, trying to find matching pairs.")
    print("The goal is to remember the locations of cards to match them and collect pairs until all cards are matched.")
    print("Once you match all the cards and have none flipped upside down you win!\n")
    
    deck = deckBuilder()
    gameBoard(deck)
    gameRunning = True
    
    while gameRunning == True:
        print(deck)
        inputChecker(deck)
        gameBoard(deck)
        
    #if all cards are flipped stop the game and add a congratulations message
    
#Build a "shuffled" stack of 20 cards that has 2 of each symbol in it in it
def deckBuilder():
    deck = []
    
    # List of 2 of each symbol that will be used as pairs of cards
    symbols = ['!', '@', '#', '$', '%', '<', '&', '*', '>', '+', 
               '!', '@', '#', '$', '%', '<', '&', '*', '>', '+']
    random.shuffle(symbols)

    #List of numbers from 1 - 20
    numbers = list(range(1, 21))

    for symbol in symbols:
        deck.append([symbol, numbers.pop()])

    return(deck)

def gameBoard(deck):
    nodeCounter = 0
    
    currentCard = Node() #What is this mess
    currentCardTemp = currentCard #What is this mess
    
    for card in deck:
        nodeCounter += 1
        
        currentCardTemp.next = Node(card) #What is this mess
        currentCardTemp = currentCardTemp.next #What is this mess
    
        cardNumber = currentCardTemp.data[1]
        
        if isinstance(cardNumber, int):
            if cardNumber > 9:
                print(f"{cardNumber}", end = "  ")
            else:
                print(f" {cardNumber}", end = "  ")
        else: 
            print(f" {currentCardTemp.data[0]}", end = "  ")

        #If amount of nodes printed is divisible by 5 start a new row
        if nodeCounter % 5 == 0:
            print("\n")
        
#Take user input and check the values of the cards chosen to see if they are a pair
def inputChecker(deck):
    currentCard = Node() #What is this mess
    currentCardTemp = currentCard #What is this mess
    
    cardsToFlip = [0, 0]
    currentCardSymbol = [0, 1]
    
    for i in range(0, 2):
        cardsToFlip[i] = input("What is the number of the next card you want to flip? ")
        while not cardsToFlip[i].isdigit() or not 1 <= int(cardsToFlip[i]) <= 20:
            cardsToFlip[i] = input("Sorry that wasn't an integer number between 1-20. Or it was already guessed. What is the number (1-20) of the next card you want to flip? ")
            
        for card in deck:
            currentCardTemp.next = Node(card) #What is this mess
            currentCardTemp = currentCardTemp.next #What is this mess
        
            if int(cardsToFlip[i]) == currentCardTemp.data[1]:
                #currentCardTemp.data[1] = currentCardTemp.data[0]
                currentCardSymbol[i] = currentCardTemp.data[0]
                print("Card ", cardsToFlip[i], " is a ", currentCardTemp.data[0])
            
                #Only flip if the symbols match, make sure to flip both cards FIX THIS
                        
                #Only flips the second card given because it does not know if they are a pair until after it iterates throught the linked list
                if currentCardSymbol[0] == currentCardSymbol[1]:
                    #Need to iterate through the whole gameboard and update the matching pair FIX THIS
                    print("pair\n")

                    currentCardTemp.data[1] = currentCardTemp.data[0]
    
    print("The chosen cards were not a pair.\n")
    print("Current Gameboard:\n")
    return deck


#If there is a main method, run it
if __name__ == "__main__":
    main()