N = 8
board = [[0] * N for _ in range(N)]
def isSafe(row, col):
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
def solveNQUtil(col):
    if col >= N:
        return True
    for i in range(N):
        if isSafe(i, col):
            board[i][col] = 1
            if solveNQUtil(col + 1):
                return True
            board[i][col] = 0
    return False
def printSolution():
    for i in range(N):
        print(" ".join(str(x) for x in board[i]))
if __name__ == "__main__":
    if solveNQUtil(0):
        printSolution()
    else:
        print("Solution does not exist")
