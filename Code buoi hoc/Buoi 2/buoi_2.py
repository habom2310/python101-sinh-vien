# Buổi 2: Cấu trúc rẽ nhánh if

#1.1 Kiểu dữ liệu boolean (bool)
'''
bool: True/False, 1/0
'''

#1.2 Các toán tử logic
'''
<, <=, >, >=, ==
!= : khác
'''

#1.3 Biểu thức logic
'''
and: và
or: hoặc
not: không

truth table

n^2 trường hợp với n = số biến
2 biến x, y có 2^2 = 4 trường hợp

X	    |Y	    |X and Y	|X or Y	    |not X
true	|true	|true	    |true	    |false
true	|false	|false	    |true	    |false
false	|true	|false	    |true	    |true
false	|false	|false	    |false	    |true

Bài 1:
Viết chương trình:
- Nhập vào giá trị của x (float), khai báo biến các biến boolean lưu kết quả và in ra: x > 0, x < 0, x == 0

- Nhập số double y, khai báo và in ra kết quả x > y, x <= y

In ra giá trị False and (x > y), True or (x <= y)

Bài 2:

Viết chương trình kiểm tra một ký tự c nhập vào từ bàn phím:

- Là ký tự thường
- Là ký tự in hoa
- Là số
- Là ký tự đặc biệt (không phải số, không phải chữ cái)
gợi ý: not (số) and not (chữ)

- Là dấu enter (null)
gợi ý: enter: ''

search: Ascii table

Hàm:
- ord(): lấy giá trị input của 1 kí tự
'''

#2. Cấu trúc rẽ nhánh. Câu lệnh if
'''
2.1: If
Nhập 1 số, kiểm tra nếu số đó lớn hơn 2 thì in ra chữ "Hello", nếu không thì ko thực hiện đoạn code đó.

Ex3: 
nhập vào 1 kí tự, kiểm tra xem là chữ thường hay hoa. Nếu là chữ thường thì biến thành chữ hoa.

2.2 if - else
nếu điều kiện trong phần if đúng thì sẽ thực hiện các câu lệnh trong block if
nếu điều kiện trong phần if sai thì sẽ thực hiện các câu lệnh trong block else

2.3 if - elif - else
- sử dụng khi có nhiều điều kiện cần kiểm tra.
- khi điều kiện thỏa mãn thì sẽ thực hiện các câu lệnh trong block đó, và bỏ qua các câu lệnh dưới nó.

truthy-falsy
x = 0
if x: #check x # 0 hay ko, đúng thì chạy block if, nếu sai chạy block else
    print("x # 0")
else:
    print("x = 0")

'''