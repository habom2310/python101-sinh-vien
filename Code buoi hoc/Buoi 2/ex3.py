x = 'a'

#kiem tra xem x co nằm trong khoảng từ a -> z hay ko (chữ thường)
if 97 <= ord(x) and ord(x) <= 122:
    print("x là chữ thường")

# kiểm tra chữ in hoa  A-Z
elif 'A' <= x and x <= 'Z':
    print("x là chữ in hoa")

# kiểm tra là số hay không 0-9
elif '0' <= x and x <= '9':
    print("x là số")

# ko là chữ hay số
else:
    print("x ko là số, cũng ko là chữ")

print("hết đoạn if else rồi")
