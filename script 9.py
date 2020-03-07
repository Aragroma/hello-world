# Boolean literals
# The True and False of python, first letter capital, other small!
x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is ", x)
print("y is ", y)
print("a:", a)
print("b:", b)
print("In Python True = 1 and False = 0")

# Special literals
# Only the "None" excists

drink = "Available"
food = None

def menu(x):
    if x == drink:
        print(drink)
    else:
        print(food)

menu(drink)
menu(food)

# 'menu' is a function
