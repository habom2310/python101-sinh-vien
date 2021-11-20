# Bài 12: Module - package

## Module
'''
Khi tạo ra 1 file .py thì tạo ra 1 module. Tên module là tên file (bỏ đi .py)
Truy cập module:
 - import module_name
 - Các thứ truy cập được trong module:
    + biến
    + hàm
    + class

import test

print(test.a)
print(test.add(1, 2))
c = test.MyClass()
print(c.a)
'''

#Cách import module:
#C1:import tất cả
# import test

# print(test.a)
# print(test.add(1, 2))
# c = test.MyClass()
# print(c.a)

#C2: import 1 phần
# from test import add, MyClass
# print(add(1, 2))
# c = MyClass()
# print(c.a)

#C3: đặt biệt danh cho module
# import test as t
# from test import add as a
# print(a(1, 2))

## Package
'''
Package là 1 folder chứa nhiều module.
'''
# Cách import package:
# C1: import tuyệt đối (đường dẫn)
from package1 import module1
from package1.package2 import module2
print(module1.add(1, 2))
print(module2.multiply(2,3))
print(module1.multiply2(2,3,4))
#C2: import tương đối
import numpy as np
np.sum([1,2,3])

