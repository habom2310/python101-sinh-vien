def is_int(input_str):
    print(input_str)
    if input_str[0] == "-" or input_str[0] == "+":
        input_str = input_str.replace(input_str[0], "")
    print(input_str)
    for c in set(input_str):
        if c < '0' or '9' < c:
            return False
    return True
