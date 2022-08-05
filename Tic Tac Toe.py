import os
clear = lambda: os.system('cls') 

print('Welcome to Tic Tac Toe!')

#the function displaying the gameboard
def game_board(num):
    game_list = ('| '+ num[0] + ' | ' + num[1] + ' | ' + num[2] + ' |\n-------------\n| '+ num[3] + ' | ' + num[4] + ' | ' + num[5] + ' |\n-------------\n| '+ num[6] + ' | ' + num[7] + ' | ' + num[8] + ' |')
    print('Here is the current game board')
    print(game_list)
    
#the function asking players to start a game
def new_game():
    ng = ''
    while ng not in ['Yes','yes','No','no']:
        ng = input("Do you want to start a new game?\nAnswer 'Yes' or 'No' ")
        if ng =='Yes' or ng =='yes':
            return True
        elif ng == 'No' or ng =='no':
            return False
        else:
            clear() 
            print ('Invalid aswer. Please try again.')

#the function allowing players to choose their symbols
def players_symbols():
    player1 = 'wrong'
    player2 = ''
    while player1 not in ['X','O']:
        player1 = input("Let's start this game!\nPlayer1, do you want to be X or O? ")
        if player1 == 'X':
            player2 = 'O'
        elif player1 == 'O':
            player2 = 'X'
        else:
            clear()
            print ('Invalid aswer. Please choose between X and O.')
    print ('Okay! Player1 will go first.')
    return (player1, player2)

#the function asking where to put a symbol
def user_choice(k,num):
    pos = 'wrong'
    while pos not in num or pos == 'X' or pos == 'O':
        pos = input(f'Player{(k % 2) + 1}, your turn to choose an empty field (1-9): ')
        if pos not in num or pos == 'X' or pos == 'O':
            print('Invalid choice! Choose an empty field on the board.')            
    return int(pos) - 1

#the function changing the board
def board_change(num, player_position, players_list, k):
    if k % 2 == 0:
        num [player_position] = players_list[0]
    else:
        num [player_position] = players_list[1]

# the variable to keep game playing
game_on = True
while game_on:
    players_list = players_symbols()
    num = ['1','2','3','4','5','6','7','8','9']
    game_board(num)
    k = 0
    while k < 9:
        player_position = user_choice(k, num)
        board_change(num, player_position, players_list, k)
        clear()
        game_board(num)
        if num[0] == num [1] == num[2] or num[0] == num [3] == num[6] or num[0] == num [4] == num[8] or num[1] == num [4] == num[7] or num[2] == num [4] == num[6] or num[2] == num [5] == num[8] or num[3] == num [4] == num[5] or num[6] == num [7] == num[8]:
            print(f'Player{(k % 2) + 1} won!')
            break
        k += 1
    else:
        print('The game ended in a draw.')
    game_on = new_game()
print ("Okay. See you next time!")