txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite") #it dosent print the space we given with banana
#The strip() method removes any leading (spaces at the beginning) 
# and trailing (spaces at the end) characters (space is the default leading character to remove)

txt_2 = ",,,,,,banana............rrrrrrr"
z = txt_2.strip(",.r ana")
print(z)