from math import inf as infinity

game_board = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']]
symbols = ['X','O']

def make_move(board, symbol, position):
    if board[int((position-1)/3)][(position-1)%3] == ' ':
        board[int((position-1)/3)][(position-1)%3] = symbol
    else:
        position = int(input("Space is not empty, choose again: "))
        make_move(board, symbol, position)
    
def copy_board(board):
    new_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for i in range(3):
        for j in range(3):
            new_board[i][j] = board[i][j]
    return new_board
    
def check_state(game_board):
    
    
    # Check horizontals
    if (game_board[0][0] == game_board[0][1] and game_board[0][1] == game_board[0][2] and game_board[0][0] != ' '):
        return game_board[0][0], "Done"
    if (game_board[1][0] == game_board[1][1] and game_board[1][1] == game_board[1][2] and game_board[1][0] != ' '):
        return game_board[1][0], "Done"
    if (game_board[2][0] == game_board[2][1] and game_board[2][1] == game_board[2][2] and game_board[2][0] != ' '):
        return game_board[2][0], "Done"
    
    # Check verticals
    if (game_board[0][0] == game_board[1][0] and game_board[1][0] == game_board[2][0] and game_board[0][0] != ' '):
        return game_board[0][0], "Done"
    if (game_board[0][1] == game_board[1][1] and game_board[1][1] == game_board[2][1] and game_board[0][1] != ' '):
        return game_board[0][1], "Done"
    if (game_board[0][2] == game_board[1][2] and game_board[1][2] == game_board[2][2] and game_board[0][2] != ' '):
        return game_board[0][2], "Done"
    
    # Check diagonals
    if (game_board[0][0] == game_board[1][1] and game_board[1][1] == game_board[2][2] and game_board[0][0] != ' '):
        return game_board[1][1], "Done"
    if (game_board[2][0] == game_board[1][1] and game_board[1][1] == game_board[0][2] and game_board[2][0] != ' '):
        return game_board[1][1], "Done"
    
    # Check if draw
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if game_board[i][j] == ' ':
                draw_flag = 1
    if draw_flag == 0:
        return None, "Draw"
    
    return None, "Not Done"

def print_board(game_board):
    print('----------------')
    print('| ' + str(game_board[0][0]) + ' || ' + str(game_board[0][1]) + ' || ' + str(game_board[0][2]) + ' |')
    print('----------------')
    print('| ' + str(game_board[1][0]) + ' || ' + str(game_board[1][1]) + ' || ' + str(game_board[1][2]) + ' |')
    print('----------------')
    print('| ' + str(game_board[2][0]) + ' || ' + str(game_board[2][1]) + ' || ' + str(game_board[2][2]) + ' |')
    print('----------------')
    
    
def get_best_move(board, symbol):
    #Minimax Algorithm
    
    winner_loser , done = check_state(board)
    if done == "Done" and winner_loser == 'O': # If AI won
        return (1,0)
    elif done == "Done" and winner_loser == 'X': # If Human won
        return (-1,0)
    elif done == "Draw":    # Draw condition
        return (0,0)
        
    moves = []
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_cells.append(i*3 + (j+1))
    
    for empty_cell in empty_cells:
        move = {}
        move['index'] = empty_cell
        new_board = copy_board(board)
        make_move(new_board, symbol, empty_cell)
        
        if symbol == 'O':    # If AI
            result,_ = get_best_move(new_board, 'X')    # make more depth tree for human
            move['score'] = result
        else:
            result,_ = get_best_move(new_board, 'O')    # make more depth tree for AI
            move['score'] = result
        
        moves.append(move)

    # Find best move
    best_move = None
    if symbol == 'O':   # If AI symbol
        best = -infinity
        for move in moves:            
            if move['score'] > best:
                best = move['score']
                best_move = move['index']
    else:
        best = infinity
        for move in moves:
            if move['score'] < best:
                best = move['score']
                best_move = move['index']
                
    return (best, best_move)

# Playing
play_again = 'Y'
while play_again == 'Y' or play_again == 'y':
    game_board = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']]
    current_state = "Not Done"
    print("\nNew Game!")
    print_board(game_board)
    symbol_choice = input("Choose which symbol goes first - X (You) or O(The AI): ")
    winner = None
    
    if symbol_choice == 'X' or symbol_choice == 'x':
        current_symbol_idx = 0
    else:
        current_symbol_idx = 1
        
    while current_state == "Not Done":
        if current_symbol_idx == 0: # Human's turn
            position_choice = int(input("Your turn! Choose where to place (1 to 9): "))
            make_move(game_board ,symbols[current_symbol_idx], position_choice)
        else:   # AI's turn
            _,position_choice = get_best_move(game_board, symbols[current_symbol_idx])
            make_move(game_board ,symbols[current_symbol_idx], position_choice)
            print("AI plays move: " + str(position_choice))
        print_board(game_board)
        winner, current_state = check_state(game_board)
        if winner is not None:
            print(str(winner) + " won!")
        else:
            current_symbol_idx = (current_symbol_idx + 1)%2
        
        if current_state == "Draw":
            print("Draw!")
            
    play_again = input('Wanna try again?(Y/N) : ')
    if play_again == 'N':
        print('GG!')