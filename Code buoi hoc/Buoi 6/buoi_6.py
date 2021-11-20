# Buổi 6 - Dictionary

# 6.1 Khái niệm, khởi tạo
'''
- Cấu trúc dữ liệu đặc trưng là key-value
- Ví dụ:

dict_1 = {
    "key1": {
        "key1": "1",
        "key2": "2"
    },
    "key2": 1,
    "3": 1.2
}

- Khởi tạo bằng dict comprehension
dict_1 = {x: x + 1  for x in range(5)}

- kiểu dữ liêu của key: int, string, ... (immutable datatype)
- kiểu dữ liệu của value: tất cả các loại dữ liệu
'''

# 6.2 Cách truy cập vào phần tử của dictionary
'''
- biết key, muốn lấy value

dict_1 = {
    "key1": {
        "key1": "1",
        "key2": "2"
    },
    "key2": 1,
    "3": 1.2
}
print(dict_1["key1"]) # truy cập dùng key
print(dict_1["key3"]) # bị lỗi do key ko tồn tại
print(dict_1.get("key3")) # trả về None nếu key ko tồn tại
'''

#6.2.1 - Walrus operator (sau python 3.8)
'''
- Gán giá trị trong biểu thức logic

if s := input("nhap vao 1 chuoi"):
    print(s)
else:
    print("chuoi rong")
'''
'''
Ex1: Cho dictionary với key là 1 chữ cái và value là 1 số nguyên. Nhập vào 1 chữ cái, nếu dictionary chưa có key đó thì báo là chưa có, nếu có rồi thì trả về giá trị

d = {"a": 1, "b": 2, "c": 5, "f": 10}
c = input("nhap vao 1 chu cai: ")
## kiem tra input
if value := d.get(c): #neu value khac None
    print(f"gia tri cua key {c} la: {value}")
else:
    print(f"key {c} khong ton tai")

- Ex2: tim so lan xuat hien cua 1 ki tu trong 1 chuoi (cach su dung dict)

count_dict = {}
s = input("nhap vao 1 chuoi")

for c in s:
    if value := count_dict.get(c): #neu value khac None
        count_dict[c] = value + 1 # dem them 1 
    else:
        count_dict[c] = 1
'''

#6.3 Các phương thức thường gặp với dictionary
'''
- get(), dict["<key>"]: truy cập giá trị sử dụng key
- d[key] = value: gán, update giá trị
- Xóa: .pop("<key>")

d = {"a": 1, "b": 2, "c": 5, "f": 10}
d["d"] = 4 # gán giá trị 4 cho key "d"
print(d)
d["d"] = 6 # thay đổi giá trị key "d" thành 6
print(d)
print(d.pop("d"))
print(d)
'''

# 6.4 dict và vòng lặp
'''
lặp với:
- keys
- values
- items: key-value

d = {"a": 1, "b": 2, "c": 1, "f": 10}
for k in d.keys(): # lặp với keys
    print(k, d[k])

for v in d.values(): # lặp với values (ko biết thuộc về key nào)
    print(v)

for k, v in d.items(): # lặp với items
    print(k, v)

Ex2: cho 1 dictionary d, revert d (key - value -> value - key). In ra revert d, nếu ko revert đc (có value trùng nhau) thì in ra -1.
d = {"a": 1, "b": 2, "c": 5, "f": 10}
d = {"a": 1, "b": 2, "c": 1, "f": 10}
d_reversed = {}
can_reversed = True

for k, v in d.items():
    print(k, v)
    if d_reversed.get(v):
        can_reversed = False
        break
    else:
        d_reversed[v] = k

if can_reversed == True:
    print(d_reversed)
else:
    print(-1)
'''

'''
Bài 00: Viết chương trình tính tích value của các phần tử trong một dict
Bài 01: Viết chương trình tìm giá trị lớn nhất và giá trị nhỏ nhất của trường value trong một dict
Bài 02: Viết chương trình sắp xếp các phần tử của dict theo chiều tăng dần của key
Bài 03: Viết chương trình lấy các các giá trị không trùng lặp từ dict
Bài 04: Viết chương trình tìm ra 3 phần tử có key lớn nhất trong dict
Bài 05: Viết chương trình tạo ra dict với lớn hơn 3 phần tử, value của mỗi phần tử là một list có lớn hơn 5 phần tử. Truy cập và in ra phần tử thứ 5 trong phần value của mỗi phần tử trong dict
Bài 06: Viết chương trình lấy ra các phần tử key-value xuất hiện trong cả 2 dict

Bài 07: Viết chương trình tạo dict mới bằng cách trích xuất dữ liệu từ dict ban đầu theo tập các key cho trước
Ví dụ:
dict ban đầu: sampleDict = {"name": "Kelly", "age":25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
Output: {'name': 'Kelly', 'salary': 8000}
Bài 08: Viết chương trình lấy ra top 3 phần tử có giá trị lớn nhất từ dict
Bài 09: Viết hàm đếm số lần xuất hiện các ký tự trong một StringVí dụ: Input: ‘Stringings’ Output: {‘S’: 1, ‘t’: 1, ‘r’: 1, ’i’: 2, ‘n’: 2, ‘g’: 2, ‘s’: 1}
Bài 10: Viết chương trình đếm số lần xuất hiện các từ đơn trong một đoạn văn bản
Bài 11: Viết chương trình để sinh ra dict mới từ list các dict có dạng như trong ví dụ:
Input: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}] Output: {'item1': 1150, 'item2': 300}

'''