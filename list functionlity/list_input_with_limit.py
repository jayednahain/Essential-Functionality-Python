list=[]

n = int(input("enter limit of element: "))

for i in range(0,n):
   element_input = int(input(f'{i}.no element: '))
   
   list.append(element_input)

print(list)