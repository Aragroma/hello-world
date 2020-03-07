""" The Zen of Python
    -----------------
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

import this
# Where the Zen of Python is stored

# A name is the identifier that is given to an object.
# eg. a = 2, a is the name and 2 is the object.

# The adress of the object is the same as the adress of the name:
# [Only after the name is assigned]
a = 2
print('a =', a)
print('id(2) =', id(2))
print('id(a) =', id(a))
print("if a is raised by one")
a += 1
print('a =', a)
print('id(a) =', id(a))
print('lo and behold: id(3) =', id(3))
print("and now we make a new name 'b'for 2")
b = 2
print('b =', b)
print('id(b) =', id(b))

# The dynamic nature of Python lies in this name binding, where no new objects need be created

# Functions are objects too.
def printHello():
    print("Hello")

a = printHello()

a

print(id(printHello()))
print(id(a))
