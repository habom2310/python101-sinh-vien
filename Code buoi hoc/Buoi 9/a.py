"""
write a function calculate sum of all even numbers in a list
"""
def sum_even(lst):
    sum = 0
    for i in lst:
        if i % 2 == 0:
            sum += i
    return sum

