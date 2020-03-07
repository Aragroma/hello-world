# Data Types
#___________
# type() is the function to find the type

# Number data types
#------------------
# intergers = int
# floats = float
# complex numbers = complex

a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is of type", type(a))
print(a, "is complex number?", isinstance(1+2j, complex))
print(a, "is complex number 2.0?", isinstance(a, complex))

# limit of integer is limited by memory
# float is accurate up to 15 decimals and will be truncated, not rounded!

