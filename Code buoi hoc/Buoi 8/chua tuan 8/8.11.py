'''
Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
            F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
    Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
        + Hàm Đệ quy
        + Hàm Không đệ quy '''

def de_quy(n):
    if n < 3:
        return 1
    elif n == 3:
        return 2
    else:
        return de_quy(n-1) + de_quy(n-2) + de_quy(n-3)

n= int(input("nhập n:"))

print(f"số Tribonacci thứ {n} là:",de_quy(n))

