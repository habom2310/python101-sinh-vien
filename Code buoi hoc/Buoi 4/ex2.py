n = int(input("nhap 1 so nguyen duong N = "))
a = []
print(f"nhap vao {n} so")
for i in range(n):
    so = int(input(f"nhap so thu {i + 1}: "))
    a.append(so)

tong = 0
tich = 1

temp_max = a[0]
idx_max = 0

for idx, element in enumerate(a):
    tong = tong + element
    tich = tich*element

    if element > temp_max:
        temp_max = element
        idx_max = idx

print("tong la: ", tong)
print("tich la: ", tich)

print(f"so lon nhat la: {temp_max}, o vi tri {idx_max + 1}")
