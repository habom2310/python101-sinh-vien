# Buổi 8: Hàm - function

## 8.1 Định nghĩa/ Cú pháp
'''
Cấu trúc 1 function bao gồm:
- bắt buộc: từ khóa (def), tên function (my_function), thân hàm/các dòng code được thực thi
- ko bắt buộc (optional): argument, doc string (comment giải thích), return

def my_function(argument1, argument2): # keyword: def <tên hàm>(<tham số truyền vào>):
    return_value1 = argument1 + 10
    return_value2 = argument2 + "Hello"
    print("argument1", argument1)
    print("argument2", argument2)

    return return_value1, return_value2
    
ret1, ret2 = my_function(1,"a")
print(ret1, ret2)
'''

## 8.2 Cách gọi hàm/Call stack
'''
<tên hàm>()
'''

## 8.3 Tham số truyền vào
'''
# 1. tham số bắt buộc
def func_1(arg1, arg2): # tham số bắt buộc
    print("arg1 =", arg1)
    print("arg2 =", arg2)

func_1(1, 2) # phải truyền đủ số tham số đã khởi tạo, nếu ko bị TypeError

# 2. tham số ko bắt buộc
def func_1(arg1, arg2, arg3 = 1): 
    print("arg1 =", arg1)
    print("arg2 =", arg2)
    print("arg3 =", arg3)

# func_1(1, 2) # ko truyền arg3, giá trị arg3 bằng giá trị default
func_1(1, 2, 3) # truyền arg3 = 3, giá trị tham số bị thay đổi

# 3. truyền tham số theo tên
def func_1(arg1, arg2, arg3 = 1): 
    print("arg1 =", arg1)
    print("arg2 =", arg2)
    print("arg3 =", arg3)

func_1(arg3 = 1, arg2 = 2, arg1 = 3) 

- Chú ý: Các tham số bắt buộc để lên trước, các tham số ko bắt buộc để ở sau
- Nếu ko phải truyền tham số theo tên thì cần truyền đúng thứ tự
'''

## 8.4 Giá trị trả về (return)
'''
- Từ khóa: return. Chạy đến return là kết thúc hàm
- Hàm có thể ko trả về cái j, có thể có 1 hoặc nhiều giá trị
- Các giá trị return ở dạng tuple

def calculation(a, b):
    sum = a + b
    mul = a * b
    return sum, mul

so1 = 1
so2 = 2
tong, tich = calculation(a = so1, b = so2)

print(f"{so1} + {so2} = {tong}")
print(f"{so1} * {so2} = {tich}")

# return với if-else
def calculation(a, b, tong_hay_tich):
    if tong_hay_tich == "tong":
        tong = a + b
        return tong
    elif tong_hay_tich == "tich":
        tich = a * b
        return tich
'''

'''
Ex1: tạo 1 function tên là greet, nhận vào tên người.
- Chuẩn hóa tên rồi in ra (chữ cái đầu viết hoa, các phần cách nhau 1 dấu cách, ko có dấu cách thừa ở đầu, cuối)
- In ra "Xin vào <tên người đó>"
- Trả về số chữ cái trong tên người đó (ko dấu). In ra màn hình kết quả.

'''

## 8.5 Global vs Local variable
'''
#1. biến global, truy cập (đọc giá trị/ read-only) được cả trong lẫn ngoài hàm (với immutable datatype: int, str, float)
x = 'global'
print("x outside:", x)

def func():
    print("x inside:", x)

func()

#2. tạo biến x global, trong hàm gán giá trị mới cho x. x trong hàm là local variable, x global ko thay đổi giá trị
x = 1
print("x outside before:", x)

def func():
    x = 2
    print("x inside:", x)

func()
print("x outside after:", x)

#3. tạo biến x global, trong hàm thay đổi giá trị x. Lỗi do hàm hiểu x ở bên phải dấu = là local variable và chưa đc khởi tạo
x = 1
print("x outside before:", x)

def func():
    x = x + 1
    print("x inside:", x)

func()
print("x outside after:", x)
> UnboundLocalError: local variable 'x' referenced before assignment

#4. Khởi tạo biến x trong hàm. in giá trị x ngoài hàm
def func():
    x = 1
    print("x inside:", x)

func()
print("x outside:", x)
> NameError: name 'x' is not defined

# 5. khởi tạo 1 list global l. trong hàm append thêm 1 phần tử. Sau khi chạy hàm, list l có thêm 1 phần tử (đã bị thay đổi so với ban đầu): kiểu dữ liệu mutable (dict, list) sẽ bị thay đổi trong hàm.

l = [1]
print("before ", l)

def them(l):
    l.append(2)

them(l)
print("after ", l)
'''

"""
Bài 01: Viết hàm
        def max_min(list_number)
    trả lại cả giá trị max, min của nhiều số được truyền vào

Bài 02: Viết hàm
        def reverse_string(str)
    trả lại chuỗi đảo ngược của chuỗi str

Bài 03: Viết hàm
        def is_perfect(n)
    để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
    Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi

Bài 04: Viết hàm
        def is_prime(n)
    để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False

Bài 05: Viết hàm
        def count_upper_lower(str)
    trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str

Bài 06: Viết hàm
        def is_pangram(str, alphabet)
    đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
    Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần

Bài 07: Viết hàm
        def create_matrix(n, m)
    xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j

Bài 08: Viết hàm
        def body_mass_index(m, h)
    để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
      Viết hàm
        def bmi_information(m, h)
    để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h

Bài 09: Viết hàm
        def change_upper_lower(str)
    chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str

Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
        Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)

Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
            F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
    Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
        + Hàm Đệ quy
        + Hàm Không đệ quy

Bài 12: Viết hàm
        def find_x(a_list, x)
    trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1

Bài 13. Thực hiện code lại hàm sau và cho biết ý nghĩa của nó
def enter_data():
    while True:
        n = input("Nhập 1 số nguyên: ")
        if n.isnumeric():
            n = int(n)
            if n > 0:
                print("Đã nhập số dương")
                return n
            print("Đã nhập số không dương. Chương trình sẽ tiếp tục!")
        else:
            print("Dữ liệu đã nhập không phải số nguyên")
"""