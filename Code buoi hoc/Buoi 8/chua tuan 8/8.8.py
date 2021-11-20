'''
Bài 08: Viết hàm
        def body_mass_index(m, h)
    để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
      Viết hàm
        def bmi_information(m, h)
    để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
'''
m = float(input("nhập cân nặng theo kg:"))
h = float(input("nhập chiều cao theo m:"))

def body_mass_index(): # hàm sẽ nhận vào giá trị m và h (đặt trong argument)
    BMI = m/(h*h)
    print("BMI =", BMI)
    if BMI < 18.5:
        print("Gầy")
    elif BMI <25:
        print("Bình thường")
    else:
        print("Thừa cân")

    # Kết quả trả về dùng return (print chỉ để hiện ra màn hình)

body_mass_index()

#Chữa
def body_mass_index(m, h):
    BMI = m/(h*h)
    kq = ""
    if BMI < 18.5:
        kq = "Gầy"
    elif BMI <25:
        kq = "Bình thường"
    else:
        kq = "Thừa cân"

    return kq

m = 70 # trong các bài làm về hàm ko cần phải dùng input (fix cứng 1 giá trị bất kì)
h = 175
kq = body_mass_index(m, h)
print(kq)
