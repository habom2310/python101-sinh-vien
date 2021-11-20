from handle_data import check_data_file_created, create_data_file, \
    get_all_data, update_data

class SinhVien:
    num = 0 # class variable
    data = [] # class 
    
    field_names = ['id', 'name', 'age', 'gender']

    def __init__(self, name, age, gender, id=None, from_db=False):
        if not from_db:
            self.name = name
            self.age = age
            self.gender = gender
            self.id = self.__class__.num + 1 # len(self.__class__.data) + 1
            self.__class__.num += 1 # HocSinh.num += 1 hard code -> self.__class__ -> HocSinh
            self.__class__.data.append(self)
            self.__class__.update_data()
        else:
            self.name = name
            self.age = age
            self.gender = gender
            self.id = int(id)
            self.__class__.num = int(id)
            self.__class__.data.append(self)

          
    def __repr__(self):
        return  (f'<Student id: {self.id}, name: {self.name},' + 
            f'age: {self.age}, gender: {self.gender}>')
        
    def update_info(self, name=None, age=None, gender=None):
        if name:
            self.name = name
        
        if age:
            self.age = age
        
        if gender:
            self.gender = gender

        self.__class__.update_data()
    
    def remove(self):
        current_idx = self.id

        self.__class__.data = [
            element for element in self.__class__.data if element.id != current_idx
        ]

        self.__class__.update_data()

    @classmethod
    def update_data(cls):
        update_data(cls.data_fpath, cls.field_names, cls.data)

    @classmethod
    def get_or_create_data_file(cls, folder_name, file_name):
        cls.data_fpath = folder_name + '/' + file_name # khai báo thêm 1 class variable
        if check_data_file_created(cls.data_fpath):
            for current_student_data in get_all_data(cls.data_fpath):
                cls(**current_student_data, from_db=True)
        else:
            create_data_file(cls.data_fpath, cls.field_names)

    @classmethod
    def count(cls):
        return cls.num
    
    @classmethod
    def get_all(cls):
        return cls.data

    @classmethod
    def get_all_by_gender(cls, gender):
        return [element for element in cls.data if element.gender == gender]

    @classmethod
    def find_by_id(cls, idx):
        for element in cls.data:
            if element.id == idx:
                return element

        return None