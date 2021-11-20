'''
Bài 03: Viết hàm
        def is_perfect(n)
    để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
    Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi
    '''
def is_perfect(): # cho n vào argument
    n = int(input("nhập số cần kiểm tra:")) # khi viết hàm, ta ko dùng input để nhập giá trị. Giá trị input sẽ được đưa vào argument
    kt = 0
    for i in range(1 , n-1):
        if n % i == 0:
            kt += i
    
    if kt == n:
        print("số cần kiểm tra hoàn hảo")
    else:
        print("số cần kiểm tra hoàn hảo không hoàn hảo")
    return

is_perfect()
