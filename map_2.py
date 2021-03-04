a = [1,2,3,4,5]

sqr_a =[]

for i in a:
    sqr_a.append(i**2)
    #print(sqr_a)

print(sqr_a)

print("similar out_put done using map function vai  creating a function")

def sqr(b):
    return b**2

list_result =[]

#map function using system: map(function_to_apply,list_of_items)

list_result = map(sqr,a)
print(list(list_result))