
print("-----------reverce integer--------------")
value = 1234567
print("the value is: ",value)
value_type= type(value)
print("value type: ",value_type)
value_convert_lsit = str(value)
print("value converted to string: ",value_convert_lsit)
reversed_value = value_convert_lsit[::-1]
print("reversed value: ",reversed_value)
print("current type is: ",type(reversed_value))
a=int(reversed_value)
print("convert again in integer: ",a)
print("current type is: ",type(a))