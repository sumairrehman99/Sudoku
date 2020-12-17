board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(game_board):
    for i in range(len(game_board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")

        for j in range(len(game_board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(game_board[i][j])
            else:
                print(str(game_board[i][j]) + " ", end=" ")


# finds the first empty spot in the row
def find_empty(game_board):
    for row in game_board:
        for position in row:
            if position == 0:
                return game_board.index(row), row.index(position)

    return None


def valid_board(game_board, number, position):
    isValid = True
    # checks row
    for i in range(len(game_board[0])):
        if game_board[position[0]][i] == number and position[1] != i:
            isValid = False

    # checks column
    for j in range(position[1] + 1):
        if game_board[j][position[1]] == number:
            isValid = False

    # check box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if game_board[i][j] == number and (i, j) != position:
                isValid = False

    return isValid


def solve(game_board):
    empty_square = find_empty(game_board)

    if not empty_square:
        return True
    else:
        row, col = empty_square

    for i in range(1,10):
        if valid_board(game_board, i, (row,col)):
            game_board[row][col] = i

            if solve(game_board):
                return True

            game_board[row][col] = 0

    return False



solve(board)
print_board(board)
