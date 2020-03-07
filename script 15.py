# Implicit type Conversion: automatic conversion
# ----------------------------------------------
# (Python interpreter's decision)

num_int = 123
num_flo = 1.23
print("Value of num_int = ", num_int)
print("Value of num_flo = ", num_flo)

num_new = num_int + num_flo

print("datatype of num_int: ", type(num_int))
print("datatype of num_flo: ", type(num_flo))

print("Value of num_new = ", num_new)
print("datatype of num_new: ", type(num_new))

# integer < float
# Python always converts from a smaller data type to a larger one to avoid data loss>

# string and integer gives the following

num_str = "456"

print("datatype of num_str: ", type(num_str))

print('''gives a typeerror:
num_new = num_int + num_str
print("Value of num_new = ", num_new)
print("datatype of num_new: ", type(num_new))''')

# Explicit type Conversion: forced conversion
# -------------------------------------------
# (programmers decision)
# also called 'Type Casting'
# data loss in possible

num_str = int(num_str)
print("datatype of num_str after type casting: ", type(num_str))

num_new = num_int + num_str

print("Value of num_new = ", num_new)
print("datatype of num_new: ", type(num_new))
