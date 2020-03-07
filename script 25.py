# Lambda function in Python

double = lambda x: x * 2

#Output: 10
print("double(5)=", double(5))

# Similar to def function

def double_2(x):
    return x * 2

print("double_2(5)=", double_2(5))

# Lambda is used along side filter(), map(), etc.
# Program to filter out only the even items from a list

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

print(my_list)

new_list = list(filter(lambda x: (x%2 == 0), my_list))

# output new_list is only even

print(new_list)

new_uneven_list = list(filter(lambda x: (x%2 == 1), my_list))

print(new_uneven_list)
# list's remember the order
# a set can also be used

my_set = {8, 4, 3, 7, 17, 8}

print(my_set)

new_set = set(filter(lambda x: (x%2 == 0), my_set))

print(new_set)

# The map() function

new_list2 = list(map(lambda x: x * 2, my_list))

print(new_list2)

# with set's experiment

new_set2 = set(map(lambda x: x * 2, my_set))

print(new_set2)
