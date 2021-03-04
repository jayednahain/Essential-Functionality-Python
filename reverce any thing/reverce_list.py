Number_a =[1,2,3,4,5,6]
Alphabet_a = ["chowdhury","jayed","nahian"]


print("------------------")
print(Number_a)
Number_a_type = type(Number_a)
print("this is: ",Number_a_type)
count_number_list = len(Number_a)
print("numbers of element: ",count_number_list)
rever_list_number = Number_a[::-1]
print("reverced:",rever_list_number)

print("--------------------------------")

print(Alphabet_a)
Alphabat_a_type= type(Alphabet_a)
print("this is: ",Alphabat_a_type)
count_alphabet_list = len(Alphabet_a)
print("numbers of element: ",count_alphabet_list)
rever_list_alphabet =Alphabet_a[::-1]
print("reverced: ",rever_list_alphabet)
rever_element_alphabet = Alphabet_a[0][::-1],Alphabet_a[1][::-1],Alphabet_a[2][::-1]
rever_list_element = list(rever_element_alphabet)
print("reverced every element: ",rever_list_element)
print("---------------------------------------------------------")




