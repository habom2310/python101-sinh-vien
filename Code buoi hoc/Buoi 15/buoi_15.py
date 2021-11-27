list_2D =  [["x", " ", "x", " "], 
            [" ", "o", "o", "x"], 
            ["x", "o", " ", "x"]]

nrow = 10
ncol = 10

def create_board(nrow = 10, ncol = 10):
    array = [[0] * ncol for _ in range(nrow)]
    return array

print(create_board())

# def draw_board(board):
#     for row in board:
#         for element in row:
#             print(str(element),end="|")
#         print("\n" + "-+"*len(row))
# draw_board(list_2D)