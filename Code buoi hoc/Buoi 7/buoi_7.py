# Buổi 7 - Tuple - set

## 7.1 Tuple
'''
t = (1, "a", [1, 1.2])

tại sao lại có tuple vs list:
- size: tuple < list -> tuple nhanh hơn khi có nhiều phần tử

t = (1, 2, 3)
l = [1, 2, 3]

print(t.__sizeof__())
print(l.__sizeof__())

- coding convention: tuple chứa các phần tử khác loại (datatype), list chứa các phần tử cùng loại

- Debug: tuple thường dùng trong debug vì giá trị phần tử không đổi

- Ứng dụng: để return giá trị khác loại trong 1 hàm

- Khởi tạo tuple 1 phần tử
t = (1,)
print(t, type(t))

- Packing - unpacking
#Packing
t = 1, 2, 3
print(t, type(t))

#Unpacking
a, b, c = t
print(a, b, c)

t = 1, 2, 3, 4, 5
a, *b = t
print(a, type(a))
print(b, type(b))

*a, b = t
print(a, type(a))
print(b, type(b))

a, *b, c = t
print(a, type(a))
print(b, type(b))
print(c, type(c))

- slicing: giống list, trả về tuple
t = 1, 2, 3, 4, 5
print(t[0:1])

- Tuple chứa các phần tử immutable (ko bị thay đổi giá trị) nên ko có thêm (append/ insert),sửa, xóa (del/pop)

mutable  /  immutable 
id ko doi   id thay doi
list        string
dict        int
            float
            tuple

Ex1: cho tuple: t = 1, 2, 3, "a", "b"
1. slicing từ t ra: ("a", "b")
2. +, *, slicing tạo ra ("a", "b", "a", "b", 1, 2, 3)
'''

#7.2 Set
'''
- Chứa các phần tử bất biến (immutable)
- Các phần tử trong set là độc nhất

- Khởi tạo: ngoặc nhọn {}
s = {1, 2, 3}
print(s, type(s))

# khai báo từ 1 list: set()
l = [1, 2, 3]
s = set(l)
print(s)

# kiểm tra xem 1 phần tử có trong set ko
print(2 in s) -> True/False

for element in s: #truy cập phần tử
    print(element)

- Ứng dụng:
1. lọc các phần tử lặp
l = [1, 2, 3, 1, 2, 2]
s = set(l)
print(s)

2. tìm giao (các phần tử xuất hiện ở cả 2 hoặc nhiều tập). x.intersection(y, z): AND
l1 = [1, 2, 3, 1, 2, 2]
l2 = [2, 4, 5, 7, 2, 3]

s1 = set(l1)
s2 = set(l2)
print(s1)
print(s2)

intersect = s1.intersection(s2)
print(intersect)

3. tìm hợp (các phần tử có mặt, có trong ít nhất 1 tập). x.union(y, z): OR
l1 = [1, 2, 3, 1, 2, 2]
l2 = [2, 4, 5, 7, 2, 3]

s1 = set(l1)
s2 = set(l2)
print(s1)
print(s2)

union = s1.union(s2)
print(union)

Ex2: 
Nhập n số từ bàn phím. Sử dụng set để in ra các phần tử phân biệt

'''

"""
BTVN

1. Viết chương trình đảo ngược một tuple
2. Viết chương trình đếm số lượng các phần tử trong một list đến khi gặp một phần tử kiểu tuple.
3. Viết chương trình tìm ra tuple có phần tử thứ 2 là nhỏ nhất từ một list chứa các tuple.
4. Viết chương trình tính tổng và tìm giá trị lớn nhất trong tuple chứa các số thực.

1. Viết chương  trình đếm số lượng kí tự phân biệt từ một chuỗi nhập vào từ bàn phím sử dụng Set

2. Khởi tạo 2 List có n phần tử kí tự 'a' - 'z'. Tìm phần tử chung giữa 2 list đó với:
a. n = 10
b. n = 100
c. n = 1000000

3. Đếm số key:val trùng lặp trong 2 dictionary
"""


