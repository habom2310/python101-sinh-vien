"""
2. Khởi tạo 2 List có n phần tử kí tự 'a' - 'z'. Tìm phần tử chung giữa 2 list đó với:
a. n = 10
b. n = 100
c. n = 1000000
"""
import random
n = 100
v1 = ord("a")
v2 = ord("z")

l1 = []
l2 = []
for i in range(n):
    r1 = random.randint(v1, v2)
    c1 = chr(r1)
    l1.append(c1)

    r2 = random.randint(v1, v2)
    c2 = chr(r2)
    l2.append(c2)
print(l1)
print(l2)