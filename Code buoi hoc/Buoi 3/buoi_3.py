# Buổi 3: Cấu trúc lặp

#1. Cấu trúc "for"
'''
for i in range(5):
    print("Hello")

Ex1: 
- tính tổng các số từ 1 đến 10
- tính tổng các số lẻ

in ra màn hình giá trị i và giá trị tạm thời của biến tổng


- Hàm range:
range(stop): từ 0 đến stop - 1
range(start, stop): từ start đến stop - 1
range(start, stop, step): từ start đến stop - 1, các giá trị cách nhau 1 step

global variable
local variable

1.2 Lặp với iterable
a = [1, 2, 3, 4, 5, 'a', 1.2]

for element in a:
    print(element)

for i, v in enumerate(a):
    print(i, v)
'''

# Cấu trúc While
'''
i = 0
while i < 10:
    print(i)
    i = i + 1 

Ex2: 
- viết 1 chương trình yêu cầu nhập vào 1 chuỗi có 2 kí tự trở lên, nếu sai thì bắt nhập lại, nếu đúng thì in ra màn hình chuỗi vừa nhập.

check độ dài của 1 chuỗi, mảng: len()

Ex3:
- Yêu cầu nhập tuổi, nếu sai thì bắt nhập lại, đúng thì in ra màn hình.
check 1 số trường hợp: abc, 1a, a1, 0, 20
'''

#3. Điều khiển vòng lặp
'''
in ra các số chia hết cho 2, bỏ qua các số ko chia hết cho 2, thoát vòng lặp khi phần tử ko phải số

l = [1, 2, 3, 4, 5, 'a', 7, 'b']

for element in l:
    print("phan tu hien tai la:",element) # debug
    if type(element) != int: # neu ko phai la so 
        print(element, "ko phai la so, thoat chuong trinh")
        break
    elif element % 2 != 0: # neu chia het cho 2 
        print(element, "ko chia het cho 2, bo qua sang phan tu tiep theo")
        continue
    else:
        print(element, "chia het cho 2")
'''






