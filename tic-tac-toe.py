import random

def show_board(board):
    '''
        Take an arry as input and displays a representation of it as a tic tac toe board.
        board must either be 'O', 'X' or ' ' 
    '''

    print('       |       |')
    print('   {}   |   {}   |   {}   '.format(board[6],board[7],board[8]))
    print('-------|-------|-------')
    print('   {}   |   {}   |   {}   '.format(board[3],board[4],board[5]))
    print('-------|-------|-------')
    print('   {}   |   {}   |   {}   '.format(board[0],board[1],board[2]))
    print('       |       |')

def player_input():
    print('Welcome to Tic Tac Toe!')
    player1 = input('player1: choose X or O? ').upper()
    player2 = 'X' if player1 == 'O' else 'O'
    return (player1,player2)

def place_marker(board,marker):
    position = 0
    while position not in range(1,10):
        try:
            position = int(input('{}({}): What is your move (1-9)? '.format(current_player,mark)))
            if board[position - 1] != ' ':
                position = 0
                raise
        except:
            print('Not valid')

    board[position - 1] = marker
    return board

def win_check(board,mark):
    # Check columns
    for num in range(3):
        if board[num] == board[num+3] == board[num+6] == mark:
            return True
    
    #Check rows
    for num in range(0,7,3):
        if board[num] == board[num+1] == board[num+2] == mark:
            return True

    if board[0] == board[4] == board[8] == mark:
        return True

    if board[2] == board[4] == board[6] == mark:
        return True
    
    return False

def draw_check(board,mark1,mark2):
    if (board.count(mark1) + board.count(mark2)) == 9:
        return True
    return False

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

player_switch = {
    'player1':'player2',
    'player2':'player1'
}

player1mark,player2mark = player_input()

current_player = random.choice(list(player_switch))
print('{} goes first\n'.format(current_player))

while True:
    mark = player1mark if current_player == 'player1' else player2mark

    show_board(board)
    
    board = place_marker(board,mark)
    
    if win_check(board,mark):
        show_board(board)
        print('Congratulations {}, you have won!'.format(current_player))
        break
    elif draw_check(board,player1mark,player2mark):
        show_board(board)
        print('Game is tied!')
        break

    current_player = player_switch[current_player]
