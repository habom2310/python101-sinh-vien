d = {"a": 1, "b": 2, "c": 5, "f": 10}
c = input("nhap vao 1 chu cai: ")
## kiem tra input
if value := d.get(c): #neu value khac None
    print(f"gia tri cua key {c} la: {value}")
else:
    print(f"key {c} khong ton tai")