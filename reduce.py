from functools import reduce

list_numbers =[1,2,3,11,20,1,2,8]


def sum(a,b):
    return a+b

list_element_total_edition = reduce(sum,list_numbers)

print(list_element_total_edition)

