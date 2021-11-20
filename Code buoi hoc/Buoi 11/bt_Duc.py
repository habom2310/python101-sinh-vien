'''
BTVN:
Bài 1: Khai báo lớp Học sinh có các thành phần sau Tên, tuổi, giới tính, id (tự tăng theo số học sinh được nhập vào), điểm toán, văn, anh 
- Hàm __init__ tên, tuổi, giới tính
- Hàm get điểm, set điểm từng môn(điểm trong khoảng 0, 10)
- Hàm __repr__ in ra thông tin, điểm từng môn, điểm trung bình
- Hàm update thông tin với các named arguments (được học trong bài function) (tìm theo id để update)
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
class HocSinh:
    num = 0
    list_hs = []
    def  __init__(self,ten,tuoi:int,gender):
        self.ten = ten
        self.tuoi = tuoi
        self.gender = gender
        HocSinh.num += 1 
        self.__id =  HocSinh.num
        # HocSinh.list_hs.append([self.__id,self.ten,self.tuoi,self.gender])
        HocSinh.list_hs.append(self)

    # def diem(self,toan:float,van:float,anh:float):
    #     self.toan = toan
    #     self.anh = anh
    #     self.van = van
    #     self.trungbinh = (toan + van + anh) *1/3
    
    # C1
    # def set_diem_toan(self, diem_toan):
    #     self.__diem_toan = diem_toan
    
    # def get_diem_toan(self):
    #     return self.__diem_toan

    def get_id(self):
        return self.__id

    # C2
    def set_diem(self, diem, mon = "toan"):
        if mon == "toan":
            self.__diem_toan = diem
        elif mon == "van":
            self.__diem_van = diem
        elif mon == "anh":
            self.__diem_anh = diem

    def get_diem(self, mon = "toan"):
        if mon == "toan":
            return self.__diem_toan
        elif mon == "van":
            return self.__diem_van
        elif mon == "anh":
            return self.__diem_anh
        
    def get_diem_TB(self):
        return (self.__diem_toan + self.__diem_van + self.__diem_anh) / 3

    def __repr__(self):
        return(f"{self.__id}; {self.ten}; {self.tuoi} Tuổi; Giới tính {self.gender}; Điểm toán: {self.__diem_toan}; Điểm văn: {self.__diem_van}; Điểm anh: {self.__diem_anh}; Trung bình {self.get_diem_TB()}")
    
    # def update(self,id1, ten1,tuoi1,gender1):
    #     if self.__id == id1:
    #         self.ten = ten1
    #         self.tuoi = tuoi1
    #         self.gender = gender1
    #         HocSinh.list_hs[id1-1] = [id1,ten1,tuoi1,gender1]
    #         print(f"Sửa thông tin: {self.__id}; {self.ten}; {self.tuoi} Tuổi; Giới tính {self.gender}")
    #     else:
    #         print("Ko tìm thấy trong ds lớp")

    @classmethod
    def update(cls, id, ten, tuoi, gender):
        for hs in cls.list_hs:
            if hs.get_id() == id: # đây là bản ghi cần update
                hs.ten = ten
                hs.tuoi = tuoi
                hs.gender = gender
                break
    
    @classmethod
    def remove(cls, id):
        for i, hs in enumerate(cls.list_hs):
            if hs.get_id() == id:
                cls.list_hs.pop(i)
                break
    
    @classmethod
    def so_hs(cls):
        print("Số hs là:",cls.num)
        return cls.num
    
    @classmethod
    def get_all(cls):
        print("Danh sách lớp\n ",cls.list_hs)
        return cls.list_hs

    @classmethod
    def get_by_gender(cls,gender):
        list_hs_gt =[]
        for i in range(len(cls.list_hs)):
            if cls.list_hs[i][3] == gender:
                list_hs_gt.append(cls.list_hs[i])
        print(f"Danh sách học sinh {gender} là \n",list_hs_gt)
        return list_hs_gt

    @classmethod
    def get_by_id(cls,id:int):
        for i in range(len(cls.list_hs)):
            if cls.list_hs[i].get_id() == id:
                print(f"Học sinh STT {id} là: ",cls.list_hs[id-1])
                return cls.list_hs[i]
            else:
                print(f"Ko tìm thấy hs có id là {id}")
    
    @classmethod
    def add_new_student(cls, ten, tuoi, gender, diem_toan, diem_van, diem_anh):
        f = open("SV_db.txt", "a")
        f.write(f"{ten},{tuoi},{gender},{diem_toan},{diem_van},{diem_anh}\n")
        f.close()

    @classmethod
    def load_db(cls):
        f = open("SV_db.txt", "r")
        

a = HocSinh("Ng Van A",15,"nam")
b = HocSinh("Ng Van B",16,"nam")

HocSinh.add_new_student("Ng Van A",15,"nam",1,2,3)
# print([a, b])

a.set_diem(8, "toan")
a.set_diem(7, "van")
a.set_diem(9, "anh")

b.set_diem(8, "toan")
b.set_diem(7, "van")
b.set_diem(9, "anh")

print(HocSinh.list_hs)
print(HocSinh.get_by_id(1))

HocSinh.remove(1)
print(HocSinh.get_by_id(1))
print(HocSinh.list_hs)


# HocSinh.update(2,"Ng Van C",17,"nam")

# print(HocSinh.list_hs)

# a.set_diem(8, "toan")
# a.set_diem(7, "van")
# a.set_diem(9, "anh")
# print(a)

# a.update(2, "Ng Van C",17,"nam")
# print(a)

# a = HocSinh("Ng Van A",15,"nam")
# a_diem = a.diem(8.5,8,8)
# #print(a.__repr__)

# b= HocSinh("Ng Thi B",15,"nu")
# b_diem = b.diem(7,8,8.5)
# #print(b.__repr__)

# c = HocSinh("C",17,"nam")
# c_diem = c.diem(5,6,7)

# c_update = c.update(3,"Nguyen Van C",14,"nam")

# HocSinh.so_hs()
# HocSinh.get_all()
# HocSinh.get_by_gender("nam")
# HocSinh.get_by_gender("nu")
# HocSinh.get_by_id(4)