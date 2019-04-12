from IPython.display import clear_output
import random

def display_board(board):
    print("\n#The current situation on the board is:\n")
    print(" ",board[7]," || ",board[8]," || ",board[9]," ")
    print("=====||=====||=====")
    print(" ",board[4]," || ",board[5]," || ",board[6]," ")
    print("=====||=====||=====")
    print(" ",board[1]," || ",board[2]," || ",board[3]," ")


def player_input():
    p1 = input("\n---->Choose between 'X' or 'O' for Player 1 : ").upper()
    while(p1 != 'X' and p1 != 'O'):
        p1 = input("WRONG INPUT!\nTry again : ").upper()
    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'
    return p1,p2


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] ==  board[8] ==  board[9] == mark) or
    (board[4] ==  board[5] ==  board[6] == mark) or 
    (board[1] ==  board[2] ==  board[3] == mark) or 
    (board[7] ==  board[4] ==  board[1] == mark) or 
    (board[8] ==  board[5] ==  board[2] == mark) or 
    (board[9] ==  board[6] ==  board[3] == mark) or 
    (board[7] ==  board[5] ==  board[3] == mark) or 
    (board[9] ==  board[5] ==  board[1] == mark)) 


def choose_first():
    if random.randint(1,2) == 1:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return board[position] != 'X' and board[position] != 'O'


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board,turn):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Enter Move for "+turn+": "))
    return position    


def replay():
    n=input("--------Do you want to play again??--------\n------Enter yes to continue or no to exit.------").lower()
    if n == 'yes':
        return True
    else:
        return False


print('******** Welcome to Tic Tac Toe!! ********')
board = [' '] * 10
while True:
    player_m1,player_m2=player_input()
    turn = choose_first()
    print("\n---->"+turn + ' will go first!!!')
    
    if input('\n---->Are You Ready?? Yes or No: ').lower() == 'yes':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn =='Player 1':
            
            display_board(board)
            position = player_choice(board,turn)
            place_marker(board,player_m1,position)
            if win_check(board,player_m1):
                print("\n########### Congratulations Player 1 won the Game!! ###########")
                display_board(board)
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("###### The Game is Draw!! ######")
                    break
                else:
                    turn = 'Player 2'
        else:
            
            display_board(board)
            position = player_choice(board,turn)
            place_marker(board,player_m2,position)
            if win_check(board,player_m2):
                print("\n########### Congratulations Player 2 won the Game ###########")
                display_board(board)
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("###### The Game is Draw!! ######")
                    break
                else:
                    turn = 'Player 1'
        

    if not replay():
        break