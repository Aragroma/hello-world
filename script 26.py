# Global, Local and Nonlocal variables
# ------------------------------------

# Global = outside any function
# can be called inside and outside the function

x = "global"

def foo():
    print("x inside:", x)
    y = x * 2
    print("2x inside:", y)

foo()
print("x outside:", x)

# but it is not possible to change the value of a global variable inside a function

a = "still global"

'''
def too():
    a = a * 2
    print("a inside:", a)

too()
'''
print("a outside:", a)

# Local = inside a function

def moo():
    b = "local"
    print("b inside:", b)

moo()
'''
print(b)
'''

# b is not definde outside the function

# global and local

print("x is still:", x)
print("a is:", a)

def goo():
    global x
    y = "local"
    x = x * 2
    print("the global x :", x)
    print("the local y:", y)

#before running the function, x remains the same
print(x)

goo()

# with the 'global' argument, the x is globally modified within the function
print(x)


# by declaring a new value to a variable inside the function, the value is stored localy but not altered globaly

def loo():
    x = 10
    print("the local x:", x)

loo()
print("the global x:", x)

# Nonlocal = inside a nested function, so neither local nor global

def outer():
    x = "local"

    def inner():
        x = "nonlocal"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()

# but it can still be altered with the nonlocal argument without altering the global


def outer2():
    x = "local"

    def inner2():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)

    inner2()
    print("outer:", x)

outer2()
print(x)

# global, local and nonlocal are "keywords"

# global in nested

z = 6

def zoo():
    z = 20

    def bar():
        global z
        z = 25

    print("Before calling bar: ", z)
    print("Calling bar now")
    bar()
    print("After calling bar: ", z)

print("Before calling zoo, z in main: ", z)
print("Calling zoo now")
zoo()
print("z in main: ", z)
