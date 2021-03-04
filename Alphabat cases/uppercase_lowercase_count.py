pra = "my NamE is ChowDhury jayeD nahian. i read in daffodil univercity.i am good. im addicted. i druncked"
split_sentence_list=pra.split('.')
print(split_sentence_list)
str_frist_string=str(split_sentence_list[0])

count_uppercase = 0
count_lowercase = 0
count_whitespace = 0
for char in str_frist_string:
    if char.isupper() ==True:
        count_uppercase=count_uppercase+1
    elif char.islower()==True:
        count_lowercase=count_lowercase+1
    elif char.isspace()==True:
        count_whitespace=count_whitespace+1
print("for frist value, uppercase: ",count_uppercase)
print("for frist value, lowercase: ",count_lowercase)
print("for frist value, whitespace:  ",count_whitespace)