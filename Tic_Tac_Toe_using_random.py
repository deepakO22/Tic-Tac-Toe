# Tic Tac Toe Game with AI

game_board = [' ' for x in range(10)]


def update_board(letter, pos):
    global game_board
    game_board[pos] = letter


def is_space_free(pos):
    return game_board[pos] == ' '


def is_winner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))


def player_move():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if 0 < move < 10:
                if is_space_free(move):
                    run = False
                    update_board('X', move)
                else:
                    print('This position is already occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def select_random_item(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def computer_move():
    possible_moves = [x for x, letter in enumerate(game_board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possible_moves:
            board_copy = game_board[:]
            board_copy[i] = let
            if is_winner(board_copy, let):
                move = i
                return move

    corners_open = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            corners_open.append(i)
    if len(corners_open) > 0:
        move = select_random_item(corners_open)
        return move

    if 5 in possible_moves:
        move = 5
        return move

    edges_open = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            edges_open.append(i)

    if len(edges_open) > 0:
        move = select_random_item(edges_open)

    return move


def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def print_game_board():
    print('   |   |')
    print(' ' + game_board[1] + ' | ' + game_board[2] + ' | ' + game_board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + game_board[4] + ' | ' + game_board[5] + ' | ' + game_board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + game_board[7] + ' | ' + game_board[8] + ' | ' + game_board[9])
    print('   |   |')


def play_game():
    print('Welcome to Tic Tac Toe, to win complete a straight line of your letter (Diagonal, Horizontal, Vertical). The board has positions 1-9 starting at the top left.')
    print_game_board()

    while not(is_board_full(game_board)):
        if not(is_winner(game_board, 'O')):
            player_move()
            print_game_board()
        else:
            print('O\'s win this time...')
            break

        if not(is_winner(game_board, 'X')):
            move = computer_move()
            if move == 0:
                print('Game is a Tie! No more spaces left to move.')
            else:
                update_board('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                print_game_board()
        else:
            print('X\'s win, good job!')
            break

    if is_board_full(game_board):
        print('Game is a tie! No more spaces left to move.')


def play_again():
    while True:
        answer = input('Do you want to play again? (Y/N)')
        if answer.lower() == 'y' or answer.lower() == 'yes':
            global game_board
            game_board = [' ' for x in range(10)]
            print('-----------------------------------')
            play_game()
        else:
            break


play_game()
play_again()
