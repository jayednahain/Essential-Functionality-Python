"""
   > pop() is a moethod
   > takes single argument
   > the argument pass in the method is optional
   > if the argument is not passed the defult index-1 passed as argument
        this is index of the last item
   > if the index passed to the method is not in range,
        it will be throws an error
"""
languages = ['Python', 'Java', 'C++', 'French', 'C']
print(languages)

return_value = languages.pop(3)
print("return_value:",return_value)
print(return_value)

list_tw