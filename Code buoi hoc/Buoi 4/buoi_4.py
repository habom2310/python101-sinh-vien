# Buổi 4: List
# 1.1 Giới thiệu List
'''
Khai báo:
    a = 1
    list1 = [1, 2, 3, 1.2, 'c', "hello world", (1,2), [1, 2, 3]]

- list có thể ko có phần tử nào (list rỗng)
- len(list) trả về số phần tử của list

'''
#1.2 List comprehension
'''
khởi tạo list từ 1 đến 10:
list2 = [i for i in range(10)]

ex1: Sử dụng list comprehension để tạo 1 list có chứa kí tự từ 'a' đến chữ 'm' (sử dụng ord(), chr())

    a_pos = ord('a')
    m_pos = ord('m')
    list3 = [chr(i) for i in range(a_pos, m_pos + 1)]
    print(list3)

list4 = [i for i in range(10) if i%2==0] # tạo 1 list số chẵn từ 0-9
print(list4)

list5 = [i if i%3==0 else i + 100 for i in range(10) if i%2==0]
print(list5)
'''

#2.1. Truy cập phần tử của list
'''
chỉ số dương: chỉ số vị trí của phần tử trong list (bắt đầu từ 0)
list1 = [1, 2, 3, 1.2, 'c', "hello world", (1,2), [1, 2, 3]]
print(list1[7])

chỉ số âm: chỉ số vị trí của phần tử trong list (đếm ngược từ phải qua trái, bắt đầu từ -1)

list1  =  [1, 2, 3, 1.2, 'c', "hello world", (1,2), [1, 2, 3]]
idx dương  0  1  2   3    4         5          6        7
idx âm    -8 -7 -6  -5   -4        -3         -2       -1 
'''

#2.2. Slicing - truy cập nhiều phần tử trong list
'''
list1  =  [1, 2, 3, 1.2, 'c', "hello world", (1,2), [1, 2, 3]]

print(list1[:4]) # lấy 4 phần tử đầu tiên (dùng index dương)
print(list1[2:6]) # lấy 4 phần tử vị trí từ 2 -> 5
print(list1[-4:]) # lấy 4 phần tử cuối (dùng index âm)
print(list1[:]) # lấy tất
print(list1[:7:2]) # step = 2
'''

#3.1. Thêm phần tử
'''
- Thêm 1 phần tử vào vị trí cuối cùng: append()
    list3 = []
    for i in range(10):
        i = i + 10
        list3.append(i)

    print(list3)

- Thêm 1 phần tử vào vị trí bất kì n: insert()
    list4 = [1, 2, 3]
    list4.insert(1, 4)
    print(list4)

- Thêm 1 list vào cuối: extend()
    list5 = [1, 2, 3]
    list6 = [4, 5]
    # muốn list5 thành [1, 2, 3, 4, 5]
    list5.extend(list6)
    print(list5)
'''

#3.1. Vòng lặp và list
'''
- Vòng lặp dùng chỉ số (index)
    list1 = [1, 2, 3, 1.2, 'c', "hello world", (1,2), [1, 2, 3]]

    for idx in range(len(list1)):
        print(f"index = {idx}: value = {list1[idx]}")

- Vòng lặp dùng phần tử
    list1 = [1, 2, 3, 1.2, 'c', "hello world", (1,2), [1, 2, 3]]

    for element in list1:
        print(f"value = {element}")

- Vòng lặp dùng chỉ số - phần tử
    list1 = [1, 2, 3, 1.2, 'c', "hello world", (1,2), [1, 2, 3]]

    for idx, element in enumerate(list1):
        print(f"index = {idx}: value = {element}")
'''

'''
Ex2: Viết chương trình.

- Nhập số n nguyên dương
- Khai báo list a rỗng
- Nhập vào từ bàn phím n số, lưu vào a
- Lặp qua các phần tử của a. In ra:
    - Số lớn nhất - vị trí của nó. 
    - Số nhỏ nhất - vị trí của nó.
    - Tổng - tích các phần tử
(Chạy bằng tay từng dòng code theo dữ liệu nhập vào. Thêm print để kiểm nghiệm kết quả.)

'''
