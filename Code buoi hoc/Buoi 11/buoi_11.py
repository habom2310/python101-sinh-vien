# Bài 11 - OOP (tiếp)

"""
4 tính chất của OOP:
- Encapsulation: Tính đóng gói
- Inheritance: Tính kế thừa
- Polymorphism: Tính đa hình
- Abstraction: Tính trừu tượng

"""

'''
1. Tính đóng gói
Các thuộc tính hay method trong class có khả năng public/private, access modifier.
đặt 2 dấu "__" trước thuộc tính hay method để chuyển thành private
'''

"""
2. Tính kế thừa
- Cho phép 1 class có thể dùng lại code của 1 class khác (parent/child class)
- X kế thừa Y, Y kế thừa ông Z thì X kế thừa Z
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.breed = breed

    def bark(self, sound):
        return f"{self.name} nói {sound}"

class Chihuahua(Dog): # đặt tên của class được kế thừa trong ngoặc
    def __init__(self, name, age, sound = "gau gau"):
        super().__init__(name, age)
        self.sound = sound

    def bark(self): # C1: sử dụng super() để truy cập vào class cha.
        return super().bark(self.sound)

    # def bark(self, sound = "gau gau"): # C2: override.
    #     return f"{self.name} says {sound}"

class Golden(Dog):
    pass

dog1 = Chihuahua("1", 1)
dog2 = Golden("2", 3)
dog3 = Chihuahua("3", 2)

print(dog1.bark())
"""


"""
3. Tính đa hình
C2 trong ví dụ trên là biểu hiện của tính đa hình: Trong class con, ta có thể thêm sửa xóa các thuộc tính, hàm có cùng tên với class cha mà có tính năng khác hẳn.
"""

"""
4. Tính trừu tượng
from abc import abstractmethod, ABC # sử dụng thư viện ABC

class Dog(ABC): # class kế thừa class ABC (abtract)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod # keyword để cho biết hàm này là abstract
    def bark(self):
        pass

    def bark2(self): # optional. ko bắt buộc phải viết code cho hàm này
        pass

class Chihuahua(Dog):
    def bark(self):
        print("làm cái gì đấy")

dog1 = Chihuahua("1", 1)
"""

# from datetime import date, datetime

# print(datetime.now())

# class datetime2(datetime):
#     def __repr__(self):
#         return f"{self.now().time()} {self.now().date()}"

# dt2 = datetime2()
# print(datetime2)
