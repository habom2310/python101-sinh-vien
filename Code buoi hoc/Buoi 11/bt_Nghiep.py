import os


class Student: 
    
    num = 0
    student_data = []
    def __init__(self , name , age , sex ):
        self.name = name
        self.age =  age
        self.sex =  sex
        self.ID = Student.num+ 1
        Student.num += 1
        Student.student_data.append (self)

    def grademath (self , get_grade_math ) : 
       while (get_grade_math < 0 or get_grade_math > 11 ):
           get_grade_math  = float ( input ("Please Input  math grade"))
       else: 
          self.real_math = get_grade_math
          return self.real_math  
        
    def gradelit (self , get_grade_lit ) : 
       while (get_grade_lit < 0 or get_grade_lit > 11 ):
           get_grade_lit  = int ( input ("Please Input  literature grade"))
       else: 
          self.real_lit = get_grade_lit
          return self.real_lit 
    def gradeeng ( self , get_grade_eng) :  
       while (get_grade_eng < 0 or get_grade_eng > 11 ):
           get_grade_eng  = int ( input ("Please Input  English grade"))
       else: 
          self.real_eng = get_grade_eng
          return self.real_eng 
  
    def averagegrade (self):
        self.aver_grade = (self.real_eng + self.real_math + self.real_lit)/3
        return self.aver_grade  
    def __repr__(self):
        return f'Student(ID = {self.ID}  , name={self.name}, age={self.age}, gender ={self.sex} , math = {self.real_math} , english = {self.real_eng} , literature = {self.real_lit} , average = {self.aver_grade})'
    def updateinfo (self, name ,age , sex ):
        self.name_update = name      
        self.age_update = age  
        self.sex_update = sex 
        for character in self.name_update:
          if character.isdigit() == True:
             print ("Please input again your name contain number ")
             self.name_update = input ("Please input your name : ")
             break
        
        if len(self.sex_update) < 2   : 
            if self.sex_update == 'M' or self.sex_update == 'F':               
               print (self.sex_update)
            else :
               print ("wrong input for sex")
               self.sex_update = input ("please input your sex : ")
        else:
            print ("wrong ")  
            self.sex_update = input ("please input your sex : ")  

    def remove(self): 
        ID_var = self.ID
        Student.student_data = [ele_ID for ele_ID in Student.student_data if ele_ID.ID !=  ID_var]
        
    @classmethod 
    def countStudent (cls):
        return cls.ID
    @classmethod 
    def getall (cls):
      return cls.student_data
    @classmethod 
    def get_all_by_gender (cls,gender): 
        return  [ele_gen for ele_gen in cls.student_data if ele_gen.sex == gender ]
    @classmethod 
    def find_by_id (cls, ID ):
        for ele_ID in cls.student_data:
            if ele_ID.ID == ID : 
                return ele_ID
    



Long = Student("Long",12, 'M')
Long.grademath(5)
Long.gradeeng (4)
Long.gradelit(3)
average_grade = Long.averagegrade()
print(Long.__repr__())

My = Student("My",12, 'F')
My.grademath(5)
My.gradeeng (3)
My.gradelit(3)
average_grade = My.averagegrade()
print(My.__repr__())


Bi = Student("Bi",16, 'M')
Bi.grademath(2)
Bi.gradeeng (4)
Bi.gradelit(6)
average_grade = Bi.averagegrade()
print(Bi.__repr__())

print ("\n")
print('Danh sách học sinh:',Student.getall())

print ("\n")
print('Danh sách học sinh nữ:',Student.get_all_by_gender('F'))

Student_removed = Student.find_by_id(3)
Student_removed.remove()
print ("\n")
print ("Danh sách học sinh :",Student.getall())