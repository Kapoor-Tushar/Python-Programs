#BlackJack
#We will be creating a simplified version of the game with only one human player and a computer dealer.

import random

#1) We will declaring suits, ranks and their values which will be required by this game.
suits = ('Spades','Hearts','Clubs','Diamonds')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Jack':10,'Queen':10,'King':10,'Ace':11}
#2) We will be creating card class for card creation.
class Card:
    #Declaring the constructor for the class
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
    def __str__(self):
        #This will help us to print out class object
        return self.rank + " of " + self.suit

#3) Now we will be creating a class to create deck
class Deck:
    #Declaring the constructor for the class
    def __init__(self):
        #list containing all cards
        self.all_cards = []
        #Implementing logic to create deck
        for suit in suits:
            for rank in ranks:
                new_card = Card(rank,suit)
                self.all_cards.append(new_card)
    #Creating a method to shuffle cards
    def shuffle(self):
        random.shuffle(self.all_cards)
    #Creating a method to remove card from the deck
    def deal_one_card(self):
        #we will always remove the top most card from the deck
        return self.all_cards.pop(0)
        
#4) Now we will be creating player class
class Player:
    #Declaring the constructor for the class
    def __init__(self,name,amount_in_hand):
        self.name = name
        self.amount_in_hand = amount_in_hand
        self.all_cards_with_player = []
    
    #Creating a method to print player
    def __str__(self):
        return (f'Player {self.name} has {len(self.all_cards_with_player)} cards')
    #creating a method to add a card in players hand
    def add_card(self,new_card):
        self.all_cards_with_player.append(new_card)
#Creating a function to calculate total sum of cards
def calSumOfCards(player_card1, player_card2):
    player_card_sum =0 
    if(player_card1.value == 11):
        if(player_card1.value+player_card2.value>21):
            player_card_sum = player_card2.value+1
        else:
            player_card_sum = player_card2.value+player_card1.value
    elif(player_card2.value == 11):
        if(player_card1.value + player_card2.value>21):
            player_card_sum = player_card1.value+1
        else:
            player_card_sum = player_card2.value+player_card1.value
    else:
        player_card_sum = player_card2.value+player_card1.value
    return player_card_sum

#Creating a function to check who won
def checkUserWon(player_card_sum, player_dealer_card_sum, player_user, player_dealer,bet_amount):
    if(player_card_sum >21 ):
        print(f'{player_user.name} got Burst!!')
        print(f"{player_dealer.name} won!!")
        player_dealer.amount_in_hand += bet_amount*2 
        print(f"Equivalent balance of {player_user.name} is {player_user.amount_in_hand}")

    else:
        if((player_card_sum == 21 and player_dealer_card_sum !=21) or player_card_sum>player_dealer_card_sum):
            print(f"{player_user.name} won!!")
            player_user.amount_in_hand += bet_amount*2 
            print(f"Equivalent balance of {player_user.name} is {player_user.amount_in_hand}")
                    
        elif(player_dealer_card_sum>player_card_sum):
            print(f"{player_dealer.name} won!!")
            player_dealer.amount_in_hand += bet_amount*2 
            print(f"Equivalent balance of {player_user.name} is {player_user.amount_in_hand}")
                    
        elif(player_dealer_card_sum==21 and player_card_sum==21):
            print(f"It's a Tie!!")
            player_user.amount_in_hand += bet_amount*2 
            print(f"Equivalent balance of {player_user.name} is {player_user.amount_in_hand}")
        

            
#Creating a function for game Play
def gamePlay():
    print('Welcome to BlackJack!\n')

    #Collecting user data
    player_name = input('Enter your name: ')
    print(f'{player_name} now enter the amount you want to play with, Please note that the maximum amount with which you can play is $1000 and minimum amount is $10.')
    player_amount = int(input('Enter the amount: '))
    while player_amount not in range(10,10000):
        print('Amount you entered is wrong,Please provide correct amount')
        player_amount = input('Enter the amount: ')

    #Creating players
    player_user = Player(player_name,player_amount)
    player_dealer = Player('Dealer',10000)

    #Creating a new deck
    new_deck = Deck()
    #Shuffling the cards
    new_deck.shuffle()

    gameon = True
    while gameon:
        bet_amount = int(input('\nEnter the amount you want to bet: '))
        while bet_amount<10 or bet_amount>player_user.amount_in_hand:
            print('Wrong input')
            print("Betting amount can't be less than 10 or can't be greater than the amount you have in your balance.")
            bet_amount = int(input('Enter the amount you want to bet: '))
        player_user.amount_in_hand -= bet_amount
        print(f'Equivalent balance of {player_user.name} is {player_user.amount_in_hand}')
        
        #Allocating cards to player and dealer
        player_user_card1 = new_deck.deal_one_card()
        player_user_card2 = new_deck.deal_one_card()
        player_dealer_card1 = new_deck.deal_one_card()
        player_dealer_card2 = new_deck.deal_one_card()
        print('\nDealing cards...')
        print(f'Cards with {player_user.name} are ',player_user_card1,"&",player_user_card2)
        
        #Finding sum of cards of player
        player_card_sum = calSumOfCards(player_user_card1, player_user_card2)

        #finding dealer totals sum            
        player_dealer_card_sum = calSumOfCards(player_dealer_card1, player_dealer_card2)
            
        #Printing player equivalent score
        print(f"Cards with {player_dealer.name} are ", player_dealer_card1,'& one unreveiled card\n')
        print(f"Equivalent total of {player_user.name}'s cards is: {player_card_sum}")
        

        hit = int(input('Do you want to hit a card(for hitting a card press 1 and to stay press 0): '))
        if(hit==0):
            print(f"Another card of Dealer is {player_dealer_card2} and equivalent total of dealer is {player_dealer_card_sum}")
            checkUserWon(player_card_sum, player_dealer_card_sum, player_user, player_dealer, bet_amount)
        else:
            while(hit==1):
                print('\nDealing another card')
                player_user_extra_card = new_deck.deal_one_card()
                print(f"New card given to {player_user.name} is {player_user_extra_card}")
                
                if(player_user_extra_card.value==11):
                    if(player_card_sum + player_user_extra_card.value>21):
                        player_card_sum += 1
                    else:
                        player_card_sum += 11
                else:
                    player_card_sum += player_user_extra_card.value
                print(f"New Total of {player_user.name} cards is {player_card_sum}")
                hit = int(input('Do you want to hit a card(for hitting a card press 1 and to stay press 0): '))
            print(f"\nAnother card of Dealer is {player_dealer_card2} and equivalent total of dealer is {player_dealer_card_sum}\n")
            checkUserWon(player_card_sum, player_dealer_card_sum, player_user, player_dealer, bet_amount)
        playMore = int(input('\nTo play more press 1 or to exit press 0: '))
        if(playMore ==0):
            break
        else:
            if(player_user.amount_in_hand!=0):
                continue
            else:
                print('\nSorry! You have 0 rupees in your account please get a topup to play more.')
                break
        
            
gamePlay()








    
        
