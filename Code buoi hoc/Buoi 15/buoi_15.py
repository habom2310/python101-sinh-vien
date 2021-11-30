import numpy as np

a = np.array(  [["x", " ", " ", " ", " ", " ", "x"], 
                [" ", "x", "o", "x", "x", "x", "o"], 
                [" ", "o", "x", "x", "x", "o", "x"],
                [" ", "o", "o", "o", "x", "x", "x"],
                [" ", "x", "o", "x", "o", "x", "o"],
                [" ", "o", "o", "x", "x", "x", "x"],
                [" ", "o", "o", "x", "x", "o", "x"]])


diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]

# Now back to the original array to get the upper-left-to-lower-right diagonals,
# starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

# Another list comp to convert back to Python lists from numpy arrays,
# so it prints what you requested.
print([n.tolist() for n in diags])

# def get_diagonal(board):
#     nrow = len(board)
#     ncol = len(board[0])

#     fdiag = [[] for _ in range(nrow + ncol - 1)]
#     bdiag = [[] for _ in range(len(fdiag))]
#     min_bdiag = -nrow + 1

#     for y in range(nrow):
#         for x in range(ncol):
#             fdiag[x+y].append(board[y][x])
#             bdiag[x-y-min_bdiag].append(board[y][x])

#     return fdiag, bdiag


# fdiag, bdiag = get_diagonal(list_2D)
# for f in fdiag:
#     print(f)
# for b in bdiag:
#     print(b)

# def check_row(board):
#     """
#     Check xem có 5 ô cùng hàng chứa kí tự giống nhau hay ko.
#     """
#     for row in board:
#         #cắt 5 kí tự liền nhau trong mỗi row
#         for i in range(len(row)-4):
#             # print(row[i:i+5])
#             slice = row[i:i+5]
#             #kiểm tra xem mỗi slice có 5 kí tự giống nhau ko (khác " ")
#             if " " in slice:
#                 continue
#             else:
#                 if slice.count("x") == 5 or slice.count("o") == 5:
#                     return True

#     return False

# # print(check_row(list_2D))

# def check_col(board):
#     """
#     Check xem có 5 ô cùng cột chứa kí tự giống nhau hay ko.
#     """
#     cols = []
#     for i in range(len(board)):
#         col = []
#         for row in board:
#             col.append(row[i])
#         cols.append(col)
#     print(cols)

#     return check_row(cols)

# print(check_col(list_2D))
    

# nrow = 10
# ncol = 10

# def create_board(nrow = 10, ncol = 10):
#     array = [[0] * ncol for _ in range(nrow)]
#     return array

# print(create_board())

# def draw_board(board):
#     for row in board:
#         for element in row:
#             print(str(element),end="|")
#         print("\n" + "-+"*len(row))
# draw_board(list_2D)