def drawBoard(board):
    x = len(board)
    y = len(board[0])
    for i in range(x):
        for j in range(y):
            print(board[i][j], end = "|")
        print("\n"+'-+'*y)

def get_diagonal(board):
    nrow = len(board)
    ncol = len(board[0])

    fdiag = [[] for _ in range(nrow + ncol - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -nrow + 1

    for y in range(nrow):
        for x in range(ncol):
            fdiag[x+y].append(board[y][x])
            bdiag[x-y-min_bdiag].append(board[y][x])

    return fdiag, bdiag


# board = [3 * [i] for i in range(4)]
# drawBoard(board)

# fdiag, bdiag = get_diagonal(board)
# print(fdiag)
# print(bdiag)

