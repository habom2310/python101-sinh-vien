"""

Viết chương trình mật mã Ceasar với yêu cầu sau:
- Chương trình có thể lưu trữ lại key (độ dịch chuyển d (kiểm tra 0-26)) vào file key.secret trong thư mục desktop.
- Nếu chưa có file hoặc trong đó không đúng format(chỉ có 1 số nguyên dương 0-26) thì yêu cầu nhập lại key và ghi vào.
- Nếu có rồi thì đọc lại giá trị
- Mã hóa và in ra màn hình kết quả được mã hóa
- Lưu lại các thao tác đã sử dụng chia theo cấu trúc folder của từng ngày tự động (logs/2021-08-15/timestamp_ceasar.log) trong đó ghi cụ thể key, đoạn text nhập vào, đoạn text mã hóa, ngày giờ - được encode dạng byte nhị phân
- Cho phép đọc đoạn log đó với một chế độ kiểm tra log của chương trình với input là ngày được nhập vào

a b c d e f g h i j k l m n o p q r s t u v w x y z # bảng chữ cái bth
độ dịch chuyển d = 4
e f g h i j k l m n o p q r s t u v w x y z a b c d # bảng chữ cái sau khi dịch

Chuỗi đầu vào (dựa vào bảng chữ cái bth): Hello
Chuỗi đầu ra (dựa vào bảng chữ cái sau khi dịch): Lipps

"""

input("nhập option: 1: mã hóa, 2: mở file log:")
import os
filepath = "key.secret" #phải đổi lại dấu \ thành / ???
# filepath = "C:\\Users\\ADMIN\\Desktop\\key.secret" 
if os.path.exists(filepath) == False:  
    f= open(filepath,"w+")
    d= input("nhap d:") # kiểm tra đầu vào (số nguyên dương)
    f.write(d)
else:
    f= open(filepath,"r")
    d= f.read() # d đang là str
    try:
        if int(d) in range(27): # d đang là str nên khi chuyển sang in thì có thể bị lỗi
            print("d la:",d)
    except:
        f= open(filepath,"w")
        d= input("nhập lại d:") #chưa có check
        f.write(d)

def kiem_tra_d(d):
    #kiểm tra d 0-26
    pass

def ma_hoa(s, d):
    '''
    input:
    s: chuỗi đầu vào
    d: độ dịch chuyển (0-26)

    output:
    y: chuỗi sau khi mã hóa
    ''' 
    y = ""
    i = 0
    while i < len(s):
        t = ord(s[i]) + d%26
        if (ord(s[i]) <= 90 and t>90) or (ord(s[i]) <= 122 and t > 122):
            t = t - 26
        y = y + chr(t)
        i = i+1

    # for c in s:
    #     # dịch c 1 khoảng d, thêm vào y

    return y

s = input("Nhập chuỗi cần mã hóa:")
y = ma_hoa(s, int(d))
print("chuỗi sau khi mã hóa:", y)
f.close()

'''
- Lưu lại các thao tác đã sử dụng chia theo cấu trúc folder của từng ngày tự động (logs/2021-08-15/timestamp_ceasar.log) trong đó ghi cụ thể key, đoạn text nhập vào, đoạn text mã hóa, ngày giờ - được encode dạng byte nhị phân
- Cho phép đọc đoạn log đó với một chế độ kiểm tra log của chương trình với input là ngày được nhập vào
'''
import datetime
if os.path.exists("logs") == False:
    os.mkdir("logs")

dt = datetime.datetime.now()
print(dt)

if os.path.exists("logs/" + str(dt.date())) == False:
    os.mkdir("logs/" + str(dt.date()))

log = open("logs/" + str(dt.date()) + "/timestamp_ceasar.log", "a+")
log_str = f"{d}, {s}, {y}, {str(dt)}\n"
log.write(log_str)
log.close()

