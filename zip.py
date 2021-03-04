""The zip()function returns 
an iterator of tuples based on the
iterable objects.""

number_list = ["one","two","three"]
str_list = [1,2,3]


result= zip()
print(result)
print(type(result))
print("---------------------------")

result_list = list(result)
print(result_list)
print(type(result_list))


print("---------------------------")

result_zip = zip(number_list,str_list)
result_zip_list = list(result_zip)
result_zip_set = set(result_zip)
print(result_zip)
print(result_zip_list)
print(result_zip_set)