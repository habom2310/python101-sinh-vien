# Buổi 10 - OOP (Object Oriented Programming) - Lập trình hướng đối tượng

"""
Nội dung:
- Khái niệm
- Class, instance, attribute, method
"""

## 10.1 Khái niệm
'''
class: loài mèo
instance/object: từng con mèo cụ thể

Ví dụ:

class ClassMeo: # tên class viết liền, viết hoa các chữ cái đầu mỗi từ
    def __init__(self, name, owner):
        self.name = name # để tạo, gán thuộc tính (attribute) cho đối tượng (object), sử dụng 'self.<tên thuộc tính> = giá trị'
        self.owner = owner

    def make_sound(self):
        print(f"I am {self.name}. My owner is {self.owner}")

boss = ClassMeo("Boss", "Con Sen") # 1 object của ClassMeo 
print(boss.name, boss.owner)
boss.make_sound()
miu = ClassMeo("Miu", "Con Sen") # 1 object của Class Meo
print(miu.name, miu.owner)
miu.make_sound()

'''

'''
Ex1: Khai báo class `Shape`
- Thuộc tính (attribute)
  - Tên
  - Số cạnh
- Phương thức (method)
  - hàm `print_info()`, hàm này sẽ print ra:  `Hình tam giác có 3 cạnh`
'''

"""
2 Phương thức đặc biệt trong class:
  -  __init__(): để khởi tạo object 
  -  __repr__(): để in ra giá trị khi print(obj)

  def __repr_(self):
      return "cái mà mình muốn print ra"
"""

'''
Ex2: 
Khai báo 1 class `ComplexNumber`
- Thuộc tính: phần thực, phần ảo
- Khai báo hàm __repr__ để in ra số phức đó (có dạng (a + bi))
- Khai báo các phương thức: add(), substract(), multiply(), divide()
trong class ComplexNumber - Yêu cầu: giá trị trả về là 1 ComplexNumber.
'''

"""
10.2. Class method - Class variable

"""
class ClassMeo: # tên class viết liền, viết hoa các chữ cái đầu mỗi từ
    num = 0 # thuộc tính của class

    def __init__(self, name, owner):
        self.name = name # để tạo, gán thuộc tính (attribute) cho đối tượng (object), sử dụng 'self.<tên thuộc tính> = giá trị'
        self.__owner = owner # thuộc tính của object
        ClassMeo.num += 1

    def make_sound(self):
        print(f"I am {self.name}. My owner is {self.__owner}")

    @classmethod # phải có cái này trước khi khai báo method của class
    def get_num_object(cls):
        print("Số mèo (object) đã được tạo là: ", cls.num)

boss = ClassMeo("Boss", "Con Sen")
print(boss.__owner)

'''
BTVN:
Bài 1: Khai báo lớp Học sinh có các thành phần sau Tên, tuổi, giới tính, id (tự tăng theo số học sinh được nhập vào), điểm toán, văn, anh 
- Hàm __init__ tên, tuổi, giới tính
- Hàm get điểm, set điểm từng môn(điểm trong khoảng 0, 10)
- Hàm __repr__ in ra thông tin, điểm từng môn, điểm trung bình
- Hàm update thông tin với các named arguments (được học trong bài function)
    - name
    - age
    - gender

2. Bổ sung vào bài 1
- Class method count cho phép trả về số học sinh
- Class method get_all cho phép lấy toàn bộ học sinh
- Class method get_all_by_gender với đối số là nam, nữ cho phép lấy thông tin học sinh theo giới tính
- Class method find_by_id tìm kiếm học viên bằng id và trả về một đối tượng HocSinh
- Khai báo thêm instance method remove để remove học viên đã tìm thấy
- Ví dụ: a = HocSinh.find_by_id(1); a.remove()

3. Bổ sung vào bài 2:
Viết chương trình với các tính năng
- Thêm, học viên
- Chỉnh sửa thông tin học viên
- Xóa học viên
- List all học viên
- Filter nam, nữ
- Toàn bộ dữ liệu được lưu vào file

'''