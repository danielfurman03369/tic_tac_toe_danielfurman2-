wins = [0,0]

def create_board() -> list:
    '''
    creates a list for the board positions
    :return: list of positions
    '''
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return board

def print_board(list):
    '''
    prints the board
    :param list: the board positions
    :return: prints the poard
    '''
    print()
    print('╔═══╦═══╦═══╗')
    print(f'║ {list[0]} ║ {list[1]} ║ {list[2]} ║')
    print('╠═══╬═══╬═══╣')
    print(f'║ {list[3]} ║ {list[4]} ║ {list[5]} ║')
    print('╠═══╬═══╬═══╣')
    print(f'║ {list[6]} ║ {list[7]} ║ {list[8]} ║')
    print('╚═══╩═══╩═══╝')
    print()

def get_move(player, board) -> str | None:
    '''
    gets an input from the user and checks if it in the board list
    if not asks to enter a valid position (1-9)
    :param player: the symbol of the current player
    :param board: list of positions
    :return: returns the valid checked position
    '''
    while True:
        position = input(f'player {player} pls enter your move: ')
        if position == 'r' or position == 'R':
            return 'r'
        elif position != 'X' and position != 'O':
            if position in board:
                return position
            else:
                print('please enter a valid position')
        else:
            print('please enter a valid position')
            continue

def make_move(board, position, symbol):
    '''
    makes a move on the board by subtracting 1 from the inputed position
    to find the index of that position

    :param board: list of positions
    :param position: the current player chosen position
    :param symbol: list of symbols
    :return:
    '''
    board[int(position)-1] = symbol
    print_board(board)

def switch_player(current) -> int:
    '''
    swiches the current player by toggeling the index between 1 and 0
    :param current: index of current player
    :return: index of next player
    '''
    current = (current + 1) % 2
    return current

def check_winner(board, symbol) -> bool:
    '''
    checks all possible winner combos
    and if they exist returns true else returns false
    :param board: list of positions
    :param symbol: list of symbols
    :return:bool -> True or False
    '''
    wins = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == symbol:
            return True
    return False

def is_tie(board) -> bool:
    '''
    check if there is a tie by checking if any items on the
    list (board) are digits if yes the game hasent ended
    if no and it was not a win this function runs
    :param board: list of positions
    :return: bool -> True or False
    '''
    if any(item.isdigit() for item in board):
        return False
    else:
        return True

def reset_game(player, current) -> list:
    '''
    prints the player who reset the game then switches
    the player and adds 1 to his wins then prints the total score
    and prints and returns the new board
    :param player: list of the symbols representing the players
    :param current: int
    :return: list (new_board)
    '''
    print(f'Player {player[current]} has reset the game as a penalty the other player gets a point')
    current = switch_player(current)
    wins[current] += 1
    print_total()
    new_board = create_board()
    print_board(new_board)
    return new_board

def play_game():
    '''
    plays the main game loop of tic tac toe and calls all the functions
    :return: none
    '''
    players: list = ['X', 'O']
    current_pl: int = 0
    position: str = '_'
    board = create_board()
    print_board(board)

    while True:
        position = get_move(players[current_pl], board)
        if position == 'r':
            board = reset_game(players, current_pl)
            current_pl = 0
            continue
        make_move(board, position, players[current_pl])
        if check_winner(board, players[current_pl]):
            print(f'Player {players[current_pl]} wins!')
            wins[current_pl] += 1
            break
        elif is_tie(board):
            print('its a tie!')
            break
        current_pl = switch_player(current_pl)

def play_again() -> bool | None:
    '''
    asks the player if they want to play again and validates the answer to get y or n only
    after that returns True or False to reset the game
    :return: bool -> True or False
    '''
    while True:
        a = input('would you like to start a new game? (y/n): ')
        if a.isalpha():
            a = a.lower()
            if a == 'y':
                return True
            elif a == 'n':
                print('alright good bye!')
                return False
            else:
                print('please enter y or n')
                continue
        else:
            print('please enter y or n')
            continue

def print_total():
    '''
    prints out the total number of wins for both players
    :return: None
    '''
    print('╔══════════════════╗')
    print('║   ✖        〇    ║')
    print(f'║   {wins[0]}         {wins[1]}    ║')
    print('╚══════════════════╝')


# main code

to_play = True
print('hello!! welcom to my tic tac toe game hope u enjoy!'
      'pls enter one of the nums you see on the board!')
while to_play:
    play_game()
    print_total()
    to_play = play_again()



