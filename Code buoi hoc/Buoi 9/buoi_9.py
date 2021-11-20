# Bài 9: Files, Directories, and Exceptions

# 9.1 Files

'''
File text: .txt có thể mở = nhiều phần mềm: notepad, visual code
File binary: đc mã hóa theo cách riêng, mở = phần mềm chuyên dụng (jpg, png mở bằng paint)

Mở file:
filename: đường dẫn đến file, ở dạng string
mode: chế độ sử dụng file:
    - r: đọc
    - w: ghi file từ đầu
    - a: ghi thêm vào cuối

Đọc file

- Đọc cả file 
f = open("a.txt","r")
print(f.read())

- Đọc theo dòng (C1)
f = open("a.txt","r")
print(f.readline())
print(f.readline())

- Đọc theo dòng (C2)
f = open("a.txt","r")
for line in f:
    print(line.replace("\n",""))

'''

'''
Ghi File

text = "Python"
print(text)
f = open("a.txt", "w")
f.write(text)
f.close()

Ex1: Viết 1 chương trình tạo 1 file "ex1.txt". Ghi 3 dòng "Hello" vào file, đóng file.
Sau đó tạo 1 file khác là "ex1_2.txt", copy paste nội dung từ file ex1.txt vào file ex1_2.txt, thêm 1 dòng "End" ở cuối file

f1 = open("ex1.txt", "w")
f1.write("Hello\nHello\nHello")
f1.close()

f2 = open("ex1.txt", "r")
text_from_f1 = f2.read()
f2.close()

f3 = open("ex1_2.txt", "w")
# new_text = text_from_f1 + "\n" + "End"
f3.write(text_from_f1)
f3.write("\nEnd")
f3.close()
'''

"""
Encode: Mã hóa

# ko mã hóa
f = open("a.txt", "w")
f.write("Xin chào")

# có mã hóa
f = open("a.txt", "wb")
my_str = "Xin chào"
my_str_as_byte = str.encode(my_str)
print(my_str_as_byte)
f.write(my_str_as_byte)

# đọc file byte (giải mã)
f = open("a.txt", "rb")
bytes_read_from_file = f.read()
print(bytes_read_from_file)
decode_str = bytes_read_from_file.decode()
print(decode_str)
"""

# 9.2 Directory
"""
# import os

# lấy đường dẫn hiện tại
# print(os.getcwd())

# đi sang thư mục khác
# print(os.chdir(".."))

# tạo thư mục mới
# os.mkdir("new_dir")

# đổi tên thư mục
# os.rename("new_dir", "old_dir")

# xóa thư mục
# os.rmdir("old_dir")

#xóa file
# os.remove("a.txt")

# kiểm tra file/folder tồn tại
import os
print(os.path.isfile("a.txt"))
print(os.path.isdir("<ten_folder>"))
print(os.path.exists("<ten_file_folder>"))
"""

# 9.3 Exception
"""

try:
    print(x)
except:
    print("co loi")

"""


'''
# BTVN

Viết chương trình mật mã Ceasar với yêu cầu sau:
- Chương trình có thể lưu trữ lại key (độ dịch chuyển d) vào file key.secret trong thư mục desktop.
- Nếu chưa có file hoặc trong đó không đúng format(chỉ có 1 số nguyên dương 0-26) thì yêu cầu nhập lại key và ghi vào.
- Nếu có rồi thì đọc lại giá trị
- Mã hóa và in ra màn hình kết quả được mã hóa
- Lưu lại các thao tác đã sử dụng chia theo cấu trúc folder của từng ngày tự động (logs/2021-08-15/timestamp_ceasar.log) trong đó ghi cụ thể key, đoạn text nhập vào, đoạn text mã hóa, ngày giờ - được encode dạng byte nhị phân
- Cho phép đọc đoạn log đó với một chế độ kiểm tra log của chương trình với input là ngày được nhập vào

'''
