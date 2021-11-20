string = '12345abC(67'
tong = 0
for c in string:
    if 48 <= ord(c) and ord(c) <= 57:
        tong = tong + int(c)
    elif 60 <= ord(c) and ord(c) <= 90:
        print(c.lower())
    elif 97 <= ord(c)  and ord(c) <= 122:
        print(c)
    else:
        pass
print(tong)