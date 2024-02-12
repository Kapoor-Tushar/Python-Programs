#In this project we will be creating war card game.
#Pate pe Pata

#1) First we will be declaring the some of the values like suits, rank and values for each rank and importing required modules.
import random

suits = ('Spades','Hearts','Clubs', 'Diamonds')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

#2) Now we will creating card class which will describe us about a single card
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    #Creating a method for printing the card using print() method
    def __str__(self):
        return self.rank +' of '+self.suit

#3) Now we will be creating deck class which will conatain all cards in a deck. It will conatin methods to shuffle cards and deal a card to the player.
class Deck:
    def __init__(self):
        #This list will conatin all the cards
        self.all_cards = []
        #This is the logic to generate all the cards in the deck.
        for suit in suits:
            for rank in ranks:
                created_card = Card(rank,suit)
                self.all_cards.append(created_card)
                
    #Creating a method for shuffling the cards
    def shuffle(self):
        random.shuffle(self.all_cards)

    #Creating a method to deal one card
    def deal_one_card(self):
        #Here we are removing the first card from the shuffled deck as always remove the top card from the deck while distributing the cards to players.
        return self.all_cards.pop(0)

#4) Now we will be creating player class which will conatin player name, cards with player, method to remove and add card(s) and print the player.
class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards_with_player = []
    #Creating a method to print the player
    def __str__(self):
        return (f'Player {self.name} has {len(self.all_cards_with_player)} cards')
    #creating method to remove the top card in from the set of cards player has.
    def remove_one_card(self):
        return self.all_cards_with_player.pop(0)
    def add_cards(self,new_cards):
        if(type(new_cards)==type([])):
            self.all_cards_with_player.extend(new_cards)
        else:
            self.all_cards_with_player.append(new_cards)

#5) Now we will be creating game logic
def gamePlay():
    #Welcome message
    print('Welcome to War of Cards')
    #Taking player name input
    player1Name = input('Enter the name of Player 1: ')
    player2Name = input('Enter the name of Player 2: ')

    #Creating players
    player1 = Player(player1Name)
    player2 = Player(player2Name)

    #Creating a new Deck of cards
    new_deck = Deck()
    #Shuffling the deck
    new_deck.shuffle()
    #Distributing cards to player 1 and 2
    for i in range(26):
        player1.add_cards(new_deck.deal_one_card())
        player2.add_cards(new_deck.deal_one_card())
    print(player1)
    print(player2)
    print('\n')
    
    gameon = True
    #Now we will be playing game between player 1 and player 2. Both the players are computers.
    while gameon:
        #Checking for who won
        if(len(player1.all_cards_with_player)==0):
            print(f'Player {player2.name} wins!')
            gameon = False
            break
        if(len(player2.all_cards_with_player)==0):
            print(f'Player {player1.name} wins!')
            gameon = False
            break
        
        player1Cards = []
        player2Cards = []
        
        #Removing top most card from each player
        player1Cards.append(player1.remove_one_card())
        player2Cards.append(player2.remove_one_card())
        
        print(f'Card thrown by {player1.name} is ',player1Cards[-1])
        print(f'Card thrown by {player2.name} is ',player2Cards[-1])
        
        #Game logic
        atwar = True
        while atwar:
            if(player1Cards[-1].value>player2Cards[-1].value):
                    player1.add_cards(player1Cards)
                    player1.add_cards(player2Cards)
                    print (f'Card in hands of {player1.name}: ',len(player1.all_cards_with_player),f'\nCards in hands of {player2.name}: ',len(player2.all_cards_with_player))
                    print(f'{player1.name} wins this round')
                    print('\n')
                    atwar = False
                    
            elif(player1Cards[-1].value<player2Cards[-1].value):
                    player2.add_cards(player1Cards)
                    player2.add_cards(player2Cards)
                    print (f'Card in hands of {player1.name}: ',len(player1.all_cards_with_player),f'\nCards in hands of {player2.name}: ',len(player2.all_cards_with_player))  
                    print(f'{player2.name} wins this round')
                    print('\n')
                    atwar = False
            else:
                print('Same Cards ---- War!')
                if(len(player1.all_cards_with_player)<5):
                    print(f"Player {player1.name} unable to play war! Game Over at War")
                    print(f"Player {player2.name} Wins!")
                    gameon=False
                    break
                elif(len(player2.all_cards_with_player)<5):
                    print(f"Player {player2.name} unable to play war! Game Over at War")
                    print(f"Player {player1.name} Wins!")
                    gameon=False
                    break
                else:
                    print('Now each player will throw 5 cards')
                    for i in range(5):
                        player1Cards.append(player1.remove_one_card())
                        player2Cards.append(player2.remove_one_card())
                    

gamePlay()              
