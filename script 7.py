# Literals = raw data in a variable or constant
# numeric literals are immutable (unchangeable)

print('Numeric literals = type: Integer, Float and Complex')

# Integer literals
a = 0b1010 #binary literal
b = 100 #decimal literal
c = 0o310 #octal literal
d = 0x12c #hexadecimal literal

# Float literals
float_1 = 10.5
float_2 = 1.5e2

# Complex literal
x = 3.14j

print(a, b, c, d) # an integer literal is always printed as decimal
print(float_1, float_2) # 1.5e2 = 1.5 * 10^2
print(x, x.imag, x.real) # 'j' = the imagenary part
