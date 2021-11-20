def greet(name):

    name = name.strip() # bỏ dấu cách ở đầu và cuối
    l = name.split() # bỏ dấu cách ở giữa, sau khi split thì các chữ thành phần tử trong list l
    print(l)
    new_l = []
    n_char = 0 # đếm số chữ cái
    for s in l:
        print(s)
        new_s = s[0].upper() + s[1:].lower() # biến chữ đầu thành chữ hoa, phần còn lại thành chữ thường
        new_l.append(new_s)
        n_char += len(new_s)

    new_name = " ".join(new_l)
    print("Hello", new_name)
    return n_char

n_char = greet("  hA   Nguyen")
print(n_char)