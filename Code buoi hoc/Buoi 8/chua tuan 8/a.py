"""
write a function take a list and return a dictionary with the 
number of occurance of each element
"""
def count_occurance(list_input):
    dict_output = {}
    for i in list_input:
        if i in dict_output:
            dict_output[i] += 1
        else:
            dict_output[i] = 1
    return dict_output

list_input = [1, 1, 2, 3, 3, 3]

dict_output = count_occurance(list_input)
print(dict_output)