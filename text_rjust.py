text ='banana'
space= 20
x = text.rjust(space)
print(x, "is my favorite food")
'''this willReturn a 20 characters long, 
left justified version of the word "banana"'''


print("fill up space portion with '-' symbol")
z = text.rjust(space,'-')
print(z, "is my favorite fruit")