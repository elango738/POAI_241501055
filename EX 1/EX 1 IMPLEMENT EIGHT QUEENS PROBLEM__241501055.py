
# Eight Queens Problem using Backtracking

N = 8

def print_solution(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print()

def is_safe(board, row, col):
    for i in range(col):
        if board[row][i]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j]:
            return False
    return True

def solve_nqueens(board, col):
    if col >= N:
        print_solution(board)
        return True
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve_nqueens(board, col + 1):
                return True
            board[i][col] = 0
    return False

def eight_queens():
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens(board, 0):
        print("Solution does not exist.")

eight_queens()
