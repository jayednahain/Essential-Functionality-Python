x = input("enter a value for X: ")
y = input("enter a value for Y: ")

#crating a temp variable for swap values
print(f'before swap x = {x} and y= {y}')

temp = x # x tranfering value to temp
x = y # x is empty, y is transfering value to x

y = temp # now y is empty , temp is trafaring his value to y

print(f'after  swap x = {x} and y= {y}')

