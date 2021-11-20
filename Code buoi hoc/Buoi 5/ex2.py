s = input("nhap vao 1 string: ")

count_list = [0 for i in range(26)] # list đếm số lần xuất hiện của từng chữ cái a->z

# count_list = [0, 0, 0, 0, 0, 0, 0 ...]
# alphabet   = [a, b, c, d, e, f, g ...]
# index      = [0, 1, 2, 3, 4, 5, 6 ...]

for i, c in enumerate(s):
    idx = ord(c) - ord("a") # ord("g") - ord("a"): khoảng cách từ chữ g -> a: index cua chu g trong list
    count_list[idx] += 1

for i in range(len(count_list)):
    if count_list[i] == 0:
        continue

    letter = chr(i + ord("a"))
    n = count_list[i]
    print(f"chu {letter} xuat hien {n} lan")

