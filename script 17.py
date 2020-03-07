# Operators

#  Arithmetic operators
x = 15
y = 4

print('x + y =', x + y)
print('x - y =', x - y)
print('x * y =', x * y)
print('x / y =', x / y)
print('x // y =', x // y)
print('x ** y =', x ** y)
print('x % y =', x % y)

# Comparison operators

x = 10
y = 12

print('x > y is', x > y)
print('x < y is', x < y)
print('x == y is', x == y)
print('x != y is', x != y)
print('x >= y is', x >= y)
print('x <= y is', x <= y)

# Logical operators

x = True
y = False

print('x and y is', x and y)
print('x or y is', x or y)
print('not x is', not x)

# Bitwise operators

x = 10
y = 4

print('x & y =', x&y) # and
print('x | y =', x|y) # or
print('~x =', ~x) # not
print('x ^ y =', x^y) # xor
print('x >> y =', x>>y) # right shift
print('x << y =', x<<y) # left shift

# Assignment operators

x = 5
print('x =', x)
x += 5
print('x += 5:', x)
x -= 5
print('x -= 5:', x)
x *= 5
print('x *= 5:', x)
x /= 5
print('x /= 5:', x)
x %= 5
print('x %= 5:', x)
x //= 5
print('x //= 5:', x)
x **= 5
print('x **= 5:', x)
y = 2
print('y =', y)
y &= 1
print('y &= 1:', x)
y |= 5
print('y |= 5:', x)
y ^= 5
print('y ^= 5:', x)
y >>= 5
print('y >>= 5:', x)
y <<= 5
print('y <<= 5:', x)

# Special operators
# -----------------

# Identity operators
# (is and is not)

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print('x1 is not y1')
print(x1 is not y1)

print('x2 is y2')
print(x2 is y2)

print('x3 is y3')
print(x3 is y3)
print("Lists are equal but not identical.")

# Membership operators
# (in and not in)

x = 'Hello world'
y = {1:'a', 2:'b'}

print('x =', x)
print('y =', y)

print("H in x?")
print('H' in x)

print("hello in x")
print('hello' in x)
print("Operator is case sensitive")

print("1 in y")
print(1 in y)

print("'a' in y")
print('a' in y)
print("Values from dictionaries are not traceble")
