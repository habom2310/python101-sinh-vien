'''
Bài 07: Viết hàm
        def create_matrix(n, m)
    xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j
'''
'''
2 hàng, 3 cột
n hàng, m cột -> n list, mỗi list là 1 hàng có m phần tử
'''
matrix = [[0, 0, 0],[0, 1, 2]]


def create_matrix(m,n): #m hàng, n cột
    array = {} # khi tạo matrix thì dùng list 2 chiều (list trong list)
    for i in range(1,m+1): # loop từ 0
        for j in range(1,n+1): # loop từ 0
            key = str(f"({i},{j})")
            array[key] = i*j
    print(array)
    
create_matrix(2,3)

# Chữa lỗi
def create_matrix(m,n):
    array = []
    for i in range(m): 
        array.append([])
        for j in range(n):
            array[i].append(i*j)
    print(array) 
    print("hang 1:", array[0]) 

create_matrix(2,3)
