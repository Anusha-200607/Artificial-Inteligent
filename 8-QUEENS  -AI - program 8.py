N = 8

def print_solution(board):
    for row in board:
        print(" ".join("Q" if x else "." for x in row))
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

def solve_n_queens(board, col):
    if col >= N:
        print_solution(board)
        return True
    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_n_queens(board, col + 1) or res
            board[i][col] = 0
    return res

def eight_queens():
    board = [[0]*N for _ in range(N)]
    solve_n_queens(board, 0)

print("\n8 Queens Problem")
print("----------------")
eight_queens()
