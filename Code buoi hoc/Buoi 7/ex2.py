"""
Ex2: 
Nhập n số từ bàn phím. Sử dụng set để in ra các phần tử phân biệt
"""
n = int(input("Nhap n: "))

l = []
for i in range(n):
    so = int(input(f"nhap so thu {i + 1}: "))
    l.append(so)

print(set(l))
