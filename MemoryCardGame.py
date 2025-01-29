#ChatGPT helped with game introduction and understanding python formatting and some linked list problem solving
#Used chatGPT to help with learning python syntax and how to arrange pieces for a desired output
#Used geeks for geeks to reference some python linked list base code
import random

#Node class to use in creating and manipulating linked lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#linked list class that has a few general linked list manipulation methods
#Also has more purpose built custom methods
class LinkedList:
    def __init__(self):
        self.head = None

    #Method to add a node at the beginning of the linked list
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    #Update node at a given position in the linked list
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        while current_node is not None and position != index:
            position += 1
            current_node = current_node.next

        if current_node is not None:
            current_node.data[1] = val
        else:
            print("Index not present")
            
    #Print the formatted deck linked list as a game board
    def printBoard(self):
        current_node = self.head
        nodeCounter = 0
        
        print("Current Game Board:", end = "")
        
        while current_node: 
            #If amount of nodes printed is divisible by 5 start a new row
            if nodeCounter % 5 == 0:
                print("\n")
            
            if isinstance(current_node.data[1], int):
                if current_node.data[1] > 9:
                    print(f"{current_node.data[1]}", end = "  ")
                else:
                    print(f" {current_node.data[1]}", end = "  ")
            else: #If the data is a symbol (not an int)
                print(f" {current_node.data[0]}", end = "  ")
                
            current_node = current_node.next
            nodeCounter += 1
        print("\n")
        
    #Check if ALL cards are symbols (not ints)
    def allNonInt(self):
        current_node = self.head
        position = 0
        symbolCounter = 0
        while current_node is not None and position != 20:
            if not isinstance(current_node.data[1], int):
                symbolCounter += 1
            position += 1
            current_node = current_node.next

        if symbolCounter == 20:
            return True
        else:
            return False

    #Print the linked list (used for troubleshooting)
    def printLL(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        print()

def main():
    print("The memory card game, also known as Concentration, is a card-matching game where all cards are laid face down.")
    print("You will take turns flipping over two cards at a time, trying to find matching pairs.")
    print("The goal is to remember the locations of cards to match them and collect pairs until all cards are matched.")
    print("Once you match all the cards and have none flipped upside down you win!\n")
    
    deck = deckBuilder()
    gameRunning = True

    while gameRunning == True:
        #Uncomment to print the linked list for troubleshooting or "cheating" the game
        #deck.printLL()
        
        deck.printBoard()
        guessedCards_guessedSymbols = inputChecker(deck)
        
        if isItAPair(guessedCards_guessedSymbols) == True:
            deck.updateNode(guessedCards_guessedSymbols[1][0], int(guessedCards_guessedSymbols[0][0]) - 1)
            deck.updateNode(guessedCards_guessedSymbols[1][1], int(guessedCards_guessedSymbols[0][1]) - 1)

        if deck.allNonInt() == True:
            deck.printBoard()
            print("Congratulations!!! You beat the game. Good job sticking in there!")
            gameRunning = False
    
#Build a "shuffled" stack of 20 cards that has 2 of each symbol and a number on the "back" of each card.
def deckBuilder():
    deck = LinkedList()
    
    # List of 2 of each symbol that will be used as pairs of cards
    symbols = ['!', '@', '#', '$', '%', '<', '&', '*', '>', '+', 
               '!', '@', '#', '$', '%', '<', '&', '*', '>', '+']
    random.shuffle(symbols)

    #List of numbers from 1 - 20
    numbers = list(range(1, 21))

    for symbol in symbols:
        deck.insertAtBegin([symbol, numbers.pop()])

    return deck
        
#Take user input and make sure it is valid. Then check what the symbols on the cards are and return the user chosen cards and symbols.
def inputChecker(deck):
    cardsToFlip = [0, 0]
    cardSymbols = [0, 1]
    
    for i in range(0, 2):
        cardsToFlip[i] = input("What is the number of the next card you want to flip? ")
        while not cardsToFlip[i].isdigit() or not 1 <= int(cardsToFlip[i]) <= 20:
            cardsToFlip[i] = input("Sorry that wasn't an integer number between 1-20. What is the number (1-20) of the next card you want to flip? ")
    
        current = deck.head
        nodeCounter = 1
            
        while current:
            if nodeCounter == int(cardsToFlip[i]):
                cardSymbols[i] = current.data[0]
            current = current.next
            nodeCounter += 1
            
        print("Card", cardsToFlip[i], "is: ", cardSymbols[i])
            
    guessedCards_guessedSymbols = [cardsToFlip, cardSymbols]
    return guessedCards_guessedSymbols

#If the symbols on the cards are the same then they form a pair
def isItAPair(guessedCards_guessedSymbols):
    if guessedCards_guessedSymbols[1][0] == guessedCards_guessedSymbols[1][1]:
        print("Card", guessedCards_guessedSymbols[0][0], "and card", guessedCards_guessedSymbols[0][1], "are a pair!")
        return True
    else:
        print("Sorry but card", guessedCards_guessedSymbols[0][0], "and card", guessedCards_guessedSymbols[0][1], "are not a pair.")
        return False
    
#If there is a main method, run it
if __name__ == "__main__":
    main()