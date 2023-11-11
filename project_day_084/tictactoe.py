# tictactoe.py - Text-based console Tic Tac Toe game

squares = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

player = {"X": input('Enter first player name, who will use "X": '),
          "O": input('Enter second player name, who will use "O": ')}
current_player = "X"


def spaces_free():
    count = 0
    for square in squares:
        if square != 'X' and square != 'O':
            count += 1
    return count


def print_board():
    board = f"""
     {squares[0]} | {squares[1]} | {squares[2]}
    ----------
     {squares[3]} | {squares[4]} | {squares[5]}
    ----------
     {squares[6]} | {squares[7]} | {squares[8]}"""

    print(board)


def update_board(choice):
    squares[choice] = current_player


def switch_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_for_win():
    count = 0
    sequences = [[0, 3, 1], [3, 6, 1], [6, 9, 1], [0, 7, 3], [1, 8, 3], [2, 9, 3], [0, 9, 4], [2, 7, 2]]
    for sequence in sequences:
        for i in range(sequence[0], sequence[1], sequence[2]):
            if squares[i] == current_player:
                count += 1
        if count == 3:
            return True
        count = 0
    return False


def is_taken(choice):
    return squares[choice] == 'X' or squares[choice] == 'O'


while spaces_free():
    print_board()
    choice = input(f"{player[current_player]}, please place an {current_player} on the board by entering the "
                   f"number of any available space: ")
    try:
        choice = int(choice)
        if choice not in range(1, 10) or is_taken(choice-1):
            continue
    except ValueError:
        continue

    update_board(choice-1)
    if check_for_win():
        print_board()
        print(player[current_player] + " wins!")
        exit(0)

    switch_player()

print_board()
print("Game ended in draw")
