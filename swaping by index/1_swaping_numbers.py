def swapFUn(list,pos_1,pos_2):

    list[pos_1],list[pos_2] = list[pos_2],list[pos_1]
    return print("new list",list)





list = [11,22,33,44,55,66]
print("old list",list)

pos_1 =1
pos_2 =3

print(swapFUn(list,pos_1-1,pos_2-1))