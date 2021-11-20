x = input("nhap vao mot ky tu: ")
if 97 <= ord(x)  and ord(x) <= 122: # chu thuong
    print(" day la ky tu: ", x)
elif 60 <= ord(x) and ord(x) <= 90: # chu hoa
   print("day la ky tu: ", str(x).lower)
elif 48 <= ord(x) and ord(x) <= 57: # so
   print("so doi la: ", int(x)*(-1))
else: 
    print("ki tu dac biet")