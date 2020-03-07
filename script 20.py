# The "if...elif...else"-statement

# If the numer is positive, we print an appropriate message
num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This also is always printed.")

# If else
num = 3
if num >= 0:
    print(num, "positive or zero")
else:
    print("negative")

num = -1
if num >= 0:
    print(num, "positive or zero")
else:
    print("negative")

num = 0
if num >= 0:
    print(num, "positive or zero")
else:
    print("negative")

# If elif else
num = 3
if num > 0:
    print(num, "positive")
elif num == 0:
    print(num, "zero")
else:
    print(num, "negative")

num = -4.5
if num > 0:
    print(num, "positive")
elif num == 0:
    print(num, "zero")
else:
    print(num, "negative")

num = 0
if num > 0:
    print(num, "positive")
elif num == 0:
    print(num, "zero")
else:
    print(num, "negative")

# also nestable
num = float(input("Enter a numer: "))
if num >= 0:
    if num == 0:
        print(num, "zero")
    else:
        print(num, "positive")
else:
    print(num, "negative")
