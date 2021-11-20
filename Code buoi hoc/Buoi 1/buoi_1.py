#1. Giá trị, kiểu dữ liệu và biến

'''
- Số nguyên (int): 1, 2, 3
- Số thực (float): 0.2
- Chuỗi (string): "Hello world"

floating point, dấu phẩy động, biểu diễn số trong hệ cơ sở

code convention:
- Tên biến thể hiện đúng mục đích
- nếu tên biến có nhiều hơn 2 từ, thì mỗi từ  cách nhau bởi 1 dấu "_" (underscore). VD: thu_nhap_hang_thang
- các thành phần trong 1 dòng code cách nhau một dấu cách. VD: x = 1
- Cách đặt tên biến:
    + có phân biệt hoa vs thường: Abc # abc
    + không chứa kí tự đặc biệt: abc@!
    + không bắt đầu bằng số: 1abc
    + không dùng các từ khóa đặc biệt của python: int, float, class ...
'''

#2. Các câu lệnh nhập xuất đơn giản

'''
Câu lệnh xuất: print()
- gán giá trị vào string khi print: print(f"giá trị của a là {a}")
- Có thể ghép nhiều phần từ các kiểu dữ liệu khác nhau trong print. VD: print("năm nay tôi", 27, "tuổi")

Câu lệnh nhập: input()
- Giá trị input vào là kiểu string
- VD: age = input("nhập vào số tuổi của bạn: ")

Ép kiểu dữ liệu:
VD: int("10") -> biến kiểu dữ liệu string "10" thành số int 10
    age = int(input("nhap so tuoi: ")) # nhập tuổi, ép kiểu về int, gán vào biến age
Ex1: nhập số tuổi hiện tại, hiện lên màn hình tuổi của mình hiên tại và sau 5 năm.

'''

#3. Toán tử và biểu thức
'''
- Toán tử cơ bản: + - * /
- Phép chia lấy nguyên và lấy dư
    + chia lấy nguyên: 7 // 2 = 3
    + chia lấy dư: 7 % 2 = 1

Ex2: nhập hai số a, b, in ra màn hình kết quả +, -, *, /, //, % giữa 2 số a và b.
VD: 'a + b = ...'
'''







