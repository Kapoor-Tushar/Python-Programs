#Shell Game
# In this game we will be having 3 shells and one ball, we will be using functions to create this game

#1) We will be creating shuffle function. For this we require shuffle from random library.
from random import shuffle
def shuffle_list(arr):
    shuffle(arr)
    return arr

#2) Creating game playing logic function 
def shell_game(user_input):
    arr = ['O',' ',' ']
    shuffled_arr = shuffle_list(arr)
    if(shuffled_arr[user_input]=='O'):
        print(arr)
        return True
    else:
        print(arr)
        return False

#3) Creating function for user input and deciding whether user won or lost.
def game_playing():
    print('There are 3 shells - shell 1, shell 2 & shell 3.\nEnter the shell number you think in which ball is present.')
    user_inpt = 8
    while user_inpt not in [1,2,3]:
        user_inpt = int(input("Enter the shell number: "))
        if(user_inpt not in [1,2,3]):
            print('Shell number is out of range, please enter again!\n')
    shell_game_play = shell_game(user_inpt-1)
    if(shell_game_play == True):
        print('You Won!')
    else:
        print('You Lose!')

#4) Creating function for user to play more than one time.  
def player_guess():
    x=0   
    while(x==0):
        game_playing()    
        x = int(input("To play more press 0 and to exit press 1: "))
        print('\n')
#5) Calling function to execute it in the interpreter.
player_guess()
