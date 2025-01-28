""" 

1 # # # 0
# 3 # # #
# # 1 3 #
# 0 # # #

Use a Stack for the shuffled deck (game board after the cards are shuffled) of 4x5 cards using a stack to store them and then "print" from


might use queue for computer instructions: 

flip chosen card 1, 
flip chosen card 2, 
compare the newly flipped cards,
only reflip if they don't match

Use another data type for storing the game board and the card states

Use a stack of cards to check each "index" one by one and see if we need to update the given card to a true or false flip state

"""

#If the chosen cards to flip are the same number then it may cuase issues, need to troubleshhot later
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
    
    #Assemble gameboard
    """while deck:
        gameBoard(deck)"""
    
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
        #print(str(currentCardTemp.data))
        
        #print(currentCardTemp.data[1])
    
        cardNumber = currentCardTemp.data[1]
        #print(cardNumber)
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
        while not cardsToFlip[i].isdigit() or not 1 <= int(cardsToFlip[i]) <= 20: #Could add a case where the number has already been guessed and is a symbol
            cardsToFlip[i] = input("Sorry that wasn't an integer number between 1-20. Or it was already guessed. What is the number (1-20) of the next card you want to flip? ")
            
        for card in deck:
            currentCardTemp.next = Node(card) #What is this mess
            currentCardTemp = currentCardTemp.next #What is this mess
        
            if int(cardsToFlip[i]) == currentCardTemp.data[1]:
                #currentCardTemp.data[1] = currentCardTemp.data[0]
                currentCardSymbol[i] = currentCardTemp.data[0]
                print("Card ", cardsToFlip[i], " is a ", currentCardTemp.data[0])
            
                #Only flip if the symbols match, make sure to flip both cards FIX THIS
                """if int(cardsToFlip[i]) == currentCardTemp.data[1]:
                    currentCardTemp.data[1] = currentCardTemp.data[0]"""
                        #print("Card ", cardFlip1, " is a ", currentCardTemp.data[0])
                        
                if currentCardSymbol[0] == currentCardSymbol[1]:
                    #Need to iterate through the whole gameboard and update the matching pair FIX THIS
                    print("pair\n")

                    currentCardTemp.data[1] = currentCardTemp.data[0]

    """cardFlip2 = input("What is the number of the second card you want to flip? ")
    while not cardFlip2.isdigit() or not 1 <= int(cardFlip2) <= 20:
        cardFlip2 = input("Sorry that wasn't an integer number between 1-20. What is the number (1-20) of the second card you want to flip?\n")"""
    
    
    
    """for card in deck:
        currentCardTemp.next = Node(card)
        currentCardTemp = currentCardTemp.next
    
        if int(cardsToFlip[i]) == currentCardTemp.data[1]:
            #currentCardTemp.data[1] = currentCardTemp.data[0]
            print("Card ", cardsToFlip[i], " is a ", currentCardTemp.data[0])"""
            
    """if int(cardFlip2) == currentCardTemp.data[1]:
        #currentCardTemp.data[1] = currentCardTemp.data[0]
        print("Card ", cardFlip2, " is a ", currentCardTemp.data[0])"""

    
    print("The chosen cards were not a pair.\n")
        
        
    print("Current Gameboard:\n")
    """else: 
        for card in deck:
            currentCardTemp.next = Node(card)
            currentCardTemp = currentCardTemp.next
        
            if int(cardsToFlip[i]) == currentCardTemp.data[1]:
                currentCardTemp.data[1] = currentCardTemp.data[0]
                #print("Card ", cardFlip1, " is a ", currentCardTemp.data[0])
                
            if int(cardFlip2) == currentCardTemp.data[1]:
                currentCardTemp.data[1] = currentCardTemp.data[0]
                #print("Card ", cardFlip2, " is a ", currentCardTemp.data[0])"""

    return deck


#If there is a main method, run it
if __name__ == "__main__":
    main()