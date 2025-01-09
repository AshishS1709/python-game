board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
game_is_playing = True
winner = None


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def turn_specified():
    global current_player
    if current_player == "O":
        print("It's O's Turn...!")
    elif current_player == "X":
        print("It's X's Turn...!")


def handle_turn():
    global current_player
    valid = False
    while not valid:
        try:
            position = int(input("Enter the position of your choice (0 to 8): "))
            if position < 0 or position > 8:
                print("Invalid position. Please choose a position between 0 and 8.")
            elif board[position] != "-":
                print("Position already occupied. Please choose a different position.")
            else:
                board[position] = current_player
                valid = True
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")


def swap_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def check_the_winner():
    global winner
    row_winner = check_row()
    col_winner = check_col()
    dia_winner = check_dia()

    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif dia_winner:
        winner = dia_winner


def check_row():
    global game_is_playing
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_is_playing = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def check_col():
    global game_is_playing
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        game_is_playing = False

    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]


def check_dia():
    global game_is_playing
    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[2] == board[4] == board[6] != "-"

    if dia_1 or dia_2:
        game_is_playing = False

    if dia_1:
        return board[0]
    elif dia_2:
        return board[2]


def check_tie():
    global game_is_playing
    if "-" not in board and winner is None:
        print("Match ended with a tie....!")
        game_is_playing = False


def play_game():
    while game_is_playing:  # while True:
        display_board()
        print()
        turn_specified()
        handle_turn()
        check_the_winner()
        check_tie()
        if not game_is_playing:
            break
        swap_player()

    # Display the final board
    print("\nFinal Board:")
    display_board()

    # Announce the winner or tie
    if winner == "X" or winner == "O":
        print(f"\nCongratulations! The winner is {winner}.")
    elif winner is None:
        print("\nThe game ended in a tie.")


play_game()
