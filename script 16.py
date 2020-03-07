# Python input, output and import
# -------------------------------

# input: 'input()'
# output: 'print()'
print("This sentence is output to the screen")
# Output: This sentence is output to the screen

a = 5

print("The value of a is ", a)
# Output: The value of a is 5

# The default seperator is space.
# In case change is necessary, add 'sep= ...' to the syntax

print(1,2,3,4)

print(1,2,3,4, sep='*')
print(1,2,3,4, sep='#', end='&')

# Formatting output

a = 'bread'
b = 'butter'

print("I love {0} and {1}.".format(a,b))
print("I love {1} and {0}.".format(a,b))

# input() promts an input message:
num = input('Enter a number: ')

print(num)
print(type(num))

num = int(num)

print(num)
print(type(num))

# new type casting option: eval()
# type casting from str to int

sum1 = '2+3'
print(sum1)
print(type(sum1))

sum1 = eval(sum1)
print(sum1)
print(type(sum1))
