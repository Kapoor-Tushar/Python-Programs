#We will be creating tic-tac-toe game for 2 #players.

#1) Creating user input function for selecting the 'X' or 'O'
def userInputXOSelection():
    flag =0
    while (flag ==0):
        user1Symbol = input('Enter the symbol you want(Either X or O): ')
        if((user1Symbol=='x' or user1Symbol=='o' or user1Symbol=='X' or user1Symbol=='O')):
            user1Symbol = user1Symbol.upper()
            break
        else:
            print('You entered a wrong symbol! Please enter again.\n')
            continue
    if(user1Symbol =='X'):
        user2Symbol = 'O'
    else:
        user2Symbol = 'X'
    return (user1Symbol,user2Symbol)

#2) Creating a function to print numpad
def printNumpad():
    print('1|2|3\n4|5|6\n7|8|9\n')

#3) Creating a function to print gamepad
def printUserBoard(row1, row2, row3):
    print(f'{row1[0]}|{row1[1]}|{row1[2]}\n{row2[0]}|{row2[1]}|{row2[2]}\n{row3[0]}|{row3[1]}|{row3[2]}')

#4) Creating a function to check whether its a tie or not
def checkTie(row1,row2,row3):
    if(row1[0]!=' ' and row1[1]!=' ' and row1[2]!=' ' and row2[0]!= ' ' and row2[1]!= ' ' and row2[2]!=' ' and row3[0]!=' ' and row3[1]!= ' ' and row3[2]!=' '):
        print("It's a Tie!")
        return True
    else:
        return False
    
#5) Creating a function for gameplay logic
def gamePlaying():
    playerSymbolTuple = userInputXOSelection()
    player1Symbol = playerSymbolTuple[0]
    player2Symbol = playerSymbolTuple[1]
    print(f'Player 1 symbol will be {player1Symbol} and player 2 symbol will be {player2Symbol}\n')
    print('For playing the game please refer to the following number pad to mark you sign at appropriate postion in the tic-tac-toe grid.')
    printNumpad()
    row1 = [' ',' ',' ']
    row2 = [' ',' ',' ']
    row3 = [' ',' ',' ']
    flag =0
    while(flag==0):
        #Player1
        player1Input = int(input(f'Player 1, please enter the position you want to mark {player1Symbol}: '))
        while player1Input not in [1,2,3,4,5,6,7,8,9]:
                print('Sorry!, wrong input please enter again.')
                player1Input = int(input(f'Player 1, please enter the position you want to mark {player1Symbol}: '))
        flagP1=0
        while(flagP1==0):
            if(player1Input<4 and player1Input>0):
                if(row1[player1Input-1]==' '):
                    row1[player1Input-1] = player1Symbol
                    break
                else:
                    print('Sorry!, wrong input please enter again.')
                    player1Input = int(input(f'Player 1, please enter the position you want to mark {player1Symbol}: '))
                    while player1Input not in [1,2,3,4,5,6,7,8,9]:
                        print('Sorry!, wrong input please enter again.')
                        player1Input = int(input(f'Player 1, please enter the position you want to mark {player1Symbol}: '))
                    continue
            elif(player1Input<7 and player1Input>3):
                if(row2[player1Input-4]==' '):
                    row2[player1Input-4] = player1Symbol
                    break
                else:
                    print('Sorry!, wrong input please enter again.')
                    player1Input = int(input(f'Player 1, please enter the position you want to mark {player1Symbol}: '))
                    while player1Input not in [1,2,3,4,5,6,7,8,9]:
                        print('Sorry!, wrong input please enter again.')
                        player1Input = int(input(f'Player 1, please enter the position you want to mark {player1Symbol}: '))
                    continue
            elif(player1Input<10 and player1Input>6):
                if(row3[player1Input-7]==' '):
                    row3[player1Input-7] = player1Symbol
                    break
                else:
                    print('Sorry!, wrong input please enter again.')
                    player1Input = int(input(f'Player 1, please enter the position you want to mark {player1Symbol}: '))
                    while player1Input not in [1,2,3,4,5,6,7,8,9]:
                        print('Sorry!, wrong input please enter again.')
                        player1Input = int(input(f'Player 1, please enter the position you want to mark {player1Symbol}: '))
                    continue
        printUserBoard(row1, row2, row3)
        if(row1[0]==row1[1]==row1[2]==player1Symbol or row2[0]==row2[1]==row2[2]==player1Symbol or row3[0]==row3[1]==row3[2]==player1Symbol or row1[0]==row2[0]==row3[0]==player1Symbol or row1[1]==row2[1]==row3[1]==player1Symbol or row1[2]==row2[2]==row3[2]==player1Symbol or row1[0]==row2[1]==row3[2]==player1Symbol or row1[2]==row2[1]==row3[0]==player1Symbol):
            print('Player 1 wins!')
            break
        if(checkTie(row1,row2,row3)):
            break

        #Player 2
        player2Input = int(input(f'Player 2, please enter the position you want to mark {player2Symbol}: '))
        while player2Input not in [1,2,3,4,5,6,7,8,9]:
                print('Sorry!, wrong input please enter again.')
                player2Input = int(input(f'Player 2, please enter the position you want to mark {player2Symbol}: '))
        flagP2 =0
        while(flagP2==0):
            if(player2Input<4 and player2Input>0):
                if(row1[player2Input-1]==' '):
                    row1[player2Input-1] = player2Symbol
                    break
                else:
                    print('Sorry!, wrong input please enter again.')
                    player2Input = int(input(f'Player 2, please enter the position you want to mark {player2Symbol}: '))
                    while player2Input not in [1,2,3,4,5,6,7,8,9]:
                        print('Sorry!, wrong input please enter again.')
                        player2Input = int(input(f'Player 2, please enter the position you want to mark {player2Symbol}: '))
                    continue
            elif(player2Input<7 and player2Input>3):
                if(row2[player2Input-4]==' '):
                    row2[player2Input-4] = player2Symbol
                    break
                else:
                    print('Sorry!, wrong input please enter again.')
                    player2Input = int(input(f'Player 2, please enter the position you want to mark {player2Symbol}: '))
                    while player2Input not in [1,2,3,4,5,6,7,8,9]:
                        print('Sorry!, wrong input please enter again.')
                        player2Input = int(input(f'Player 2, please enter the position you want to mark {player2Symbol}: '))
                    continue
            elif(player2Input<10 and player2Input>6):
                if(row3[player2Input-7]==' '):
                    row3[player2Input-7] = player2Symbol
                    break
                else:
                    print('Sorry!, wrong input please enter again.')
                    player2Input = int(input(f'Player 2, please enter the position you want to mark {player2Symbol}: '))
                    while player2Input not in [1,2,3,4,5,6,7,8,9]:
                        print('Sorry!, wrong input please enter again.')
                        player2Input = int(input(f'Player 2, please enter the position you want to mark {player2Symbol}: '))
                    continue
        printUserBoard(row1, row2, row3)
        if(row1[0]==row1[1]==row1[2]==player2Symbol or row2[0]==row2[1]==row2[2]==player2Symbol or row3[0]==row3[1]==row3[2]==player2Symbol or row1[0]==row2[0]==row3[0]==player2Symbol or row1[1]==row2[1]==row3[1]==player2Symbol or row1[2]==row2[2]==row3[2]==player2Symbol or row1[0]==row2[1]==row3[2]==player2Symbol or row1[2]==row2[1]==row3[0]==player2Symbol):
            print('Player 2 wins!')
            break
        if(checkTie(row1,row2,row3)):
            break
#6) Creating a function to start game
def startGame():
    flag=1
    while(flag==1):
        print('Welcome to Tic-Tac-Toe Game\n')
        gamePlaying()
        flag = int(input('To play again press 1 or Enter 0 to exit: '))
startGame()    
    
