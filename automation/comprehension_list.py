rendom_num= [1,2,3,4,5,6,7,88,99,45,65,2342,2344,5,7]

numbers_devide_by_3 = []

for item in rendom_num:
    if item%3==0:
        numbers_devide_by_3.append(item)

print("without using list comprehension",numbers_devide_by_3)              #new list      new list   inside the old list "whos are devide by 3"
print("using list comprehensions printing those item who are devide by 3 ", [new_item for new_item in rendom_num if new_item%3==0])
print("using list comprehensions printing those item who are devide by 4",[new_item for new_item in rendom_num if new_item%4==0])