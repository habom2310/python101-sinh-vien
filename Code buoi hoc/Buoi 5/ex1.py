s = '\t Hello \t moi nguoi, I\'m Ha\n'

# a = s.split()
# a = ['Hello', 'moi', 'nguoi,', "I'm", 'Ha']
# C1: truy cập vào phần tử a[2] đổi kí tự , -> .
# element2 = a[2] # element2 = "nguoi,"
# new_element2 = element2[:-1]
# new_element2 = new_element2 + "."
# print(new_element2)
# a.pop(2)
# a.insert(2, new_element2)
# print(a)

# C2: dùng replace
s = s.replace("\n", "")
s = s.replace("\t", "")
s = s.strip()
s = s.replace(",", ".")
s = s.replace("  ", " ")
print(s)