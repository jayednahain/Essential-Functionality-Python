text ='banana'
space= 20
x = text.ljust(space)
print(x, "is my favorite food")
'''this willReturn a 20 characters long, 
left justified version of the word "banana"'''


print("fill up space portion with '-' symbol")
z = text.ljust(space,'-')
print(z, "is my favorite fruit")