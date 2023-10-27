import numpy

board = [[0, 4, 0, 2, 8, 0, 1, 7, 0],               
         [0, 0, 0, 0, 4, 6, 8, 9, 0],
         [0, 1, 0, 0, 0, 0, 6, 0, 0],
         [1, 0, 0, 0, 0, 0, 0, 8, 0],
         [0, 0, 0, 6, 5, 2, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 0, 7],
         [0, 0, 7, 0, 0, 0, 0, 5, 0],
         [0, 6, 4, 7, 2, 0, 0, 0, 0],
         [0, 2, 1, 0, 9, 3, 0, 4, 0]]

def valid(x, y, n, board):
    count = 0
    for i in range(9):
        if board[x][i] == n:
            count += 1
        if board[i][y] == n:
            count += 1
    xgrid = (int(x/3) + 1) * 3
    ygrid = (int(y/3) + 1) * 3
    for j in range(xgrid-3, xgrid):
        for k in range(ygrid-3, ygrid):
            if board[j][k] == n:
                count += 1
    if count == 0:
        return True
    else:
        return False

def solve_sudoku(board):
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                for i in range(1, 10):
                    if valid(x, y, i, board):
                        board[x][y] = i
                        if solve_sudoku(board):
                            return board
                        board[x][y] = 0
                return
    return board


print(numpy.matrix(solve_sudoku(board)))
