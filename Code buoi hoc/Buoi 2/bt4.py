#pt bac hai
import math
a = float(input("nhap he so a "))
b = float(input("nhap he so b "))
c = float(input("nhap he so c "))

if a == 0:
    if b == 0:
        print("vo nghiem")
    else:
        y = -c/b
else: # a khac 0
    delta = (b*b) - 4*a*c
    print("delta:",delta)
    if (delta < 0):
        print("vo nghiem")
    elif (delta == 0): 
        x = -(b/2*a)
        print ("nghiem kep ")
        print ("nghiem la ", x)
    else:
        x_1 =((-b + math.sqrt(delta))/(2*a))
        x_2 =((-b - math.sqrt(delta))/(2*a))
        print ("hai nghiem phan biet ")
        print ("nghiem 1 la ", x_1)
        print ("nghiem 2 la  ", x_2)