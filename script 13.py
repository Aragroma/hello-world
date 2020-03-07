# Python Strings
# --------------
# Sequence of Unicode characters
# single line: '' or ""
# multi line: ''' ''' or """ """"
# slicing operator [] is usable like in lists/tuples

s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error, also immutable
print("A string is, like a tuple, immutable. s[5] = 'd' will generate an error")
s[5] = 'd'
