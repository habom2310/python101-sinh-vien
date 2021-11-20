s = input("nhập chuỗi:")
abc = []

for y in range(128):
    abc.append(chr(y))
#cách dùng hàm count gg đc
for z in abc:
    if z in s:
        print(f"số lần xuất hiện của {z}",s.count(z))
#cách dùng vòng lặp (đang lỗi output)
for z in abc:
    xh = 0
    if z in s:
        for t in s:
            if z == t:
                xh += 1
        print(f"xuất hiện của {z} ",xh)

abc = []
y = input("nhập ký tự cần tìm:")
if y in s:
    for z,t in enumerate(s):
        if y == s[z]:
            abc.append(z)
    print(f"vị trí của ký tự {y}:",abc)
else:
    print(f"vị trí của ký tự {y}","-1")

y = input("nhập ký tự cần tìm:")
idx_y = []
if y in s:
    for z,t in enumerate(s):

        if y == s[z]:
            print(f"vị trí đầu tiên từ trái sang {y}",z)
            break
    for z,t in enumerate(s):    
        if y== s[z]:
            b = z
    print(f"vị trí đầu tiên từ phải sang {y}",b)
else:
    print(f"vị trí của ký tự {y}","-1")


