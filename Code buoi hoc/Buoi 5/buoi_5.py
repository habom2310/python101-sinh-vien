#5. String

'''
5.1 Khai báo
a = 'abc'
b = "abc"
c = """dong 1
dong2
dong3
...
"""
'''

'''
5.2 Truy cập
a = "Hello"

element     H   e   l   l   o
index +     0   1   2   3   4
index -    -5  -4  -3  -2  -1

a = "Hello"
print(a[1])
print(a[1:4])
print(a[-3:-1])

String là kiểu dữ liệu immutable
a = "2"
print(a, id(a), id("2"))
a = "3"
print(a, id(a), id("3")) 
'''

'''
Escape sequence
\n xuống dòng
\t tab 1 đoạn

VD: 
a = 'I\'m Ha'
print(a)

'''

'''
5.3 các phương thức thường gặp với string

- kiểm tra độ dài: len()
- nối 2 string: +
a = "hello"
b = "world"
c = a + " " + b 
print(c)

- nhân bản (duplicate) string: * (int)
a = "hello"
b = a * 2
print(b) 

- lower(): biến chữ hoa thành chữ thường

a = "Hello"
b = a.lower()
print(b)

- upper(): biến chữ thường thành chữ hoa

a = "Hello"
b = a.upper()
print(b)

- split(): tách các từ trong string (cách nhau bởi dấu cách (mặc định)) -> trả về 1 list các từ 
a = "Hello world 123 456"
b = a.split()
print(b) 
>>> ['Hello', 'world', '123', '456']

- split("<kí tự tách (delimiter)>"): tách từ theo kí tự
a = "Hello-world-123-456"
b = a.split("-")
print(b) 
>>> ['Hello', 'world', '123', '456']

- "<kí tự nối>".join(<list các từ>): nối các từ lại cách nhau bởi kí tự nối -> trả về string
a = ['Hello', 'world', '123', '456']
b = " ".join(a)
print(b)

- replace("<old str>", "<new str>"): thay thế str cũ thành str mới

Ex1: cho string: 
s = '\tHello \tmoi nguoi, I\'m Ha\n'

1. split, join lại cách nhau bởi dấu '-', print ra.
2. bỏ hết \t \n

['Hello', 'moi', 'nguoi,', "I'm", 'Ha']

3. biến thành: "Hello moi nguoi. I'm Ha"

Ex2: viết 1 chương trình tìm kiếm chuỗi:
- nhập 1 chuỗi (ko có dấu) lưu vào biến s
- đếm số lần xuất hiện của các kí tự trong s (dùng list)
- Tìm kiếm vị trí của 1 kí tự trong chuỗi (hỏi nhập vào kí tự cần tìm), nếu k thấy thì hiển thị -1
- tìm vị trí xuất hiện đầu tiên và cuối cùng, nếu ko tìm ra thì hiển thị -1
'''


