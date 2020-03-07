# More names and namespaces!!!
def outer_function():
    b = 20
    def inner_func():
        c =30
a = 10

# a = global namespace
# b = local namespace of outer_function()
# c = nested local namespace of inner_func()

# inside the inner_func()
# c = local and assignable
# b a = 'non local' / global ergo only readable

def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)

# accessing the correct namespace is possible

def outer_function():
    global a
    a = 20
    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)
