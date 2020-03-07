# Python List: different types is an option
# -----------------------------------------
a = [5, 10, 15, 20, 25, 30, 35, 40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

# Lists are mutable: changeable
a[2] = 14
print("a[2] was changed: ", a)

# Python Tuple: Immutable Lists
# -----------------------------
t = (5, 'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# will generate an error
print("t[0] = 10 will generate an error!")
print("t[0] = 10")

# Python Set: unordered collection of unique items
# ------------------------------------------------
a = {5, 2, 3, 2, 5, 5, 3, 1, 4}

# data type of variable a
print(type(a))

# sets eliminates duplicates
a

# slicing = no option, it is unordered so it has no index
print("slicing a set is not possible, it has no indeces")
print("a[1]")

# Python Dictionary: unordered collection of key-value pairs
# ----------------------------------------------------------
d = {1:'value', 'key':2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
# Only key's are retrievable, values can only be accessed via the key
print("Generates error")
print("print('d[2] = ', d[2])")
