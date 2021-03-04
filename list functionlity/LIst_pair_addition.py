arr= [1,2,3,4,5,6]
pair_addition_list = []

for i in range(0,len(arr),2):
   pair_addition_list.append(arr[i]+arr[i+1])

print(arr)
print(pair_addition_list)