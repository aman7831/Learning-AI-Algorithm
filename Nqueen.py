def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_valid(board, row, col):
    # check if no queen threatens the placed queen
    for i in range(col):
        if board[row][i] == "Q":
            return False
    # check upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    # check lower diagonal
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1
    return True

def n_queens(board, col):
    if col == len(board):
        print_board(board)
        return True
    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = "Q"
            if n_queens(board, col + 1):
                return True
            board[i][col] = "."
    return False

def solve_n_queens(n):
    board = [["." for j in range(n)] for i in range(n)]
    if not n_queens(board, 0):
        print("Solution does not exist.")

solve_n_queens(4)
