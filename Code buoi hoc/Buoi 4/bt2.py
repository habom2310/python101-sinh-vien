n = (input("nhập số nguyên dương n:"))
a =[]

for i in range(len(n)):
    a.append(n[i])
for i in range(len(n)):
    if a[i] != a[len(n)-i-1]:
        print("n không là số đối xứng")
        break
    elif i < len(n)-1:
        continue
    else:
        print("n là số đối xứng")