'''
Ex1: cho tuple: t = 1, 2, 3, "a", "b"
1. slicing từ t ra: ("a", "b")
2. +, *, slicing tạo ra ("a", "b", "a", "b", 1, 2, 3)
'''
t = 1, 2, 3, "a", "b"
t1 = t[3:]
print(t1)
t2 = t1*2 + t[:3]
print(t2)
