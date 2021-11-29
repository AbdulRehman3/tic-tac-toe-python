# Print Board
# Assign User numbers
# Take Input
# Validate Input
# -- If Q/q quit game
# -- Check if Valid Move
# -- Check if number not taken
# Update Board
# Check for Win
# -- If win display congrats => Quit
# Update Player
# Check If Tie: Quit Game

is_player_1 = True
current_move = 0

game_board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]


def print_board(board):
    for row in board:
        for cell in row:
            print(f"{cell} ", end="")
        print("\r")


def get_active_player_name(active_user):
    current_player_name = "X"
    if not active_user:
        current_player_name = "O"
    return current_player_name


def ask_input(active_user):
    player_name = get_active_player_name(active_user)
    print(f"Player {player_name}", end=" ")
    taken_input = input(f"Please Enter Move Number: ")
    return taken_input


def should_quit(user_command):
    if user_command.lower() == 'q':
        return True
    return False


def is_valid_move(user_command):
    if not user_command.isnumeric():
        print("Only Numbers form 1 to 9 is allowed")
        return False
    if int(user_command) < 1 or int(user_command) > 9:
        print("Only Numbers form 1 to 9 is allowed")
        return False
    return True


def is_slot_filled(slot_point, board):
    if board[slot_point[0]][slot_point[1]] == "-":
        return False
    else:
        print("This Cell has been filled already, choose another number.")
        return True


def fill_slot(slot_point, current_player, board):
    active_user = get_active_player_name(current_player)
    board[slot_point[0]][slot_point[1]] = active_user
    return


def parse_input(user_command):
    adjusted_input = int(user_command) - 1
    column = int(adjusted_input / 3)
    row = (adjusted_input % 3)
    return column, row


def has_user_won(current_player, board):
    player_name = get_active_player_name(current_player)
    if check_winning_row(player_name, board):
        return True
    # check columns
    if check_winning_columns(player_name, board):
        return True
    # check diagonals
    if check_winning_diagonals(player_name, board):
        return True

    return False


def check_winning_row(player_symbol, board):
    for row in board:
        if row[0] == player_symbol and row[1] == player_symbol and row[2] == player_symbol:
            return True
    return False


def check_winning_columns(player_symbol, board):
    # Simple Multiple Checks
    # if board[0][0] == player_symbol and board[1][0] == player_symbol and board[2][0] == player_symbol:
    #     return True
    # if board[0][1] == player_symbol and board[1][1] == player_symbol and board[2][1] == player_symbol:
    #     return True
    # if board[0][2] == player_symbol and board[1][2] == player_symbol and board[2][2] == player_symbol:
    #     return True

    # Programmable Check
    for i in range(3):
        is_win = True
        for j in range(3):
            if board[j][i] != player_symbol:
                is_win = False
                break
        if is_win:
            return True
    return False


def check_winning_diagonals(player_symbol, board):
    if board[0][0] == player_symbol and board[1][1] == player_symbol and board[2][2] == player_symbol:
        return True
    if board[0][2] == player_symbol and board[1][1] == player_symbol and board[2][0] == player_symbol:
        return True
    return False


def announce_winner(current_player, board):
    player_name = get_active_player_name(current_player)
    print_result(f"Congrats, Player {player_name} won the match", board)


def print_result(result_message, board):
    print_board(board)
    print(f"=========> {result_message}!!! <===============")


while current_move < 9:
    print_board(game_board)
    user_input = ask_input(is_player_1)
    if should_quit(user_input):
        print("Game Terminated !!!")
        break
    if not is_valid_move(user_input):
        continue

    parsed_input = parse_input(user_input)
    if is_slot_filled(parsed_input, game_board):
        continue

    fill_slot(parsed_input, is_player_1, game_board)

    # Win Is not possible before Player-X 3 moves [and total 5 moves]
    # Start checking after 4th move (which is indexed 3)
    # Basically for "Optimization"
    if current_move > 3:
        if has_user_won(is_player_1, game_board):
            announce_winner(is_player_1, game_board)
            break

    if current_move == 8:
        print_result("Good Competition, Game Tied", game_board)
        break

    current_move = current_move + 1
    is_player_1 = not is_player_1
