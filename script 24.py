# The pass statement
# ------------------

# a null statement, executable but no opration (NOP).
# used a a placeholder

# used for future programming

# used for loops, defs and classes
for val in "string":
    pass

# Functions
# ---------

# Syntax
'''
def function_name(parameters):
        """docstring"""
        statement(s)
'''

def greet(name):
    """This function greets to
    the person passed in as
    parameter"""
    print("Hello, " + name + ", Good morning!")

# Return
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >=0:
        return num
    else:
        return -num

print(absolute_value(2))
print(absolute_value(-4))


# Scope and lifetime
# a variable is in scope when it is defined in the level
# a variable is 'alive', as long as the level is not returned

x = 20

def my_func():
    x = 10
    print("Value inside function:",x)

my_func()
print("Value outside function:",x)


# Arguments
def greet(name,msg):
    """This function greets to
    the person with the provided message"""
    print("Hello, " + name + ', ' + msg)

greet("Monica", "Good morning!")

# Variable function arguments
# Default --> non default can NEVER follow default!

def greet(name, msg = "Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello, " + name + ', ' + msg)

greet("Kate")
greet("Bruce", "How do you do?")

# Arbitrary arguments

def greet(*names):
    """This function greets each
    person in the names as a tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)

greet("Monica", "Luke", "Steve", "John")

# Recursive functions
# similar to iteration

# e.g. factorial of a value

def calc_factorial(x):
    """This is a recursive function
    to find the factorial of a number"""

    if x == 1:
        return 1
    else:
        return(x * calc_factorial(x-1))
    
num = 4
print("The factorial of", num, "is", calc_factorial(num))
